from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    categories = (
        ("js", "javascript"),
        ("python", "python"),
        ("ml", "machine learning"),
        ("android", "android development"),
        ("other", "other"),
    )
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="app/static/images")
    category = models.CharField(choices=categories, default="js", max_length=30)
    stars = models.IntegerField()
    content = models.TextField(max_length=4000)
    objects = models.Manager
    users_likes = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Carousel(models.Model):
    pages = (
        ("posts", "posts"),
        ("post", "post"),
        ("categories", "categories")
    )
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="app/static/images")
    link = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    page = models.CharField(choices=pages, max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time = models.DateTimeField()
    objects = models.Manager

    def __str__(self):
        return self.title
