from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

# TODO Create StackOverflow model


class Github(models.Model):
    github_url = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    # image = models.ImageField(upload_to="profileImg/%Y/%m/%d/")
    title = models.CharField(
        max_length=100, default=""
    )  # which keywords used to search
    language = models.CharField(
        max_length=100, default=""
    )  # which language used to search
    added_date = models.DateTimeField(
        datetime.now(tz=timezone.utc), default=timezone.now
    )
    alt = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.github_url
