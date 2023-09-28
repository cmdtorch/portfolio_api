from django.contrib import admin

from .models import Freelancer, WhatToDo, Testimonial, Technology, Hobby, Experience, SocialLink, \
    Project, ProjectGallery, SEOInfo


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ['full_name_en', 'profession_en', 'email']
    date_hierarchy = 'created_at'


@admin.register(WhatToDo)
class WhatToDoAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'icon']
    date_hierarchy = 'created_at'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['full_name_en', 'profession_en']
    date_hierarchy = 'created_at'


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'show_on_main']
    date_hierarchy = 'created_at'


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon']
    date_hierarchy = 'created_at'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'experience_type', 'period', 'sort']
    date_hierarchy = 'created_at'


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    date_hierarchy = 'created_at'


class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_date', 'sort', 'tag']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'preview_image', 'created_date', 'sort')
        }),
        ('Content', {
            'classes': ('collapse', 'open'),
            'fields': ('description_en', 'description_ru', 'description_az', 'tag')
        }),
        ('Links', {
            'classes': ('collapse', 'open'),
            'fields': ('site_url', 'android_url', 'apple_url')
        }),
    )
    inlines = [ProjectGalleryInline]
    date_hierarchy = 'created_at'


@admin.register(SEOInfo)
class SEOInfoAdmin(admin.ModelAdmin):
    list_display = ['meta_description', 'updated_at']
    date_hierarchy = 'created_at'
