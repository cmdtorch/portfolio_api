import uuid
from typing import List, Union
from django.db.models.fields.reverse_related import ManyToOneRel, ManyToManyRel
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db import models
from starlette_context.errors import ContextDoesNotExistError
from starlette_context import context

from .utils import pref_iter


class BaseClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, blank=True)

    def get_data(self, pref: List[Union[str, dict]] = None, extra_fields: List[str] = None):

        if pref is not None:
            data = pref_iter(self, pref)
        else:
            data = {}

        for field in self.__class__._meta.get_fields():
            if not isinstance(field, ManyToOneRel) and\
                    not isinstance(field, ManyToManyRel) and\
                    not isinstance(field, ManyToManyField) and\
                    not isinstance(field, GenericRelation) and\
                    not isinstance(field, GenericForeignKey) and\
                    not isinstance(field, GenericForeignKey) and\
                    not isinstance(field, ForeignKey):
                data[field.name] = getattr(self, field.name)

        # Extra Fields
        if extra_fields is not None:
            for field in extra_fields:
                data[field] = getattr(self, field)

        return data

    class Meta:
        abstract = True


class BaseClassLang(BaseClass):
    lang_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.lang_fields:
            try:
                self.__init_lang()
            except ContextDoesNotExistError:
                pass

    def __init_lang(self):
        for field in self.lang_fields:
            if hasattr(self, field) and getattr(self, field) is not None:
                try:
                    setattr(self, field, getattr(self, f"{field}_{context['lang']}"))
                except KeyError:
                    setattr(self, field, getattr(self, f"{field}_en"))

    def get_data(self, *args, **kwargs):
        data = super().get_data(*args, **kwargs)

        # Lang Extra Fields
        if self.lang_fields:
            for field in self.lang_fields:
                data[field] = getattr(self, field)

        return data

    class Meta:
        abstract = True
