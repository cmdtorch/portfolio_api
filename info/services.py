from core.services import BaseService
from .models import Freelancer, WhatToDo, Testimonial, Technology, Hobby, Experience, SocialLink


class FreelancerService(BaseService):
    model = Freelancer

    def get_freelancer(self):
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


class ExperienceService(BaseService):
    model = Experience

    def experience_list(self):
        return self.parse_query(self.model.objects.filter(experience_type='EXP').order_by('sort'))

    def education_list(self):
        return self.parse_query(self.model.objects.filter(experience_type='EDU').order_by('sort'))


freelancer_service = FreelancerService()
what_to_do_service = WhatToDoService()
testimonial_service = TestimonialService()
technology_service = TechnologyService()
hobby_service = HobbyService()
social_link_service = SocialLinkService()
experience_service = ExperienceService()
