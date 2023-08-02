from pydantic import BaseModel


class MessageFormSchema(BaseModel):
    full_name: str
    email: str
    subject: str
    text: str
