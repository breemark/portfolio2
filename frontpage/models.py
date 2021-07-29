from django.db import models

# Create your models here.
class FrontPage(models.Model):
    """Front page of your Portfolio. Only the latest version will be loaded"""
    bio = models.TextField(null=True, blank=True)
    cv_resume = models.FileField(blank=True, null=True, upload_to='resume/')
    email = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    skype = models.CharField(max_length=120, null=True, blank=True)
    wechat = models.CharField(max_length=120, null=True, blank=True)
    facebook = models.CharField(max_length=120, null=True, blank=True)
    instagram = models.CharField(max_length=120, null=True, blank=True)
