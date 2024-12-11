from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit_language, name='edit_language'),
    path('delete/<int:id>/', views.delete_language, name='delete_language'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_exchange/', views.add_exchange, name='add_exchange'),
    path('exchange_list/', views.exchange_list, name='exchange_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    
]
