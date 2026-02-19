from app.api.v1.endpoints import auth, content, config, plant_disease, ai

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(content.router, prefix="/content", tags=["content"])
api_router.include_router(config.router, prefix="/config", tags=["config"])
api_router.include_router(plant_disease.router, prefix="/agri", tags=["agriculture"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai-llm"])
