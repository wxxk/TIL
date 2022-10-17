from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(400, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    thumbnail = ProcessedImageField(
        upload_to="articles/images",
        processors=[Thumbnail(400, 400)],
        format="JPEG",
        options={"quality": 80},
    )
