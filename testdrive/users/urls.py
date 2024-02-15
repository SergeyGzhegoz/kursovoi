from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register, profile

urlpatterns = [
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
