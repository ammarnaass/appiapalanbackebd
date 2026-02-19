from sqlalchemy import Boolean, Column, Integer, String, DateTime, text, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum

from app.db.base_class import Base

class UserRole(str, enum.Enum):
    SUPER_ADMIN = "super_admin"
    EDITOR = "editor"
    USER = "user"

class SubscriptionTier(str, enum.Enum):
    FREE = "free"
    PREMIUM = "premium"

class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=True) # Allow null if phone-only
    phone_number = Column(String, unique=True, index=True, nullable=True)
    google_id = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=True) # Allow null for social/phone auth
    full_name = Column(String, index=True)
    country = Column(String, index=True)
    role = Column(String, default=UserRole.USER.value)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    
    # Subscriptions
    subscription_tier = Column(String, default=SubscriptionTier.FREE.value)
    subscription_expiry = Column(DateTime, nullable=True)
    preferred_currency = Column(String, default="USD")
