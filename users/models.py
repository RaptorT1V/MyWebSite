from django.contrib.auth.models import AbstractUser
from django.db import models
import re
from django.core.validators import MinValueValidator


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=18, unique=True, verbose_name="Номер телефона")
    wallet = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Баланс кошелька"
    )

    def save(self, *args, **kwargs):
        self.phone = re.sub(r'\D', '', self.phone)
        if self.phone.startswith('8'):
            self.phone = '7' + self.phone[1:]
        self.phone = f"+7 ({self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}"
        super().save(*args, **kwargs)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions_set',
        blank=True
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
