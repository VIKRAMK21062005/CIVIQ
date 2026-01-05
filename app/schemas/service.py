# app/schemas/service.py
from pydantic import BaseModel
from typing import Optional

# Base class (shared properties)
class ServiceBase(BaseModel):
    name: str
    category: str
    description: Optional[str] = None
    fee: float
    fee_currency: str = "USD"
    processing_time: str
    icon_url: Optional[str] = None

# Properties to return to client
class ServiceResponse(ServiceBase):
    id: int

    class Config:
        from_attributes = True