from django.urls import path
from . import views

app_name = 'programmer_resume'

urlpatterns = [
    path('', views.index, name='index'),
]
