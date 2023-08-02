from uuid import UUID
from asgiref.sync import sync_to_async
from typing import Type, Optional, TypeVar

from pydantic import BaseModel
from django.db import models

ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)


class BaseService:
    """ `BaseService` базовый класс для сервисов
    """
    model: Type[ModelType]
    create_schema: CreateSchemaType
    update_schema: UpdateSchemaType
    get_schema: GetSchemaType

    def parse_query(self, query, pref=None, extra_fields=None):
        objects_list = []
        for advocate in query:
            objects_list.append(advocate.get_data(pref, extra_fields))
        return objects_list

    def update(self, pk: UUID, schema, **kwargs):
        obj = self.model.objects.get(id=pk)

        for key, value in schema.items():
            setattr(obj, key, value)

        for key, value in kwargs.items():
            setattr(obj, key, value)

        obj.save()

        return obj

    def get(self, **kwargs):
        try:
            obj = self.model.objects.get(**kwargs)
        except self.model.DoesNotExist:
            obj = None
        return obj

    @sync_to_async
    def async_get(self, **kwargs):
        try:
            obj = self.model.objects.get(**kwargs)
        except self.model.DoesNotExist:
            obj = None
        return obj

    def get_list(self, **kwargs):
        obj_list = self.model.objects.filter(**kwargs).all()
        return self.parse_query(obj_list)

    def delete(self, **kwargs):
        try:
            obj = self.model.objects.get(**kwargs)
            obj.delete()
            return True
        except self.model.DoesNotExist:
            return False
