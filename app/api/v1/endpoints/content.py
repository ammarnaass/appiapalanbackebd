from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/{type_key}", response_model=List[schemas.Content])
def read_contents(
    type_key: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve contents by type.
    """
    contents = crud.content.get_multi_by_type(
        db, type_key=type_key, skip=skip, limit=limit
    )
    return contents

@router.post("/", response_model=schemas.Content)
def create_content(
    *,
    db: Session = Depends(deps.get_db),
    content_in: schemas.ContentCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new content.
    """
    # Check if type exists
    type_obj = crud.content_type.get_by_key(db, key=content_in.type_key)
    if not type_obj:
        raise HTTPException(status_code=404, detail="Content Type not found")
        
    content = crud.content.create(db=db, obj_in=content_in, user_id=current_user.id)
    return content

@router.put("/{id}", response_model=schemas.Content)
def update_content(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    content_in: schemas.ContentUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update content.
    """
    content = crud.content.get(db=db, id=id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    content = crud.content.update(db=db, db_obj=content, obj_in=content_in)
    return content

@router.post("/type", response_model=schemas.ContentType)
def create_content_type(
    *,
    db: Session = Depends(deps.get_db),
    type_in: schemas.ContentTypeCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new content type (Superuser only).
    """
    type_obj = crud.content_type.get_by_key(db, key=type_in.key)
    if type_obj:
        raise HTTPException(status_code=400, detail="Content Type already exists")
    content_type = crud.content_type.create(db=db, obj_in=type_in)
    return content_type
