from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
import redis.asyncio as redis
import logging

from app.core.config import settings
from app.core.database import get_db
from app.api.v1.router import api_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router
app.include_router(api_router, prefix=settings.API_V1_STR)

# Redis client
redis_client = redis.from_url(settings.redis_dsn, decode_responses=True)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up PawCare AI backend...")
    # Optionally test DB and Redis on startup

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down PawCare AI backend...")
    await redis_client.close()

@app.get("/health", tags=["health"])
async def health_check(db: AsyncSession = Depends(get_db)):
    health_status = {
        "status": "ok",
        "database": "unknown",
        "redis": "unknown"
    }
    
    # Check DB
    try:
        await db.execute(text("SELECT 1"))
        health_status["database"] = "ok"
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        health_status["database"] = "error"
        health_status["status"] = "degraded"
        
    # Check Redis
    try:
        await redis_client.ping()
        health_status["redis"] = "ok"
    except Exception as e:
        logger.error(f"Redis health check failed: {e}")
        health_status["redis"] = "error"
        health_status["status"] = "degraded"
        
    return health_status
