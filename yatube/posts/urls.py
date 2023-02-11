# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком постов пользователя
    # path('posts/', views.posts_list),
    # Отдельная страница с информацией о посте
    path('group/<slug:slug>/', views.group_posts),
]
