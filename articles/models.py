from django.db import models
from frontpage.models import Language
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from unidecode import unidecode


# Create your models here.
class Article(models.Model):
    """Article Model"""
    title = models.CharField(max_length=120, unique=True)
    subtitle = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from='title_format')
    content = RichTextUploadingField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='articles/')
    language = models.ForeignKey(
        Language, 
        on_delete=models.DO_NOTHING,
        blank=True, 
        null=True
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def title_format(self):
        return unidecode(self.title)