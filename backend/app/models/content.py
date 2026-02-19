from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, text, JSON
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid

from app.db.base_class import Base

class ContentType(Base):
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(50), unique=True, index=True, nullable=False)
    schema = Column(JSONB, nullable=False) # JSON Schema for the UI builder

class Content(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type_key = Column(String(50), ForeignKey("contenttype.key"), index=True)
    title = Column(String(255))
    data = Column(JSONB, nullable=False)
    is_published = Column(Boolean(), default=False)
    published_at = Column(DateTime(timezone=True))
    created_by = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    
    # Relationships could be added here if needed, e.g., author
    # author = relationship("User", back_populates="contents")
