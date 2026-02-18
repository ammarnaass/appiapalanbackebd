from sqlalchemy import Boolean, Column, Integer, String, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base_class import Base

class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, index=True)
    role = Column(String, default="user") # 'super_admin', 'editor', 'user'
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime(timezone=True), server_default=text("now()"))
