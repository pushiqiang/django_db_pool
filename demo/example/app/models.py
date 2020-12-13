from django.db import models


class User(models.Model):
    name = models.CharField(unique=True, max_length=50)
    age = models.IntegerField()


class Category(models.Model):
    index = models.IntegerField(verbose_name='序号', default=0)
    name = models.CharField(verbose_name='分类', unique=True, max_length=50)
