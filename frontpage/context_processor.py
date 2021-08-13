from django.conf import settings
from .models import Language
from articles.models import Article
from projects.models import Project


def languages_processor(request):
    current_language = request.LANGUAGE_CODE
    languages = Language.objects.all()
    articles = Article.objects.all()
    projects = Project.objects.all()

    context = {
        'current_language': current_language, 
        'languages': languages,
        'articles': articles,
        'projects': projects,
    }

    return context