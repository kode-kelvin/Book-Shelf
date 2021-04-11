from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),













]
