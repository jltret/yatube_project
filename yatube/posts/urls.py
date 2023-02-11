# posts/urls.py
from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='mainpage'),
    # Отдельная страница с информацией о посте
    path('group/<slug:slug>/', views.group_list, name='group_posts')
]
