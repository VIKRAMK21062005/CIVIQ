# app/routers/applications.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.application import Application
from app.models.service import Service
from app.schemas.application import ApplicationOut
from app.routers.auth import get_current_user 
from app.models.user import User

router = APIRouter()

# 1. SUBMIT AN APPLICATION
@router.post("/services/{service_id}/apply", response_model=ApplicationOut)
def submit_application(
    service_id: int, 
    current_user: User = Depends(get_current_user), # <--- Requires Login!
    db: Session = Depends(get_db)
):
    # Check if service exists
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    # Create the application record
    new_app = Application(
        user_id=current_user.id,
        service_id=service_id,
        status="Pending"
    )
    
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    
    return new_app

# 2. VIEW MY HISTORY
@router.get("/applications/me", response_model=List[ApplicationOut])
def get_my_applications(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get a list of all applications submitted by the logged-in user.
    """
    return db.query(Application).filter(Application.user_id == current_user.id).all()