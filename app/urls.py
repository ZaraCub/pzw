from django.urls import path
from . import views
from .views import (
    LanguageListView, LanguageDetailView,
    UserListView, UserDetailView,
    ExchangeListView, ExchangeDetailView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit_language, name='edit_language'),
    path('delete/<int:id>/', views.delete_language, name='delete_language'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_exchange/', views.add_exchange, name='add_exchange'),
    path('exchange_list/', views.exchange_list, name='exchange_list'),

    # ListViews
    path('languages/', LanguageListView.as_view(), name='language_list'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('exchanges/', ExchangeListView.as_view(), name='exchange_list'),

    # DetailViews
    path('languages/<int:pk>/', LanguageDetailView.as_view(), name='language_detail'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('exchanges/<int:pk>/', ExchangeDetailView.as_view(), name='exchange_detail'),
]
