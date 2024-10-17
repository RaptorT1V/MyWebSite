import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import authenticate
from django.utils.safestring import mark_safe
from django.urls import reverse


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=18, required=True)  # Увеличен max_length для корректного ввода

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        # Проверяем, чтобы первый символ был числом
        if not phone[0].isdigit():
            raise forms.ValidationError('The phone number must begin with a digit.')

        phone = re.sub(r'\D', '', phone)  # Убираем все символы, кроме цифр

        # Проверка на длину и начало номера
        if len(phone) != 11 or not phone.startswith(('7', '8')):
            raise forms.ValidationError('The phone number must contain 11 digits and begin with “7” or “8”.')

        # Форматируем номер так, как он будет сохранен в базе
        formatted_phone = f"+7 ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}-{phone[9:11]}"

        # Проверяем, уникален ли отформатированный номер
        if CustomUser.objects.filter(phone=formatted_phone).exists():
            raise forms.ValidationError('User with this phone number already exists.')

        return phone


class CustomAuthenticationForm(forms.Form):
    username_or_email = forms.CharField(label='Username or Email', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')

        # Логика аутентификации по email или имени пользователя
        if '@' in username_or_email:
            user = CustomUser.objects.filter(email=username_or_email).first()
            if not user:
                raise forms.ValidationError(
                    mark_safe('Такого e-mail не существует! Хотите <a href="{}">зарегистрироваться</a>?'.format(reverse('register')))
                )
            username = user.username
        else:
            user = CustomUser.objects.filter(username=username_or_email).first()
            if not user:
                raise forms.ValidationError(
                    mark_safe('Такого имени не существует! Хотите <a href="{}">зарегистрироваться</a>?'.format(reverse('register')))
                )
            username = username_or_email

        # Аутентификация пользователя по username и паролю
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Чувак, твои login credentials получили инвалидность')

        self.cleaned_data['user'] = user
        return self.cleaned_data
