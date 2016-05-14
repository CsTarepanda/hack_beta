from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    thema = models.CharField(max_length=200)
    user_id = models.ForeignKey(User)
    created = models.DateField(auto_now=True)


class Goods(models.Model):
    post_id = models.ForeignKey(Posts)
    user_id = models.ForeignKey(User)


class Bads(models.Model):
    post_id = models.ForeignKey(Posts)
    user_id = models.ForeignKey(User)


class Photos_datas(models.Model):
    post_id = models.ForeignKey(Posts)
    data = models.TextField()
