from django.db import models

# Create your models here.


class Github(models.Model):
    github_url = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)

    def __str__(self):
        return self.github_url
