from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django_ratelimit.decorators import ratelimit


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Success! Регистрация прошла успешно! Congratulations, buddy!')
            return redirect('home')
        else:
            # Убираем дублирующее сообщение,
            # Вот это я называю Epic Fail! Регистрация провалена! Пожалуйста, исправьте Ваши ошибки, представленные ниже.'
            # которое отображает общую ошибку регистрации
            pass  # Удаляем строку с messages.error
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


@ratelimit(key='ip', rate='5/m', method='POST', block=False)
def user_login(request):
    if request.method == 'POST':
        was_limited = getattr(request, 'limits', False)
        if was_limited:
            form = CustomAuthenticationForm()
            return render(request, 'users/login.html',
                          {'form': form, 'error': 'Слишком много попыток, чел! Try again in 10 seconds.'})

        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.cleaned_data['user'])
            return redirect('user_profile')
        else:
            return render(request, 'users/login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = CustomAuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
