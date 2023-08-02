from fastapi import APIRouter, Depends, status

from .schemas import MessageFormSchema
from .models import Message


contact_router = APIRouter()


@contact_router.post('/get_in_touch/', status_code=status.HTTP_204_NO_CONTENT, summary='Get In Touch')
def get_in_touch(message: MessageFormSchema = Depends()):
    Message.objects.create(**message.model_dump())
