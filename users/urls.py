from django.urls import path
from django.shortcuts import redirect
from .views import register_view, login_view, profile_view, logout_view

urlpatterns = [
    path('', lambda request: redirect('login')),  # Перенаправление на страницу входа
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
]