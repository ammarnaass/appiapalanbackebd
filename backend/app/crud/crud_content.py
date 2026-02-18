from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.models.content import Content, ContentType
from app.schemas.content import ContentCreate, ContentUpdate, ContentTypeCreate

class CRUDContent:
    def get(self, db: Session, id: Any) -> Optional[Content]:
        return db.query(Content).filter(Content.id == id).first()

    def get_multi_by_type(
        self, db: Session, *, type_key: str, skip: int = 0, limit: int = 100
    ) -> List[Content]:
        return (
            db.query(Content)
            .filter(Content.type_key == type_key)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, db: Session, *, obj_in: ContentCreate, user_id: Any) -> Content:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Content(**obj_in_data, created_by=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Content, obj_in: Union[ContentUpdate, Dict[str, Any]]
    ) -> Content:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: Any) -> Content:
        obj = db.query(Content).get(id)
        db.delete(obj)
        db.commit()
        return obj

class CRUDContentType:
    def get_by_key(self, db: Session, key: str) -> Optional[ContentType]:
        return db.query(ContentType).filter(ContentType.key == key).first()

    def create(self, db: Session, *, obj_in: ContentTypeCreate) -> ContentType:
        db_obj = ContentType(key=obj_in.key, schema=obj_in.schema)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

content = CRUDContent()
content_type = CRUDContentType()
