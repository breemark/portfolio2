from django.conf import settings
from .models import Language


def languages_processor(request):
    languages = Language.objects.all()
    return {'languages': languages}