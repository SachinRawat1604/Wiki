from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<str:title>/', views.article_detail, name='article_detail'),
    path('create/', views.create_article, name='create_article'),
    path('edit/<str:title>/', views.edit_article, name='edit_article'),
    path('delete/<str:title>/', views.delete_article, name='delete_article'),
]