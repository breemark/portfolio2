from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'language', )

admin.site.register(Project, ProjectAdmin)