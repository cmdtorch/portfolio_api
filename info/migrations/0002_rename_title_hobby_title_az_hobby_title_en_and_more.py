# Generated by Django 4.2.3 on 2023-08-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hobby',
            old_name='title',
            new_name='title_az',
        ),
        migrations.AddField(
            model_name='hobby',
            name='title_en',
            field=models.CharField(default='qew', max_length=128, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hobby',
            name='title_ru',
            field=models.CharField(default='qwe', max_length=128, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='experience_type',
            field=models.CharField(choices=[('EXP', 'experience'), ('EDU', 'education')], max_length=16, verbose_name='Type'),
        ),
    ]
