from django.db import models


class StreamingService(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    logo = models.ImageField(upload_to='musician_resume/img/')

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    logo = models.ImageField(upload_to='musician_resume/img/')

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    url = models.FileField(upload_to='musician_resume/audio/')
    cover = models.ImageField(upload_to='musician_resume/img/')

    def __str__(self):
        return f"{self.title} by {self.artist}"
