from django.db import models
from frontpage.models import Language

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=120, null=True, blank=True)
    picture = models.ImageField(blank=True, null=True, upload_to='projects/')
    language = models.ForeignKey(
        Language, 
        on_delete=models.DO_NOTHING,
        blank=True, 
        null=True
    )
