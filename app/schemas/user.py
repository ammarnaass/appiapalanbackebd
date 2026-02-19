from typing import Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID

# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    full_name: Optional[str] = None
    country: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    role: str = "user"
    subscription_tier: str = "free"
    subscription_expiry: Optional[str] = None
    preferred_currency: str = "USD"

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: Optional[str] = None
    google_id: Optional[str] = None

# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDBBase(UserBase):
    id: Optional[UUID] = None

    class Config:
        from_attributes = True

# Additional properties to return via API
class User(UserInDBBase):
    pass

# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: Optional[str] = None
    google_id: Optional[str] = None
