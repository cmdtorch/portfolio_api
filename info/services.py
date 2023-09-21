from core.services import BaseService
from .models import Freelancer, WhatToDo, Testimonial, Technology, Hobby, Experience, SocialLink, Project, ProjectGallery

from .schemas import ProjectSchema, ProjectImageSchema


class FreelancerService(BaseService):
    model = Freelancer

    def get_freelancer(self):
        return self.model.objects.first()

    def get_avatar_path(self):
        return self.model.objects.first().avatar.url



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
        return self.model.objects.prefetch_related('gallery', 'technologies').get(slug=slug)

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


freelancer_service = FreelancerService()
what_to_do_service = WhatToDoService()
testimonial_service = TestimonialService()
technology_service = TechnologyService()
hobby_service = HobbyService()
project_service = ProjectService()
social_link_service = SocialLinkService()
experience_service = ExperienceService()
