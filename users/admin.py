from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Регистрация кастомной модели пользователя
admin.site.register(CustomUser, UserAdmin)
