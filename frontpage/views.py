
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from .models import FrontPage

# Create your views here.
def home(request):
    frontpage = FrontPage.objects.all().filter(language__code=request.LANGUAGE_CODE).last()
    
    if frontpage is None:
        frontpage = FrontPage.objects.all().filter(language__code='en-us').last()

    return render(request, 'frontpage/home.html', {'frontpage': frontpage})


def change_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response


    