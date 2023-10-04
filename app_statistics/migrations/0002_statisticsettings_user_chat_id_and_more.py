# Generated by Django 4.2.3 on 2023-10-04 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_statistics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statisticsettings',
            name='user_chat_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Chat ID for notification'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='last_visit_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 4, 12, 34, 21, 411212, tzinfo=datetime.timezone.utc), verbose_name='List visit date'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='referrer',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Referrer'),
        ),
    ]