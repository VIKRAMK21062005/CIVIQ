# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

# 1. Base Schema (Shared fields)
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

# 2. Schema for Registering (Input)
class UserCreate(UserBase):
    password: str

# 3. Schema for Returning Data (Output)
# This is the class your error was looking for!
class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True