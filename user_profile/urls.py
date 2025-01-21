from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('', views.user_profile_view, name='user_profile'),
    path('profile/<str:username>/', views.user_profile_view, name='user_detail'),
]
