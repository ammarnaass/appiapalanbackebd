from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
import uuid

router = APIRouter()

@router.get("/plants", response_model=List[schemas.plant_disease.Plant])
def read_plants(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve plants.
    """
    plants = crud.plant.get_multi(db, skip=skip, limit=limit)
    return plants

@router.get("/diseases", response_model=List[schemas.plant_disease.Disease])
def read_diseases(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    plant_id: int = None
) -> Any:
    """
    Retrieve diseases.
    """
    if plant_id:
        return crud.disease.get_by_plant(db, plant_id=plant_id)
    return crud.disease.get_multi(db, skip=skip, limit=limit)

@router.post("/predict", response_model=schemas.plant_disease.PredictionLog)
async def predict_disease(
    *,
    db: Session = Depends(deps.get_db),
    file: UploadFile = File(...),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Predict plant disease from image.
    Includes scan limit check for monetization.
    """
    # 0. Monetization Check (Demo)
    # In a real app, query user subscription status and scan count for the day
    user_scans_today = 3 # Mocked count
    is_premium = False   # Mocked status
    
    if not is_premium and user_scans_today >= 3:
        raise HTTPException(
            status_code=402, 
            detail="Daily free limit reached. Upgrade to Premium for unlimited scans."
        )

    # 1. Mock Image Upload (In real app, upload to S3/Cloud Storage)
    image_url = f"https://storage.example.com/uploads/{uuid.uuid4()}.jpg"
    
    # 2. AI Inference call to Microservice
    AI_SERVICE_URL = settings.AI_SERVICE_URL
    
    try:
        import httpx
        async with httpx.AsyncClient() as client:
            # We send the file directly to the AI service
            files = {"file": (file.filename, await file.read(), file.content_type)}
            response = await client.post(AI_SERVICE_URL, files=files)
            response.raise_for_status()
            ai_result = response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Service Error: {str(e)}")

    # 3. Create Prediction Log
    prediction_in = schemas.plant_disease.PredictionLogCreate(
        image_url=image_url,
        predicted_class=ai_result["prediction"],
        confidence=ai_result["confidence"],
        user_id=current_user.id
    )
    
    log = crud.prediction_log.create(db, obj_in=prediction_in)
    
    # 4. Attach Disease info if exists
    disease = crud.disease.get_by_name(db, name_en=log.predicted_class)
    if disease:
        log.disease = disease
        
    return log
