from django.contrib import admin
from .models import VisitFreeIP, Visit, StatisticSettings


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['ip', 'country', 'visits_count', 'last_visit_date', 'platform']
    date_hierarchy = 'created_at'


class VisitFreeIPInline(admin.StackedInline):
    model = VisitFreeIP


@admin.register(StatisticSettings)
class StatisticSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'telegram_bot_token', 'telegram_notification']
    inlines = [VisitFreeIPInline]