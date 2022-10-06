from django.db import models

# Create your models here.

class Infos(models.Model):
    title=models.CharField(max_length=10)
    summary=models.TextField()
    running_time=models.TextField()
