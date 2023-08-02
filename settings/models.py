from django.db import models

from core.models import BaseClass


class Settings(BaseClass):
    site_title = models.CharField('Site Title', max_length=32)
    logo = models.ImageField('Site Logo', upload_to='media')

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.site_title
