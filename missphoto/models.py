from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    thema = models.CharField(max_length=200)
    user_id = models.ForeignKey(User)
    created = models.DateField(auto_now=True)


class Good(models.Model):
    post_id = models.ForeignKey(Post)
    user_id = models.ForeignKey(User)


class Bad(models.Model):
    post_id = models.ForeignKey(Post)
    user_id = models.ForeignKey(User)


class PhotosData(models.Model):
    post_id = models.ForeignKey(Post)
    data = models.TextField()
