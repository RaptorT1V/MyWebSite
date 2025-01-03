from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# Функция проверки типа загружаемого файла
def validate_image_file(file):
    if not file.name.endswith(('.jpg', '.jpeg', '.png')):
        raise ValidationError("Ты чё, шутник? Файл должен быть .jpg, .jpeg, или .png!")


@login_required
def user_profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

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
        elif 'old_password' in request.POST:
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Пароль успешно изменён!')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        if 'old_password' in field:
                            messages.error(request, 'Чё, склероз настиг, дружище? Ты свой текущий пароль ввёл неверно!')
                        elif 'new_password2' in field:
                            messages.error(request, 'Чё, слепошарый? Ты хотя бы смотри, на какие клавиши нажимаешь! Новые пароли не совпадают!')
                        else:
                            messages.error(request, error)
            return redirect('user_profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'user_profile/profile.html', {
        'user': request.user,
        'password_form': form
    })