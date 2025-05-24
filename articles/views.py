from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Comment
from django.contrib import messages
from django.shortcuts import redirect

from .models import *

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html' 

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'  # Para usar {{ article }} en el template
    
    def post(self, request, *args, **kwargs):
        article = self.get_object()
        if request.user.is_authenticated:
            Comment.objects.create(
                content=request.POST.get('content'),
                article=article,
                author=request.user
            )
            messages.success(request, '¡Comentario añadido!')
        return redirect('article_detail', pk=article.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.object)  # Todos los comentarios del artículo
        return context

class ArticleCreateView(TemplateView):
    template_name = 'article/article_create.html'

class ArticleUpdateView(TemplateView):
    template_name = 'article/article_update.html'

class ArticleDeleteView(TemplateView):
    template_name = 'article/article_delete.html'