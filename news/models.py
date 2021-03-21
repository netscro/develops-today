from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django_extensions.db.fields import AutoSlugField


class Posts(models.Model):
    """
    Data fields of posts in database
    """
    title = models.CharField(max_length=200, unique=True)
    link = AutoSlugField(populate_from='title', max_length=200, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    vote_count = models.IntegerField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    """
    Data fields of comments in database
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField(max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True)
    comment_post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.creation_date}'
