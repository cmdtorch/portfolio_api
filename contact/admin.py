from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'created_at']
    date_hierarchy = 'created_at'
