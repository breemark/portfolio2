from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns 
from frontpage.views import change_language


urlpatterns = [
    path('change_language/', 
         change_language, 
         name='change_language')
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('frontpage.urls')),
    # path('projects/', include('projects.urls')),
)


admin.site.site_header = "BREEMARK"
admin.site.site_title = "Breemark"
admin.site.index_title = "Welcome, Breemark 🐉"