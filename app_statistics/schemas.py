from pydantic import BaseModel


class LocationInfoSchema(BaseModel):
    ip: str
    city: str
    region: str
    country: str


class VisitGetterSchema(BaseModel):
    ip: str
    referrer: str
    platform: str
    user_agent: str
