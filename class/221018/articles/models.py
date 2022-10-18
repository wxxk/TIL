from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
