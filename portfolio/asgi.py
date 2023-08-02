"""
ASGI config for portfolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.conf import settings
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_asgi_application()

# FAST-API
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette_context import plugins
from starlette_context.middleware import ContextMiddleware
from starlette.middleware.cors import CORSMiddleware
#import sentry_sdk

from info.api import info_router
from contact.api import contact_router

# sentry_sdk.init(
#     dsn="https://20c96de741bc463eabb33d542c5cdef4@o1135467.ingest.sentry.io/4504405296545792",
#     traces_sample_rate=1.0,
# )


middleware = [
    Middleware(
        ContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),
            plugins.CorrelationIdPlugin()
        )
    )
]


fastapp = FastAPI(title='Portfolio', debug=settings.DEBUG, middleware=middleware)


fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapp.include_router(info_router, prefix='/api')
fastapp.include_router(contact_router, prefix='/api')


if settings.MOUNT_DJANGO_APP:
    fastapp.mount("/django", application)
    fastapp.mount("/static", StaticFiles(directory="staticfiles"), name="static")
    fastapp.mount("/media", StaticFiles(directory=settings.MEDIA_SRC), name="static")