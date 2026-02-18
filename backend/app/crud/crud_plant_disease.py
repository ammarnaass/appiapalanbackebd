from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.plant_disease import Plant, Disease, PredictionLog
from app.schemas.plant_disease import PlantCreate, PlantUpdate, DiseaseCreate, DiseaseUpdate, PredictionLogCreate

class CRUDPlant(CRUDBase[Plant, PlantCreate, PlantUpdate]):
    def get_by_name(self, db: Session, *, name_en: str) -> Optional[Plant]:
        return db.query(Plant).filter(Plant.name_en == name_en).first()

class CRUDDisease(CRUDBase[Disease, DiseaseCreate, DiseaseUpdate]):
    def get_by_plant(self, db: Session, *, plant_id: int) -> List[Disease]:
        return db.query(Disease).filter(Disease.plant_id == plant_id).all()

    def get_by_name(self, db: Session, *, name_en: str) -> Optional[Disease]:
        return db.query(Disease).filter(Disease.name_en == name_en).first()

class CRUDPredictionLog(CRUDBase[PredictionLog, PredictionLogCreate, None]):
    def get_by_user(self, db: Session, *, user_id: str) -> List[PredictionLog]:
        return db.query(PredictionLog).filter(PredictionLog.user_id == user_id).all()

plant = CRUDPlant(Plant)
disease = CRUDDisease(Disease)
prediction_log = CRUDPredictionLog(PredictionLog)
