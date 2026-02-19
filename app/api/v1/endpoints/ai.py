from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import UUID4

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.ai.AIProvider])
def read_ai_providers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: Any = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve AI providers. (Superuser only)
    """
    providers = crud.crud_ai.ai_provider.get_multi(db, skip=skip, limit=limit)
    return providers

@router.post("/", response_model=schemas.ai.AIProvider)
def create_ai_provider(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.ai.AIProviderCreate,
    current_user: Any = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new AI provider. (Superuser only)
    """
    provider = crud.crud_ai.ai_provider.create(db, obj_in=obj_in)
    return provider

@router.put("/{id}", response_model=schemas.ai.AIProvider)
def update_ai_provider(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    obj_in: schemas.ai.AIProviderUpdate,
    current_user: Any = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an AI provider. (Superuser only)
    """
    provider = crud.crud_ai.ai_provider.get(db, id=id)
    if not provider:
        raise HTTPException(status_code=404, detail="AI provider not found")
    provider = crud.crud_ai.ai_provider.update(db, db_obj=provider, obj_in=obj_in)
    return provider

@router.delete("/{id}", response_model=schemas.ai.AIProvider)
def delete_ai_provider(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    current_user: Any = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an AI provider. (Superuser only)
    """
    provider = crud.crud_ai.ai_provider.get(db, id=id)
    if not provider:
        raise HTTPException(status_code=404, detail="AI provider not found")
    provider = crud.crud_ai.ai_provider.remove(db, id=id)
    return provider
