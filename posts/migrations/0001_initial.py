# Generated by Django 2.1.1 on 2020-09-05 22:31

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('photo', models.ImageField(blank=True, upload_to=posts.models.photo_path)),
            ],
        ),
    ]