from fastapi import APIRouter

from info.api import info_router, project_router
from contact.api import contact_router
from app_statistics.api import statistics_router


api_router = APIRouter(prefix='/api')


api_router.include_router(info_router, tags=['info'])
api_router.include_router(project_router, tags=['project'])
api_router.include_router(contact_router, tags=['contacts'])
api_router.include_router(statistics_router, tags=['statistics'])

