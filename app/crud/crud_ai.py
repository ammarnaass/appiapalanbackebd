from typing import List, Optional, Any
from sqlalchemy.orm import Session
from pydantic import UUID4

from app.models.ai import AIProvider
from app.schemas.ai import AIProviderCreate, AIProviderUpdate
from app.core.security import get_password_hash

class CRUDAIProvider:
    def get(self, db: Session, id: UUID4) -> Optional[AIProvider]:
        return db.query(AIProvider).filter(AIProvider.id == id).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[AIProvider]:
        return db.query(AIProvider).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: AIProviderCreate) -> AIProvider:
        db_obj = AIProvider(
            name=obj_in.name,
            provider_type=obj_in.provider_type,
            api_key=obj_in.api_key,
            model_id=obj_in.model_id,
            base_url=obj_in.base_url,
            is_active=obj_in.is_active,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: AIProvider, obj_in: AIProviderUpdate
    ) -> AIProvider:
        obj_data = db_obj.__dict__
        update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: UUID4) -> AIProvider:
        obj = db.query(AIProvider).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_active(self, db: Session) -> Optional[AIProvider]:
        return db.query(AIProvider).filter(AIProvider.is_active == True).first()

ai_provider = CRUDAIProvider()
