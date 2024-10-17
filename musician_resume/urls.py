from django.urls import path
from . import views

app_name = 'musician_resume'

urlpatterns = [
    path('', views.index, name='index'),
]
