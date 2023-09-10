import re
import datetime
from typing import List
from pydantic import field_validator

from core.schema import BaseSchema


class FreelanceSchema(BaseSchema):
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


class WhatToDoSchema(BaseSchema):
    icon: str
    title: str
    text: str


class TestimonialSchema(BaseSchema):
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


class TechnologySchema(BaseSchema):
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


class HobbySchema(BaseSchema):
    icon: str
    title: str
    value: str


class ExperienceSchema(BaseSchema):
    period: str
    title: str
    sub_title: str
    text: str
    image: str

    @field_validator('image', mode='before')
    def transform_image(cls, value):
        if not value:
            return None
        if not isinstance(value, str):
            value = value.url
        value = re.sub('.*media/', 'media/', value)
        return value


class EducationSchema(BaseSchema):
    period: str
    title: str
    sub_title: str
    text: str


class SocialLinkSchema(BaseSchema):
    name: str
    url: str


class ProjectThumbSchema(BaseSchema):
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


class ProjectImageSchema(BaseSchema):
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
    created_date: datetime.date
    description: str
    gallery: List[ProjectImageSchema] = []




