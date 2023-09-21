from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from django.conf import settings
from fastapi.staticfiles import StaticFiles

from core.language import get_language
from .schemas import FreelanceSchema, WhatToDoSchema, TestimonialSchema, TechnologySchema,\
    HobbySchema, ExperienceSchema, SocialLinkSchema, ProjectThumbSchema, ProjectSchema,\
    EducationSchema
from .services import freelancer_service, what_to_do_service, testimonial_service, technology_service,\
    hobby_service, experience_service, social_link_service, project_service

from core.schema import DjangoUserSchema

info_router = APIRouter()
project_router = APIRouter()


@info_router.get('/freelancer/', response_model=FreelanceSchema, summary='Freelancer Info')
def get_freelancer(lang: str = Depends(get_language)):
    return freelancer_service.get_freelancer()


@info_router.get('/freelancer/avatar.jpg', summary='Freelancer Avatar')
def get_avatar():
    avatar = freelancer_service.get_avatar_path()
    return FileResponse(f'{settings.BASE_DIR}{avatar}')


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


@info_router.get('/education/', response_model=List[EducationSchema], summary='Education')
def education(lang: str = Depends(get_language)):
    return experience_service.education_list()


@info_router.get('/social_links/', response_model=List[SocialLinkSchema], summary='Social Links')
def social_links(lang: str = Depends(get_language)):
    return social_link_service.get_list()


@project_router.get('/projects/', response_model=List[ProjectThumbSchema], summary='Projects List')
def projects(lang: str = Depends(get_language)):
    return project_service.get_projects()


@project_router.get('/project/{slug}/', response_model=ProjectSchema, summary='Project')
def projects(slug: str, lang: str = Depends(get_language)):
    return project_service.get_project(slug)
