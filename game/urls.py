from django.urls import path
from . import views
from game.views import ninja, typing, snake, save_score

app_name = 'game'

urlpatterns = [
    path('', views.index, name='index'),
    path('ninja/', ninja, name='ninja'),
    path('typing/', typing, name='typing'),
    path('snake/', snake, name='snake'),
    path('save_score/', save_score, name='save_score'),
]
