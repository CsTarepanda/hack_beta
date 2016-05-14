from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    pass


class Posts(models.Model):
    thema = models.CharField(max_length=200)
    user_id = models.ForeignKey(CustomUser)
    created = models.DateField(auto_now=True)


class Goods(models.Model):
    post_id = models.ForeignKey(Posts)
    user_id = models.ForeignKey(CustomUser)


class Bads(models.Model):
    post_id = models.ForeignKey(Posts)
    user_id = models.ForeignKey(CustomUser)
