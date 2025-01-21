from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Track, StreamingService, SocialLink
from django.core.serializers.json import DjangoJSONEncoder
import json


@login_required
def index(request):
    tracks = Track.objects.all().order_by('title')  # Получаем все треки и сортируем по названию
    streaming_services = StreamingService.objects.filter()  # Получаем активные стримминговые сервисы
    social_links = SocialLink.objects.exclude()  # Получаем социальные ссылки и исключаем неактивные

    # Создаем контекст
    context = {
        'streaming_services': streaming_services,
        'social_links': social_links,
        'tracks': tracks,
    }

    # Добавляем JSON для JavaScript
    tracks_json = json.dumps(
        [{'title': t.title, 'artist': t.artist,
          'url': t.url.url, 'cover': t.cover.url}
         for t in tracks],
        cls=DjangoJSONEncoder
    )
    context['tracks_json'] = tracks_json

    return render(request, 'musician_resume/index.html', context)
