# app/models/user.py
from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True, nullable=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    # System Fields (Required for Auth to work)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    # Your Custom Features (Kept safe!)
    is_verified = Column(Boolean, default=False)
    profile_strength = Column(Integer, default=0)
    emergency_contact_name = Column(String, nullable=True)
    emergency_contact_phone = Column(String, nullable=True)