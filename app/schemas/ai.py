from typing import Optional
from pydantic import BaseModel, UUID4

# Shared properties
class AIProviderBase(BaseModel):
    name: Optional[str] = None
    provider_type: Optional[str] = None
    model_id: Optional[str] = None
    base_url: Optional[str] = None
    is_active: Optional[bool] = True

# Properties to receive via API on creation
class AIProviderCreate(AIProviderBase):
    name: str
    provider_type: str
    api_key: str
    model_id: str

# Properties to receive via API on update
class AIProviderUpdate(AIProviderBase):
    api_key: Optional[str] = None

# Additional properties to return via API
class AIProvider(AIProviderBase):
    id: UUID4

    class Config:
        from_attributes = True
