from django.urls import path
from . import views

app_name = 'merch'

urlpatterns = [
    path('', views.index, name='index'),
]
