from django.urls import path
from . import views
from .views import (
    LanguageListCreateAPIView, LanguageRetrieveUpdateDestroyAPIView,
    UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView,
    ExchangeListCreateAPIView, ExchangeRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Funkcijski prikazi
    path('', views.index, name='index'),
    path('edit_language/<int:id>/', views.edit_language, name='edit_language'),
    path('delete_language/<int:id>/', views.delete_language, name='delete_language'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_exchange/', views.add_exchange, name='add_exchange'),

    # Generički prikazi
    path('languages/', views.LanguageListView.as_view(), name='language_list'),
    path('languages/<int:pk>/', views.LanguageDetailView.as_view(), name='language_detail'),
    path('languages/add/', views.LanguageCreateView.as_view(), name='language_add'),
    path('languages/<int:pk>/edit/', views.LanguageUpdateView.as_view(), name='language_edit'),
    path('languages/<int:pk>/delete/', views.LanguageDeleteView.as_view(), name='language_delete'),

    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

    path('exchanges/', views.ExchangeListView.as_view(), name='exchange_list'),
    path('exchanges/<int:pk>/', views.ExchangeDetailView.as_view(), name='exchange_detail'),
]


urlpatterns += [
    path('api/languages/', LanguageListCreateAPIView.as_view(), name='api_language_list_create'),
    path('api/languages/<int:pk>/', LanguageRetrieveUpdateDestroyAPIView.as_view(), name='api_language_detail'),
    path('api/users/', UserListCreateAPIView.as_view(), name='api_user_list_create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='api_user_detail'),
    path('api/exchanges/', ExchangeListCreateAPIView.as_view(), name='api_exchange_list_create'),
    path('api/exchanges/<int:pk>/', ExchangeRetrieveUpdateDestroyAPIView.as_view(), name='api_exchange_detail'),
]