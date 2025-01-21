from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import GameScore


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_game_score(sender, instance, created, **kwargs):
    if created:
        GameScore.objects.create(user=instance)