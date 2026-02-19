from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base_class import Base

class AIProvider(Base):
    """
    Model for managing LLM providers and AI models.
    """
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)  # e.g., "OpenAI", "Anthropic", "Gemini"
    provider_type = Column(String, index=True, nullable=False)  # e.g., "openai", "anthropic", "google"
    api_key = Column(String, nullable=False)
    model_id = Column(String, nullable=False)  # e.g., "gpt-4", "claude-3-opus", "gemini-pro"
    base_url = Column(String, nullable=True)  # For custom endpoints or local LLMs
    is_active = Column(Boolean(), default=True)
