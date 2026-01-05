# app/models/service.py
from sqlalchemy import Column, Integer, String, Float, Text
from app.core.database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)       # e.g., "Passport Renewal"
    category = Column(String, index=True)   # e.g., "Travel"
    description = Column(Text)              # Overview text from PDF
    
    # Fee logic [cite: 882, 1350]
    fee = Column(Float)                     # e.g., 130.00
    fee_currency = Column(String, default="USD")
    
    # Processing Time [cite: 881]
    processing_time = Column(String)        # e.g., "6-8 Weeks"
    
    # Icon/Image URL
    icon_url = Column(String, nullable=True)