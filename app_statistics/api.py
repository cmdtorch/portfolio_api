from fastapi import APIRouter, Depends, status, Request
from telegram import Update

from .schemas import VisitGetterSchema
from .services import statistics_service
from .telegram import telegram_bot


statistics_router = APIRouter()


@statistics_router.post('/visit/', status_code=status.HTTP_204_NO_CONTENT, summary='New Visit')
async def new_visit(visit_getter: VisitGetterSchema = Depends()):
    visit = await statistics_service.new_visit(visit_getter)
    if visit:
        await statistics_service.visit_notify(visit)


@statistics_router.post('/webhook/', summary='WebHook')
async def webhook(request: Request):
    raw_data = await request.json()
    try:
        chat_id = raw_data['message']['chat']['id']
        await telegram_bot.send_chat_id(chat_id)
    except KeyError:
        print('Chat in not fund')
    return 'ok'