from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    abstract = models.CharField(max_length=255)
    body = models.CharField(max_length=1024)
    date = models.DateField()
    time_to_read = models.IntegerField()
    image = models.CharField(max_length=1024)


class Tag(models.Model):
    tag = models.CharField(max_length=32)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
