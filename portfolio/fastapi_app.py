from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette_context import plugins
from starlette_context.middleware import ContextMiddleware
from starlette.middleware.cors import CORSMiddleware
from django.conf import settings

from .asgi import application
from .api_routers import api_router
from app_statistics.services import create_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_settings()
    yield


middleware = [
    Middleware(
        ContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),
            plugins.CorrelationIdPlugin()
        )
    )
]


fastapp = FastAPI(title='Portfolio', debug=settings.DEBUG, middleware=middleware, lifespan=lifespan)


fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapp.include_router(api_router)


if settings.MOUNT_DJANGO_APP:
    fastapp.mount("/django", application)
    fastapp.mount("/static", StaticFiles(directory="staticfiles"), name="static")
    fastapp.mount("/media", StaticFiles(directory=settings.MEDIA_SRC), name="static")