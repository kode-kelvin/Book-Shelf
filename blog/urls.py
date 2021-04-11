from django.urls import path
from . import views
import members
from .views import AddBookView, DeleteBookView, UpdateBookView, UserEntryListView
from django.contrib.auth import views as auth_views
from members import views as user_views
from members.views import PasswordsChangeView
from django.urls import reverse_lazy


app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='about'),
    path('book_delete/<int:pk>/delete', DeleteBookView.as_view(), name='book_delete'),
    path('book_update/<int:pk>/update', UpdateBookView.as_view(), name='book_update'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('user/<str:username>', UserEntryListView.as_view(), name='user-posts'),



    path('profile/', user_views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),


    path('password_change/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='pass-change'),
    path('password_success', views.password_success, name="password_success"),



    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),


    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', success_url='/'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),






    path('<slug:post>/', views.post_single, name='post_single'),  # myprobelm
    path('category/<category>/', views.CatListView.as_view(), name='category'),


]
