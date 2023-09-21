from fastapi import HTTPException
from django.conf import settings

from core.services import BaseService
from .models import Freelancer, WhatToDo, Testimonial, Technology, Hobby, Experience, SocialLink, Project,\
    ProjectGallery, SEOInfo


class FreelancerService(BaseService):
    model = Freelancer

    def get_freelancer(self):
        freelancer = self.model.objects.first()
        if not freelancer:
            freelancer = self.create_default_freelances()
        return freelancer

    def get_avatar_path(self):
        freelancer = self.get_freelancer()
        return freelancer.avatar.path

    def create_default_freelances(self):
        self.model.objects.create(
            avatar=settings.DEFAULT_USER_AVATAR,
            full_name_en='Example User',
            full_name_ru='Example User',
            full_name_az='Example User',
            about_en='User information',
            about_ru='User information',
            about_az='User information',
            profession_en='User profession',
            profession_ru='User profession',
            profession_az='User profession',
            phone_number='+123456789',
            email='user@example.com',
            address='Test address',
            cv_en=settings.DEFAULT_USER_AVATAR,
            cv_ru=settings.DEFAULT_USER_AVATAR,
            cv_az=settings.DEFAULT_USER_AVATAR
        )
        return self.model.objects.first()


class WhatToDoService(BaseService):
    model = WhatToDo


class TestimonialService(BaseService):
    model = Testimonial


class TechnologyService(BaseService):
    model = Technology


class HobbyService(BaseService):
    model = Hobby


class SocialLinkService(BaseService):
    model = SocialLink


class ProjectService(BaseService):
    model = Project

    def get_projects(self):
        return self.model.objects.prefetch_related('gallery', 'technologies').all()

    def get_project(self, slug: str):
        try:
            return self.model.objects.prefetch_related('gallery', 'technologies').get(slug=slug)
        except self.model.DoesNotExist:
            raise HTTPException(status_code=404, detail='Project not fund')

    def get_image(self):
        image = ProjectGallery.objects.select_related('project')\
            .prefetch_related('project__technologies').first()
        return image


class ExperienceService(BaseService):
    model = Experience

    def experience_list(self):
        return self.model.objects.filter(experience_type='EXP').order_by('sort')

    def education_list(self):
        return self.model.objects.filter(experience_type='EDU').order_by('sort')


class SEOInfoService(BaseService):
    model = SEOInfo

    def get_info(self):
        seo_info = self.model.objects.first()
        if not seo_info:
            seo_info = self.generate_default_seo()
        return seo_info

    def generate_default_seo(self):
        self.model.objects.create(
            meta_description='Example',
            meta_keywords='Example',
        )
        return self.model.objects.first()


freelancer_service = FreelancerService()
what_to_do_service = WhatToDoService()
testimonial_service = TestimonialService()
technology_service = TechnologyService()
hobby_service = HobbyService()
project_service = ProjectService()
social_link_service = SocialLinkService()
experience_service = ExperienceService()
seo_info_service = SEOInfoService()
