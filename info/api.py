from typing import List
from fastapi import APIRouter, Depends

from core.language import get_language
import schemas


info_router = APIRouter()


@info_router.get('/freelancer/', response_model=schemas.FreelanceSchema, summary='Freelancer Info')
def get_freelancer(lang: str = Depends(get_language)):
    ...


@info_router.get('/what_i_do/', response_model=List[schemas.WhatToDoSchema], summary='WhatIDO')
def what_i_do(lang: str = Depends(get_language)):
    ...


@info_router.get('/testimonials/', response_model=List[schemas.TestimonialSchema], summary='Testimonials')
def testimonials(lang: str = Depends(get_language)):
    ...


@info_router.get('/technologies/', response_model=List[schemas.TechnologySchema], summary='Technologies')
def technologies(lang: str = Depends(get_language)):
    ...


@info_router.get('/hobbies/', response_model=List[schemas.HobbySchema], summary='Hobbies')
def hobbies(lang: str = Depends(get_language)):
    ...


@info_router.get('/experiences/', response_model=List[schemas.ExperienceSchema], summary='Experience/Education')
def experiences(lang: str = Depends(get_language)):
    ...


@info_router.get('/social_links/', response_model=List[schemas.SocialLinkSchema], summary='Social Links')
def social_links(lang: str = Depends(get_language)):
    ...
