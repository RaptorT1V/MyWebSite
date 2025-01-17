from django.contrib import admin
from .models import (
    GitHubProfile, GitHubRepository, 
    HabrProfile, HabrArticle,
    AcademicWork, GoogleDriveFolder, Certificate
)

admin.site.register(GitHubProfile)
admin.site.register(GitHubRepository)
admin.site.register(HabrProfile)
admin.site.register(HabrArticle)
admin.site.register(AcademicWork)
admin.site.register(GoogleDriveFolder)
admin.site.register(Certificate)