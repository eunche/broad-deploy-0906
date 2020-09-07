import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.conf import settings
from . import models as post_models
from .models import Comment
from .forms import PostForm
from .forms import CommentForm

# Create your views here.


def post_list(request):
    all_posts = post_models.Post.objects.all().order_by("-created_date")
    all_posts = all_posts[:30]
    sorted_posts = post_models.Post.objects.all().order_by("-views")
    top3_posts = sorted_posts[:3]
    return render(
        request,
        "posts/post_list.html",
        {"all_posts": all_posts, "top3_posts": top3_posts},
    )


def post_my(request):
    return render(request, "posts/my_post_list.html")


def post_detail(request, post_id):
    aws_url = settings.MY_AWS_URL
    post_detail = get_object_or_404(post_models.Post, pk=post_id)
    comments = post_detail.comments.filter(target_comment__isnull=True)
    try:
        is_scraped = request.user.scraped.filter(pk=post_id).exists()
    except:
        is_scraped = ""

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_detail
            comment.user = request.user
            if request.POST.get("pk") is not None:
                comment.target_comment = Comment.objects.get(
                    pk=int(request.POST.get("pk"))
                )
            comment.save()

            return redirect(reverse("posts:detail", kwargs={"post_id": post_id}))
    else:
        form = CommentForm()
    return render(
        request,
        "posts/post_detail.html",
        {
            "post_detail": post_detail,
            "comments": comments,
            "form": form,
            "is_scraped": is_scraped,
            "aws_url": aws_url,
        },
    )


def post_write(request):
    if request.user.is_anonymous:
        return redirect("users:login")
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("/post/")

    else:
        form = PostForm()
    return render(request, "posts/post_write.html", {"form": form})


def post_update(request, post_id):
    post = get_object_or_404(post_models.Post, pk=post_id)
    if post.user != request.user:
        raise Http404("권한이 없습니다.")
    form = PostForm(request.POST, request.FILES, instance=post, auto_id=True)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/post/" + str(post_id))
    else:
        form = PostForm(instance=post)
        return render(request, "posts/post_update.html", {"form": form})


def post_delete(request, post_id):
    post = post_models.Post.objects.get(pk=post_id)
    if post.user == request.user:
        post.delete()
        return redirect("/post/")
    else:
        raise Http404("권한이 없습니다.")


def add_comment_to_post(request, post_id):
    post = get_object_or_404(post_models.Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("/post/" + str(post_id))
    else:
        form = CommentForm()
    return render(request, "posts/post_add_comment.html", {"form": form})


def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user != request.user:
        raise Http404("권한이 없습니다.")
    else:
        comment.delete()
        return redirect("/post/" + str(post_id))


@login_required
@require_POST
def ajax_scrap(request):
    if request.method == "POST":
        user = request.user
        pk = request.POST.get("pk", None)
        post = post_models.Post.objects.get(pk=pk)
        if user.scraped.filter(pk=pk).exists():
            post.scraped.remove(user)
        else:
            post.scraped.add(user)
    context = {}
    return HttpResponse(json.dumps(context), content_type="application/json")


def scrap_post_list(request):
    user = request.user
    posts = post_models.Post.objects.filter(scraped=user)
    posts = posts.order_by("-created_date")
    return render(request, "posts/scrap_post_list.html", {"posts": posts})
