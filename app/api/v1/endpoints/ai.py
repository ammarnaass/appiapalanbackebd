from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from pydantic import UUID4

from app import crud, schemas
from app.api import deps
from app.core import llm

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
    providers = crud.ai_provider.get_multi(db, skip=skip, limit=limit)
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
    provider = crud.ai_provider.create(db, obj_in=obj_in)
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
    provider = crud.ai_provider.get(db, id=id)
    if not provider:
        raise HTTPException(status_code=404, detail="AI provider not found")
    provider = crud.ai_provider.update(db, db_obj=provider, obj_in=obj_in)
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
    provider = crud.ai_provider.get(db, id=id)
    if not provider:
        raise HTTPException(status_code=404, detail="AI provider not found")
    provider = crud.ai_provider.remove(db, id=id)
    return provider

@router.post("/analyze-image")
async def analyze_plant_image(
    *,
    db: Session = Depends(deps.get_db),
    file: UploadFile = File(...),
    prompt: Optional[str] = "قم بتحليل هذه الصورة لنبات مصاب، اشرح نوع المرض، الأعراض الظاهرة، وقدم نصائح دقيقة للعلاج باللغة العربية.",
    current_user: Any = Depends(deps.get_current_active_user),
) -> Any:
    """
    Analyze plant image using the currently active LLM provider.
    This provides a more detailed and natural language analysis than the basic classifier.
    """
    # 1. Get Active Provider
    provider = crud.ai_provider.get_active(db)
    if not provider:
        raise HTTPException(
            status_code=404, 
            detail="No active AI provider configured. Please add one in settings."
        )

    # 2. Read Image Data
    image_data = await file.read()

    # 3. Call LLM Vision Utility
    try:
        result = await llm.analyze_image_with_llm(
            provider=provider,
            image_data=image_data,
            prompt=prompt
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Analysis Error: {str(e)}")
