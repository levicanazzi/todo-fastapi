
from functools import lru_cache

from app.application.repository import TaskRepository
from app.application.task_service import TaskService
from app.infrastructure.memory_repository import MemoryRepository

@lru_cache
def get_repository() -> TaskRepository:
    return MemoryRepository()

def get_task_service() -> TaskService:
    return TaskService(get_repository())