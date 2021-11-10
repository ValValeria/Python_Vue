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
    image = models.ImageField(upload_to="")
    category = models.CharField(choices=categories, default="js", max_length=30)
    stars = models.IntegerField()
    content = models.TextField(max_length=4000)
