from django.urls import path
from . import views
from users.views import register, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', user_logout, name='logout'),
]
