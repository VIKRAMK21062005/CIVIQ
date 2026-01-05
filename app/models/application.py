# app/models/application.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    
    # Who applied?
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # What for?
    service_id = Column(Integer, ForeignKey("services.id"))
    
    # Status (Pending, Approved, Rejected)
    status = Column(String, default="Pending")
    
    # When?
    submitted_at = Column(DateTime, default=datetime.utcnow)

    # Relationships (Allows us to say application.user.email)
    user = relationship("User")
    service = relationship("Service")