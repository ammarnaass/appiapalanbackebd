from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, UUID4, Field

# --- Content Type Schemas ---
class ContentTypeBase(BaseModel):
    key: str
    data_schema: Dict[str, Any] = Field(..., alias="schema") # JSON Schema

class ContentTypeCreate(ContentTypeBase):
    pass

class ContentTypeUpdate(ContentTypeBase):
    pass

class ContentType(ContentTypeBase):
    id: int

    class Config:
        from_attributes = True

# --- Content Schemas ---
class ContentBase(BaseModel):
    title: Optional[str] = None
    data: Dict[str, Any]
    is_published: Optional[bool] = False

class ContentCreate(ContentBase):
    type_key: str

class ContentUpdate(ContentBase):
    pass

class Content(ContentBase):
    id: UUID4
    type_key: str
    published_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    created_by: Optional[UUID4] = None

    class Config:
        from_attributes = True
