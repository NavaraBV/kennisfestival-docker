from typing import List, Any

from fastapi import APIRouter, Depends
from pymongo import MongoClient

from backend.core.config import settings
from backend.schemas.tasks import Task, TaskInDb

router = APIRouter(prefix="/tasks", tags=["Tasks"])


async def get_db() -> Any:
    client = MongoClient(settings.MONGO_CONNECTION_STRING)
    return client.tasks.tasks


@router.get(path="", response_model=List[Task], summary="List tasks")
async def read_tasks(db=Depends(get_db)) -> Any:
    """Read tasks."""
    return [TaskInDb(id=str(task['_id']), **task).dict() for task in db.find({})]


@router.post(path="", response_model=Task, summary="Create task")
async def create_task(task: Task, db=Depends(get_db)) -> Task:
    object_id = db.insert_one(task.dict()).inserted_id
    return TaskInDb(**task.dict(), id=str(object_id))

