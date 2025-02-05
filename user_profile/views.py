from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib import messages

User = get_user_model()


# Функция проверки типа загружаемого файла
def validate_image_file(file):
    if not file.name.endswith(('gif', '.jpg', '.jpeg', '.png', '.webp')):
        raise ValidationError("Ты чё, шутник? Файл должен быть .jpg, .jpeg, или .png!")


@login_required
def user_profile_view(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
        is_owner = request.user == user
    else:
        user = request.user
        is_owner = True

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)

    # Если пользователь загружает новый аватар на своей странице профиля
    if is_owner:
        if request.method == 'POST':
            if 'avatar' in request.FILES:
                avatar = request.FILES['avatar']
                try:
                    validate_image_file(avatar)
                    profile.avatar = avatar
                    profile.save()
                    messages.success(request, 'Аватар успешно обновлён!')
                except ValidationError as e:
                    messages.error(request, e.message)
            elif 'delete_avatar' in request.POST:
                profile.avatar.delete()
                messages.success(request, 'Аватар удалён к чёртовой матери!')

    # Если пользователь меняет пароль на своей странице профиля
        if 'old_password' in request.POST:
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Пароль успешно изменён!')
                return redirect('user_profile:user_profile')
            else:
                if form.errors.get('old_password'):
                    messages.error(request, 'Чё, склероз настиг, дружище? Ты СВОЙ ТЕКУЩИЙ ПАРОЛЬ ввёл неверно!')
                if form.errors.get('new_password2'):
                    messages.error(request, 'Чё, слепошарый? Ты хотя бы смотри, на какие клавиши нажимаешь! НОВЫЕ ПАРОЛИ у тебя не совпадают! (ну или же ты придумал фиговый пароль)')
                if form.errors.get('old_password') and form.errors.get('new_password2'):
                    messages.error(request, 'Ооо, хахах, ты ВООБЩЁ ВСЁ НЕПРАВИЛЬНО ввёл! И старый пароль, и новый пароль...')
        else:
            form = PasswordChangeForm(user=request.user)
    else:
        form = None

    context = {
        'profile_user': user,
        'is_owner': is_owner,
        'password_form': form
    }

    return render(request, 'user_profile/profile.html', context)