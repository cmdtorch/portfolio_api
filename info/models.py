from django.db import models
from django.utils.text import slugify

from core.models import BaseClass, BaseClassLang
from .schemas import ProjectSchema
from .texts import help_text


class Freelancer(BaseClassLang):
    lang_fields = ['full_name', 'about', 'profession', 'cv']

    avatar = models.ImageField('Freelancer Image', upload_to="media")
    full_name_en = models.CharField('[EN]Full Name', max_length=128)
    full_name_ru = models.CharField('[RU]Full Name', max_length=128)
    full_name_az = models.CharField('[AZ]Full Name', max_length=128)
    about_en = models.TextField('[EN]About Text', max_length=1500)
    about_ru = models.TextField('[RU]About Text', max_length=1500)
    about_az = models.TextField('[AZ]About Text', max_length=1500)
    profession_en = models.CharField('[EN]Profession', max_length=155, help_text=help_text['profession'])
    profession_ru = models.CharField('[RU]Profession', max_length=155, help_text=help_text['profession'])
    profession_az = models.CharField('[AZ]Profession', max_length=155, help_text=help_text['profession'])
    phone_number = models.CharField('Phone number', max_length=64)
    email = models.EmailField('Email')
    address = models.CharField('Address', max_length=128)
    cv_en = models.FileField('[EN]CV', upload_to="media")
    cv_ru = models.FileField('[RU]CV', upload_to="media")
    cv_az = models.FileField('[AZ]CV', upload_to="media")

    full_name: str = ''
    about: str = ''
    profession: str = ''
    cv: str = ''

    class Meta:
        verbose_name = 'Freelancer'
        verbose_name_plural = 'Freelancers'

    def __str__(self):
        return self.full_name_en


class WhatToDo(BaseClassLang):
    lang_fields = ['title', 'text']

    icon = models.CharField('Icon code', max_length=255, help_text=help_text['icon'])
    title_en = models.CharField('[EN]Title', max_length=128)
    title_ru = models.CharField('[RU]Title', max_length=128)
    title_az = models.CharField('[AZ]Title', max_length=128)
    text_en = models.TextField('[EN]Text', max_length=700)
    text_ru = models.TextField('[RU]Text', max_length=700)
    text_az = models.TextField('[AZ]Text', max_length=700)

    title: str = ''
    text: str = ''

    class Meta:
        verbose_name = 'WhatToDo'
        verbose_name_plural = 'WhatToDo'

    def __str__(self):
        return self.title_en


class Testimonial(BaseClassLang):
    lang_fields = ['full_name', 'about', 'profession']

    image = models.ImageField('Image', upload_to="media")
    full_name_en = models.CharField('[EN]Full Name', max_length=128)
    full_name_ru = models.CharField('[RU]Full Name', max_length=128)
    full_name_az = models.CharField('[AZ]Full Name', max_length=128)
    about_en = models.TextField('[EN]Text', max_length=1500)
    about_ru = models.TextField('[RU]Text', max_length=1500)
    about_az = models.TextField('[AZ]Text', max_length=1500)
    profession_en = models.CharField('[EN]Profession', max_length=155)
    profession_ru = models.CharField('[RU]Profession', max_length=155)
    profession_az = models.CharField('[AZ]Profession', max_length=155)

    full_name: str = ''
    about: str = ''
    profession: str = ''

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.full_name_en


class Technology(BaseClass):
    name = models.CharField('Name', max_length=64)
    logo = models.ImageField('Logo', upload_to="media")
    show_on_main = models.BooleanField('Show on main page', default=False)

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.name


class Hobby(BaseClassLang):
    lang_fields = ['title']

    icon = models.CharField('Icon code', max_length=255, help_text=help_text['icon'])
    title_en = models.CharField('[EN]Title', max_length=128)
    title_ru = models.CharField('[RU]Title', max_length=128)
    title_az = models.CharField('[AZ]Title', max_length=128)

    title: str = ''

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.title


class Experience(BaseClassLang):
    class TypeOfExperience(models.TextChoices):
        experience = 'EXP', 'experience'
        education = 'EDU', 'education'

    lang_fields = ['title', 'sub_title', 'text']

    experience_type = models.CharField('Type', max_length=16, choices=TypeOfExperience.choices)
    sort = models.IntegerField('Sort', default=1)
    period = models.CharField('Period', max_length=64, help_text=help_text['period'])
    title_en = models.CharField('[EN]Title', max_length=128)
    title_ru = models.CharField('[RU]Title', max_length=128)
    title_az = models.CharField('[AZ]Title', max_length=128)
    sub_title_en = models.CharField('[EN]Sub title', max_length=128)
    sub_title_ru = models.CharField('[RU]Sub title', max_length=128)
    sub_title_az = models.CharField('[AZ]Sub title', max_length=128)
    text_en = models.TextField('[EN]Text', max_length=600)
    text_ru = models.TextField('[RU]Text', max_length=600)
    text_az = models.TextField('[AZ]Text', max_length=600)
    image = models.ImageField('Image', upload_to="media", null=True, blank=True)

    title: str = ''
    sub_title: str = ''
    text: str = ''

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'

    def __str__(self):
        return self.title


class SocialLink(BaseClass):
    name = models.CharField('Name', max_length=64)
    icon = models.CharField('Icon code', max_length=255, help_text=help_text['icon'])
    url = models.URLField('Url')

    class Meta:
        verbose_name = 'SocialLink'
        verbose_name_plural = 'SocialLinks'

    def __str__(self):
        return self.name


class Project(BaseClassLang):
    lang_fields = ['description']

    title = models.CharField('Title', max_length=128)
    slug = models.CharField('Slug', max_length=255, blank=True)
    preview_image = models.ImageField('Preview image', upload_to='media')
    site_url = models.URLField('Site URL', blank=True, null=True)
    created_date = models.DateField('Created Date')
    description_en = models.TextField('[EN]Description')
    description_ru = models.TextField('[RU]Description')
    description_az = models.TextField('[AZ]Description')
    tag = models.CharField('Tag', max_length=128, help_text=help_text['tag'])

    technologies = models.ManyToManyField(Technology, verbose_name='Technologies', related_name='projects')

    description: str = ''

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectGallery(BaseClass):
    image = models.ImageField('Image', upload_to='media')
    project = models.ForeignKey(Project, verbose_name='Project', related_name='gallery', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.image.name


class SEOInfo(BaseClass):
    meta_description = models.TextField('Meta Description')
    meta_keywords = models.TextField('Meta Keywords')

    class Meta:
        verbose_name = 'SEO Info'
        verbose_name_plural = 'SEO Info'

    def __str__(self):
        return 'SEO'
