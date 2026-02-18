from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Float, DateTime, UUID, text
from sqlalchemy.orm import relationship
import uuid
from app.db.base_class import Base

class Plant(Base):
    __tablename__ = "plants"
    id = Column(Integer, primary_key=True, index=True)
    name_ar = Column(String(100), nullable=False)
    name_en = Column(String(100), nullable=False)
    scientific_name = Column(String(100))
    
    diseases = relationship("Disease", back_populates="plant")

class Disease(Base):
    __tablename__ = "diseases"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"))
    name_ar = Column(String(255), nullable=False)
    name_en = Column(String(255), nullable=False)
    description_ar = Column(Text)
    description_en = Column(Text)
    symptoms_ar = Column(Text)
    symptoms_en = Column(Text)
    treatment_ar = Column(Text)
    treatment_en = Column(Text)
    is_common = Column(Boolean, default=True)

    plant = relationship("Plant", back_populates="diseases")

class PredictionLog(Base):
    __tablename__ = "prediction_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)
    image_url = Column(Text, nullable=False)
    predicted_class = Column(String(100), nullable=False)
    confidence = Column(Float, nullable=False)
    user_feedback = Column(Boolean, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=text("now()"))

    user = relationship("User")
