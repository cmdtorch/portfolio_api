from django.contrib import admin

from .models import Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['site_title']
    date_hierarchy = 'created_at'
