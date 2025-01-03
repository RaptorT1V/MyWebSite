from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(pre_save, sender=Profile)
def delete_old_avatar(sender, instance, **kwargs):
    if instance.pk:  # Проверяем, что профиль уже существует
        old_avatar = Profile.objects.get(pk=instance.pk).avatar
        new_avatar = instance.avatar
        if old_avatar and old_avatar != new_avatar:
            old_avatar.delete(save=False)  # Удаляем старый аватар
