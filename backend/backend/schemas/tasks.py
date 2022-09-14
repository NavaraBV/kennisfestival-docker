from enum import Enum

from pydantic import BaseModel


class StatusEnum(str, Enum):
    new = "new"
    completed = "completed"


class Task(BaseModel):
    task: str
    assignee: str
    status: StatusEnum


class TaskInDb(Task):
    id: str
