# Generated by Django 4.2.3 on 2023-08-02 12:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('experience_type', models.CharField(choices=[('experience', 'EXP'), ('education', 'EDU')], max_length=16, verbose_name='Type')),
                ('sort', models.IntegerField(default=1, verbose_name='Sort')),
                ('period', models.CharField(max_length=64, verbose_name='Period')),
                ('title_en', models.CharField(max_length=128, verbose_name='[EN]Title')),
                ('title_ru', models.CharField(max_length=128, verbose_name='[RU]Title')),
                ('title_az', models.CharField(max_length=128, verbose_name='[AZ]Title')),
                ('sub_title_en', models.CharField(max_length=128, verbose_name='[EN]Sub title')),
                ('sub_title_ru', models.CharField(max_length=128, verbose_name='[RU]Sub title')),
                ('sub_title_az', models.CharField(max_length=128, verbose_name='[AZ]Sub title')),
                ('text_en', models.TextField(max_length=600, verbose_name='[EN]Text')),
                ('text_ru', models.TextField(max_length=600, verbose_name='[RU]Text')),
                ('text_az', models.TextField(max_length=600, verbose_name='[AZ]Text')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experience',
            },
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('avatar', models.ImageField(upload_to='media', verbose_name='Freelancer Image')),
                ('full_name_en', models.CharField(max_length=128, verbose_name='[EN]Full Name')),
                ('full_name_ru', models.CharField(max_length=128, verbose_name='[RU]Full Name')),
                ('full_name_az', models.CharField(max_length=128, verbose_name='[AZ]Full Name')),
                ('about_en', models.TextField(max_length=1500, verbose_name='[EN]About Text')),
                ('about_ru', models.TextField(max_length=1500, verbose_name='[RU]About Text')),
                ('about_az', models.TextField(max_length=1500, verbose_name='[AZ]About Text')),
                ('profession_en', models.CharField(max_length=155, verbose_name='[EN]Profession')),
                ('profession_ru', models.CharField(max_length=155, verbose_name='[RU]Profession')),
                ('profession_az', models.CharField(max_length=155, verbose_name='[AZ]Profession')),
                ('phone_number', models.CharField(max_length=64, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=128, verbose_name='Address')),
                ('cv_en', models.FileField(upload_to='media', verbose_name='[EN]CV')),
                ('cv_ru', models.FileField(upload_to='media', verbose_name='[RU]CV')),
                ('cv_az', models.FileField(upload_to='media', verbose_name='[AZ]CV')),
            ],
            options={
                'verbose_name': 'Freelancer',
                'verbose_name_plural': 'Freelancers',
            },
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('icon', models.CharField(max_length=64, verbose_name='Icon code')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('value', models.CharField(blank=True, max_length=16, null=True, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Hobby',
                'verbose_name_plural': 'Hobbies',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('preview_image', models.ImageField(upload_to='media', verbose_name='Preview image')),
                ('site_url', models.URLField(blank=True, null=True, verbose_name='Site URL')),
                ('created_date', models.DateField(verbose_name='Created Date')),
                ('description_en', models.TextField(verbose_name='[EN]Description')),
                ('description_ru', models.TextField(verbose_name='[RU]Description')),
                ('description_az', models.TextField(verbose_name='[AZ]Description')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('url', models.URLField(verbose_name='Url')),
            ],
            options={
                'verbose_name': 'SocialLink',
                'verbose_name_plural': 'SocialLinks',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='media', verbose_name='Logo')),
                ('show_on_main', models.BooleanField(default=False, verbose_name='Show on main page')),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('image', models.ImageField(upload_to='media', verbose_name='Image')),
                ('full_name_en', models.CharField(max_length=128, verbose_name='[EN]Full Name')),
                ('full_name_ru', models.CharField(max_length=128, verbose_name='[RU]Full Name')),
                ('full_name_az', models.CharField(max_length=128, verbose_name='[AZ]Full Name')),
                ('about_en', models.TextField(max_length=1500, verbose_name='[EN]Text')),
                ('about_ru', models.TextField(max_length=1500, verbose_name='[RU]Text')),
                ('about_az', models.TextField(max_length=1500, verbose_name='[AZ]Text')),
                ('profession_en', models.CharField(max_length=155, verbose_name='[EN]Profession')),
                ('profession_ru', models.CharField(max_length=155, verbose_name='[RU]Profession')),
                ('profession_az', models.CharField(max_length=155, verbose_name='[AZ]Profession')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='WhatToDo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('icon', models.CharField(max_length=64, verbose_name='Icon code')),
                ('title_en', models.CharField(max_length=128, verbose_name='[EN]Title')),
                ('title_ru', models.CharField(max_length=128, verbose_name='[RU]Title')),
                ('title_az', models.CharField(max_length=128, verbose_name='[AZ]Title')),
                ('text_en', models.TextField(max_length=700, verbose_name='[EN]Text')),
                ('text_ru', models.TextField(max_length=700, verbose_name='[RU]Text')),
                ('text_az', models.TextField(max_length=700, verbose_name='[AZ]Text')),
            ],
            options={
                'verbose_name': 'WhatToDo',
                'verbose_name_plural': 'WhatToDo',
            },
        ),
        migrations.CreateModel(
            name='ProjectGallery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('image', models.ImageField(upload_to='media', verbose_name='Image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='info.project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(related_name='projects', to='info.technology', verbose_name='Technologies'),
        ),
    ]