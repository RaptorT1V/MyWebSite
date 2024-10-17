import re, logging
from django import forms
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, get_user_model
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=18, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not phone[0].isdigit():
            raise forms.ValidationError('The phone number must begin with a digit.')

        phone = re.sub(r'\D', '', phone)

        if len(phone) != 11 or not phone.startswith(('7', '8')):
            raise forms.ValidationError('The phone number must contain 11 digits and begin with “7” or “8”.')

        formatted_phone = f"+7 ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}-{phone[9:11]}"

        if CustomUser.objects.filter(phone=formatted_phone).exists():
            raise forms.ValidationError('User with this phone number already exists.')

        return phone


class CustomAuthenticationForm(forms.Form):
    username_or_email = forms.CharField(label='Username or Email', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')

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

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Чувак, твои login credentials получили инвалидность')

        self.cleaned_data['user'] = user
        return self.cleaned_data
