from fastapi import APIRouter, Depends, status, Request
from telegram import Update

from .schemas import VisitGetterSchema
from .services import statistics_service
from .telegram import app as telegram_app


statistics_router = APIRouter()


@statistics_router.post('/visit/', status_code=status.HTTP_204_NO_CONTENT, summary='New Visit')
def new_visit(visit_getter: VisitGetterSchema = Depends()):
    statistics_service.new_visit(visit_getter)


@statistics_router.post('/webhook/', status_code=status.HTTP_204_NO_CONTENT, summary='WebHook')
def webhook(request: Request):
    await telegram_app.update_queue.put(
        Update.de_json(data=await request.json(), bot=telegram_app.bot)
    )
    return 'ok'