from django.conf import settings
from .models import Language


def languages_processor(request):
    current_language = request.LANGUAGE_CODE
    languages = Language.objects.all()
    return {'current_language': current_language, 'languages': languages}