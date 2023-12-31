# Generated by Django 4.2.3 on 2023-09-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_seoinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='android_url',
            field=models.URLField(blank=True, null=True, verbose_name='Play Market URL'),
        ),
        migrations.AddField(
            model_name='project',
            name='apple_url',
            field=models.URLField(blank=True, null=True, verbose_name='Apple Store URL'),
        ),
        migrations.AddField(
            model_name='project',
            name='sort',
            field=models.IntegerField(default=1, verbose_name='Sort'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Logo'),
        ),
    ]
