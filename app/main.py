from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api.v1.endpoints import router as api_v1_router
from app.core.config import settings
from app.core.logging import setup_logging, logger
from app.services.tts_service import tts_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("Uygulama başlıyor...", env=settings.ENV, log_level=settings.LOG_LEVEL)
    tts_engine.load_model()
    logger.info("Uygulama hazır ve istekleri kabul ediyor.")
    yield
    logger.info("Uygulama kapanıyor.")

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0", lifespan=lifespan)

app.include_router(api_v1_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["Health"])
def health_check():
    is_ready = tts_engine.is_ready()
    return {
        "status": "ok" if is_ready else "degraded",
        "details": {"tts_engine_loaded": is_ready}
    }