import re
from typing import List
from pydantic import BaseModel
from pydantic import field_validator


class FreelanceSchema(BaseModel):
    avatar: str
    full_name: str
    about: str
    profession: str
    phone_number: str
    email: str
    address: str
    cv: str

    @field_validator('avatar', mode='before')
    def transform_image(cls, value):
        if not value:
            return None
        if not isinstance(value, str):
            value = value.url
        value = re.sub('.*media/', 'media/', value)
        return value

    @field_validator('cv', mode='before')
    def transform_cv(cls, value):
        if not value:
            return None
        if not isinstance(value, str):
            value = value.url
        value = re.sub('.*media/', 'media/', value)
        return value


class WhatToDoSchema(BaseModel):
    icon: str
    title: str
    text: str


class TestimonialSchema(BaseModel):
    image: str
    full_name: str
    about: str
    profession: str

    @field_validator('image', mode='before')
    def transform_image(cls, value):
        if not value:
            return None
        if not isinstance(value, str):
            value = value.url
        value = re.sub('.*media/', 'media/', value)
        return value


class TechnologySchema(BaseModel):
    name: str
    logo: str

    @field_validator('logo', mode='before')
    def transform_image(cls, value):
        if not value:
            return None
        if not isinstance(value, str):
            value = value.url
        value = re.sub('.*media/', 'media/', value)
        return value


class HobbySchema(BaseModel):
    icon: str
    title: str
    value: str


class ExperienceSchema(BaseModel):
    experience_type: str
    period: str
    title: str
    sub_title: str
    text: str


class SocialLinkSchema(BaseModel):
    name: str
    url: str


class ProjectThumbSchema(BaseModel):
    title: str
    preview_image: str
    technologies: List[TechnologySchema] = []

    @field_validator('preview_image', mode='before')
    def transform_image(cls, value):
        if not value:
            return None
        if not isinstance(value, str):
            value = value.url
        value = re.sub('.*media/', 'media/', value)
        return value


class ProjectImageSchema(BaseModel):
    image: str

    @field_validator('image', mode='before')
    def transform_image(cls, value):
        if not value:
            return None
        if not isinstance(value, str):
            value = value.url
        value = re.sub('.*media/', 'media/', value)
        return value


class ProjectSchema(ProjectThumbSchema):
    site_url: str
    created_date: str
    description: str
    gallery: List[ProjectImageSchema] = []
