# app/routers/services.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.service import Service
from app.schemas.service import ServiceResponse

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)

@router.get("/", response_model=List[ServiceResponse])
def get_services(db: Session = Depends(get_db)):
    """
    Get a list of all available government services.
    """
    services = db.query(Service).all()
    return services

@router.get("/{service_id}", response_model=ServiceResponse)
def get_service_details(service_id: int, db: Session = Depends(get_db)):
    """
    Get details for a specific service by ID.
    """
    service = db.query(Service).filter(Service.id == service_id).first()
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service