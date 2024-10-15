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
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
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
                          {'form': form, 'error': 'Too many attempts. Try again in 10 seconds.'})

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
