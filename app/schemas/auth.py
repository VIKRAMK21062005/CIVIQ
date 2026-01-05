# app/schemas/auth.py
from pydantic import BaseModel, EmailStr

# What we need to Register
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

# What we return after successful login
class Token(BaseModel):
    access_token: str
    token_type: str

# What we return when asking for "Profile"
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_verified: bool
    profile_strength: int

    class Config:
        from_attributes = True