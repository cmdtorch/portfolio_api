from typing import List
from fastapi import APIRouter, Depends

from core.language import get_language
from .schemas import FreelanceSchema, WhatToDoSchema, TestimonialSchema, TechnologySchema,\
    HobbySchema, ExperienceSchema, SocialLinkSchema
from .services import freelancer_service, what_to_do_service, testimonial_service, technology_service,\
    hobby_service, experience_service, social_link_service


info_router = APIRouter()


@info_router.get('/freelancer/', response_model=FreelanceSchema, summary='Freelancer Info')
def get_freelancer(lang: str = Depends(get_language)):
    return freelancer_service.get_freelancer().get_data()


@info_router.get('/what_i_do/', response_model=List[WhatToDoSchema], summary='What I Do')
def what_i_do(lang: str = Depends(get_language)):
    return what_to_do_service.get_list()


@info_router.get('/testimonials/', response_model=List[TestimonialSchema], summary='Testimonials')
def testimonials(lang: str = Depends(get_language)):
    return testimonial_service.get_list()


@info_router.get('/technologies/', response_model=List[TechnologySchema], summary='Technologies')
def technologies(lang: str = Depends(get_language)):
    return technology_service.get_list(show_on_main=True)


@info_router.get('/hobbies/', response_model=List[HobbySchema], summary='Hobbies')
def hobbies(lang: str = Depends(get_language)):
    return hobby_service.get_list()


@info_router.get('/experiences/', response_model=List[ExperienceSchema], summary='Experience')
def experiences(lang: str = Depends(get_language)):
    return experience_service.experience_list()


@info_router.get('/education/', response_model=List[ExperienceSchema], summary='Education')
def education(lang: str = Depends(get_language)):
    return experience_service.education_list()


@info_router.get('/social_links/', response_model=List[SocialLinkSchema], summary='Social Links')
def social_links(lang: str = Depends(get_language)):
    return social_link_service.get_list()
