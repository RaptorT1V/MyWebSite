from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm



def login_required_view(request):
    # Получаем оригинальный запрошенный путь из параметра 'next'
    next_url = request.GET.get('next', '/').strip('/')

    # Запрещаем перенаправление на страницы, которые требуют авторизации
    protected_pages = ['login-required', 'login', 'register']
    if next_url in protected_pages:
        next_url = '/'  # Перенаправляем на главную страницу

    # Словарь для перевода URL в понятные названия
    page_names = {
        'game': 'Игры',
        'forum': 'Форум',
        'merch': 'Мерч',
        'musician-resume': 'Резюме музыканта',
        'programmer-resume': 'Резюме программиста',
    }

    # Получаем название страницы из словаря или используем URL как есть
    page_name = page_names.get(next_url, next_url.capitalize())

    # Преобразуем next_url в полный путь
    if not next_url.startswith('/'):
        next_url = '/' + next_url + '/'

    context = {
        'page_name': page_name,  # Передаём название страницы в контекст
        'next_url': next_url,  # Добавляем next_url в контекст
    }

    return render(request, 'users/login_required.html', context)


def login_view(request):
    next_url = request.GET.get('next', '/')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'С возвращением, {username}!')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('home')
            else:
                messages.error(request, 'Твой username или password -- инвалид! Please try again.')
        else:
            messages.error(request, 'У нас форма -- invalid! Please correct the errors below.')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def register(request):
    next_url = request.GET.get('next', '/')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Success! Регистрация прошла успешно! Congratulations, buddy!')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            pass
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def user_logout(request):
    username = request.user.username
    logout(request)
    messages.info(request, f"Вы вышли из системы. Прощайте, {username}!")

    return redirect('home')
