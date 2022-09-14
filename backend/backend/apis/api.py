from fastapi import APIRouter

from backend.apis.endpoints import tasks

api_router = APIRouter()
api_router.include_router(tasks.router)
