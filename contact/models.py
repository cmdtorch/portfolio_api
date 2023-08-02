from django.db import models

from core.models import BaseClass


class Message(BaseClass):
    full_name = models.CharField('Full Name', max_length=128)
    email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=255)
    text = models.TextField(max_length=1500)

    class Meta:
        verbose_name = 'SocialLink'
        verbose_name_plural = 'SocialLinks'

    def __str__(self):
        return self.full_name
