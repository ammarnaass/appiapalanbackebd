from typing import List, Union, Optional, Any
from pydantic import AnyHttpUrl, PostgresDsn, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Mobile CMS API"
    API_V1_STR: str = "/api/v1"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        return v

    # Database
    POSTGRES_SERVER: Optional[str] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_DB: Optional[str] = None
    POSTGRES_URL: Optional[str] = None
    DATABASE_URL: Optional[str] = None
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @model_validator(mode="after")
    def assemble_db_connection(self) -> "Settings":
        if self.SQLALCHEMY_DATABASE_URI:
            self.SQLALCHEMY_DATABASE_URI = self._fix_postgres_uri(self.SQLALCHEMY_DATABASE_URI)
            return self

        # Fallback names
        for url_field in [self.POSTGRES_URL, self.DATABASE_URL]:
            if url_field:
                self.SQLALCHEMY_DATABASE_URI = self._fix_postgres_uri(url_field)
                return self
        
        # Assemble from components
        if all([self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_SERVER, self.POSTGRES_DB]):
            self.SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
            return self
            
        return self

    def _fix_postgres_uri(self, uri: str) -> str:
        if uri.startswith("postgres://"):
            return uri.replace("postgres://", "postgresql+psycopg://", 1)
        if uri.startswith("postgresql://") and "+psycopg" not in uri:
            return uri.replace("postgresql://", "postgresql+psycopg://", 1)
        return uri

    # Security
    SECRET_KEY: Optional[str] = "development_secret_key_change_me_in_production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # AI Service
    AI_SERVICE_URL: str = "http://localhost:8001/v1/predict"
    
    model_config = SettingsConfigDict(
        case_sensitive=True, 
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
