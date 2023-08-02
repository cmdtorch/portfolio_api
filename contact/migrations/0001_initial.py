# Generated by Django 4.2.3 on 2023-08-02 12:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('full_name', models.CharField(max_length=128, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('text', models.TextField(max_length=1500)),
            ],
            options={
                'verbose_name': 'SocialLink',
                'verbose_name_plural': 'SocialLinks',
            },
        ),
    ]