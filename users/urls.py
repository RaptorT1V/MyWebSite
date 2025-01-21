from django.urls import path
from users.views import login_view, register, user_logout, login_required_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('login-required/', login_required_view, name='login_required'),
    path('logout/', user_logout, name='logout'),
]
