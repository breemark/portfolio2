from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    code = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name


class FrontPage(models.Model):
    """Front page of your Portfolio. Only the latest version will be loaded"""
    bio = models.TextField(null=True, blank=True)
    picture =  models.ImageField(blank=True, null=True, upload_to='picture/') 
    cv_resume = models.FileField(blank=True, null=True, upload_to='resume/')
    email = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    skype = models.CharField(max_length=120, null=True, blank=True)
    wechat = models.CharField(max_length=120, null=True, blank=True)
    facebook = models.CharField(max_length=120, null=True, blank=True)
    instagram = models.CharField(max_length=120, null=True, blank=True)
    linkedin = models.CharField(max_length=120, null=True, blank=True)
    language = models.ForeignKey(
        Language, 
        on_delete=models.DO_NOTHING,
        blank=True, 
        null=True
    )

    def __str__(self):
        return f"Version {self.id}"
