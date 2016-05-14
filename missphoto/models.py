from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user_id = models.ForeignKey(User)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.created)


class Good(models.Model):
    post_id = models.ForeignKey(Post)
    user_id = models.ForeignKey(User)

    def __str__(self):
        return str(self.user_id) + ":" + str(self.post_id)


class Bad(models.Model):
    post_id = models.ForeignKey(Post)
    user_id = models.ForeignKey(User)

    def __str__(self):
        return str(self.user_id) + ":" + str(self.post_id)


class PhotosData(models.Model):
    post_id = models.ForeignKey(Post)
    name = models.CharField(max_length=200, default='default')
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    post_id = models.ForeignKey(Post)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
