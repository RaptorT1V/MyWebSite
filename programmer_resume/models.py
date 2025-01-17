from django.db import models

class GitHubProfile(models.Model):
    profile_url = models.URLField()
    profile_image = models.ImageField(upload_to='programmer_resume/img/')

    class Meta:
        verbose_name = "GitHub Profile"
        verbose_name_plural = "GitHub Profile"

class GitHubRepository(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "GitHub Repository"
        verbose_name_plural = "GitHub Repositories"

    def __str__(self):
        return self.name

class HabrProfile(models.Model):
    profile_url = models.URLField()
    profile_image = models.ImageField(upload_to='programmer_resume/img/')

    class Meta:
        verbose_name = "Habr Profile"
        verbose_name_plural = "Habr Profile"

class HabrArticle(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Habr Article"
        verbose_name_plural = "Habr Articles"

    def __str__(self):
        return self.title

class AcademicWork(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='programmer_resume/docs/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class GoogleDriveFolder(models.Model):
    folder_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='programmer_resume/img/certificates/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title