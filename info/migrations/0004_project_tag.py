# Generated by Django 4.2.3 on 2023-09-10 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_experience_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.CharField(default='app', max_length=128, verbose_name='Tag'),
            preserve_default=False,
        ),
    ]