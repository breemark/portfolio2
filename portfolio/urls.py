from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns 
from frontpage.views import change_language
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('change_language/', 
         change_language, 
         name='change_language')
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('frontpage.urls')),
    path('projects/', include('projects.urls')),
    path('articles/', include('articles.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    prefix_default_language=True
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "BREEMARK"
admin.site.site_title = "Breemark"
admin.site.index_title = "Welcome, Breemark 🐉"