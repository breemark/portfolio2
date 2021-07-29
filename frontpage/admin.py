from django.contrib import admin
from .models import FrontPage, Language

# Register your models here.
class FrontPageAdmin(admin.ModelAdmin):
    pass

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Language, LanguageAdmin)
admin.site.register(FrontPage, FrontPageAdmin)
