from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, 'articles/home.html', {'articles': articles})


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article.html', {'article': article})