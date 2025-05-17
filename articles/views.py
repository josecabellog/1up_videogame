from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import *

class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html' 

class ArticleDetailView(TemplateView):
    template_name = 'article/article_detail.html'

class ArticleCreateView(TemplateView):
    template_name = 'article/article_create.html'

class ArticleUpdateView(TemplateView):
    template_name = 'article/article_update.html'

class ArticleDeleteView(TemplateView):
    template_name = 'article/article_delete.html'