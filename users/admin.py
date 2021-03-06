from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("avatar", "nickname", "is_social_login")}),
    ) + UserAdmin.fieldsets
