from django.conf import settings
from django import forms
from django.utils import timezone
from django.db import models

from core.models import BaseClass
from .telegram import telegram_bot


class Visit(BaseClass):
    ip = models.GenericIPAddressField('IP', unique=True)
    city = models.CharField('City', max_length=255)
    region = models.CharField('Region', max_length=255)
    country = models.CharField('Country', max_length=255)
    visits_count = models.PositiveIntegerField('Visit count', default=1)
    last_visit_date = models.DateTimeField('List visit date')
    referrer = models.URLField('Referrer', max_length=255, null=True, blank=True)
    platform = models.CharField('Platform', max_length=255)
    user_agent = models.CharField('User Agent', max_length=255)

    class Meta:
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'

    def increase_visit(self, increase_value: int):
        self.visits_count += increase_value
        self.last_visit_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.ip)


class StatisticSettings(BaseClass):
    site_name = models.CharField('Site name', max_length=255)
    telegram_notification = models.BooleanField('Telegram visit notification', default=False)
    telegram_bot_token = models.CharField('Telegram bot token', max_length=255, blank=True, null=True)
    user_chat_id = models.CharField('Chat ID for notification', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def save(self, *args, **kwargs):
        statistic_settings = StatisticSettings.objects.first()
        if self._state.adding and statistic_settings:
            raise forms.ValidationError('Settings is already exist')

        if statistic_settings.telegram_bot_token:
            telegram_bot.update_bot(statistic_settings.telegram_bot_token, settings.TELEGRAM_WEBHOOK_URL)
        super(StatisticSettings, self).save(*args, **kwargs)

    def __str__(self):
        return 'Settings'


class VisitFreeIP(BaseClass):
    name = models.CharField('Name', max_length=255)
    ip = models.GenericIPAddressField('IP', unique=True, help_text='IP will not be processed as a visit')

    settings = models.ForeignKey(StatisticSettings, on_delete=models.CASCADE, related_name='visit_free')

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.ip