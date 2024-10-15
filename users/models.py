from django.contrib.auth.models import AbstractUser
from django.db import models
import re


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    def save(self, *args, **kwargs):
        self.phone = re.sub(r'\D', '', self.phone)  # Убираем все символы, кроме цифр
        if self.phone.startswith('8'):
            self.phone = '7' + self.phone[1:]  # Заменяем 8 на 7
        self.phone = f"+7 ({self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}"
        super().save(*args, **kwargs)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Добавляем related_name для избежания конфликта
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions_set',  # Добавляем related_name
        blank=True
    )


class UserScore(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    current_score = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.current_score}/{self.highest_score}'
