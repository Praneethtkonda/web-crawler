from inspect import cleandoc
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from routes import tasks

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Web Crawler service"

settings = Settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=settings.API_V1_STR + "/docs/openapi.json",
    docs_url=settings.API_V1_STR + "/docs",
    redoc_url=settings.API_V1_STR + "/redoc",
    description=cleandoc("""
        This is the API for the Web Crawler service.
    """)
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
api_router = APIRouter()

api_router.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])

app.include_router(api_router)
