# app/schemas/application.py
from pydantic import BaseModel
from datetime import datetime

class ApplicationOut(BaseModel):
    id: int
    service_id: int
    status: str
    submitted_at: datetime

    class Config:
        from_attributes = True