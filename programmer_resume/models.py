from django.db import models


class ProgrammerResume(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.TextField()
    github_url = models.URLField(max_length=200)
    habr_url = models.URLField(max_length=200, blank=True, null=True)
    cv_pdf = models.FileField(upload_to='cv_pdfs/')
    diploma_image = models.ImageField(upload_to='diplomas/')

    def __str__(self):
        return self.full_name
