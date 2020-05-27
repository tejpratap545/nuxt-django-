from django.db import models
from app.Users.models import User


class Tag(models.Model):
    tagname = models.CharField(max_length=50)

    def __str__(self):
        return self.tagname


class video(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    video_url = models.URLField()
    image = models.URLField()

    def __str__(self):
        return self.name
