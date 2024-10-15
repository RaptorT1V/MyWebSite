import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import authenticate


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = re.sub(r'\D', '', phone)
        if len(phone) != 11 or not phone.startswith(('7', '8')):
            raise forms.ValidationError('Номер телефона должен содержать 11 цифр и начинаться с 7 или 8.')
        return phone


class CustomAuthenticationForm(AuthenticationForm):
    username_or_email = forms.CharField(label='Username or Email', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')

        if '@' in username_or_email:
            user = CustomUser.objects.filter(email=username_or_email).first()
            if user:
                username = user.username
            else:
                raise forms.ValidationError('Invalid email or username')

        if username:
            user = authenticate(username=username, password=password)
            if user:
                self.cleaned_data['user'] = user
            else:
                raise forms.ValidationError('Invalid login credentials')
        else:
            raise forms.ValidationError('Invalid login credentials')

        return self.cleaned_data
