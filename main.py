from fastapi import FastAPI

from app import api
from core.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(api.router, prefix="/api/fraud", tags=["fraud"])
