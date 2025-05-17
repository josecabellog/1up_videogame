from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name= 'article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name = 'article_detail'),
    path('article/create/', ArticleCreateView.as_view(), name = 'article_create'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name = 'article_update'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name = 'article_delete'),
]