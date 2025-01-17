from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import (
    GitHubProfile, GitHubRepository,
    HabrProfile, HabrArticle,
    AcademicWork, GoogleDriveFolder, Certificate
)
import logging

logger = logging.getLogger(__name__)


def index(request):
    try:
        # Получаем данные GitHub
        github_profile = GitHubProfile.objects.first()
        github_repos = GitHubRepository.objects.all()
        logger.debug(f"Loaded GitHub profile and {github_repos.count()} repositories")

        # Получаем данные Habr
        habr_profile = HabrProfile.objects.first()
        habr_articles = HabrArticle.objects.all()
        logger.debug(f"Loaded Habr profile and {habr_articles.count()} articles")

        # Получаем академические работы
        academic_works = AcademicWork.objects.all()
        logger.debug(f"Loaded {academic_works.count()} academic works")

        # Получаем папку Google Drive
        drive_folder = GoogleDriveFolder.objects.first()
        if not drive_folder:
            logger.warning("No Google Drive folder found")

        # Получаем сертификаты
        certificates = Certificate.objects.all()
        logger.debug(f"Loaded {certificates.count()} certificates")

        # Формируем контекст
        context = {
            'github_profile': github_profile,
            'github_repos': github_repos,
            'habr_profile': habr_profile,
            'habr_articles': habr_articles,
            'academic_works': academic_works,
            'drive_folder': drive_folder,
            'certificates': certificates,
        }

    except ObjectDoesNotExist as e:
        logger.error(f"Error loading data: {str(e)}")
        context = {
            'error_message': "Some content is temporarily unavailable"
        }
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        context = {
            'error_message': "An unexpected error occurred"
        }

    return render(request, 'programmer_resume/index.html', context)
