from typing import List, Optional
from pydantic import BaseModel, UUID4
from datetime import datetime

# Plant Schemas
class PlantBase(BaseModel):
    name_ar: str
    name_en: str
    scientific_name: Optional[str] = None

class PlantCreate(PlantBase):
    pass

class PlantUpdate(PlantBase):
    name_ar: Optional[str] = None
    name_en: Optional[str] = None

class Plant(PlantBase):
    id: int

    class Config:
        from_attributes = True

# Disease Schemas
class DiseaseBase(BaseModel):
    plant_id: int
    name_ar: str
    name_en: str
    description_ar: Optional[str] = None
    description_en: Optional[str] = None
    symptoms_ar: Optional[str] = None
    symptoms_en: Optional[str] = None
    treatment_ar: Optional[str] = None
    treatment_en: Optional[str] = None
    is_common: Optional[bool] = True

class DiseaseCreate(DiseaseBase):
    pass

class DiseaseUpdate(DiseaseBase):
    plant_id: Optional[int] = None
    name_ar: Optional[str] = None
    name_en: Optional[str] = None

class Disease(DiseaseBase):
    id: int

    class Config:
        from_attributes = True

# Prediction Log Schemas
class PredictionLogBase(BaseModel):
    image_url: str
    predicted_class: str
    confidence: float
    user_feedback: Optional[bool] = None

class PredictionLogCreate(PredictionLogBase):
    user_id: Optional[UUID4] = None

class PredictionLog(PredictionLogBase):
    id: UUID4
    user_id: Optional[UUID4]
    created_at: datetime
    disease: Optional[Disease] = None

    class Config:
        from_attributes = True
