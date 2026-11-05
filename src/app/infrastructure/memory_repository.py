
from copy import copy
from threading import RLock
from uuid import UUID

from app.application.repository import TaskRepository 
from app.domain.tasks import Task

class MemoryRepository(TaskRepository):
    def __init__(self) -> None:
        self._tasks: dict[UUID, Task] = {}
        self._lock = RLock()
        
    def add(self, task: Task) -> Task:
        return self.save(task)

    def get_by_id(self, task_id: UUID) -> Task | None:
        with self._lock:
            task = self._tasks.get(task_id)
            return copy(task) if task else None

    def get_all(self, status: str | None = None) -> list[Task]:
        with self._lock:
            tasks = list(self._tasks.values())
            if status is not None:
                tasks = [task for task in tasks if task.status == status]
            return [copy(task) for task in tasks]

    def update(self, task: Task) -> Task:
        with self._lock:
            if task.id not in self._tasks:
                raise ValueError(f"Task with ID {task.id} not found.")
            self._tasks[task.id] = copy(task)
            return task

    def delete(self, task: Task) -> None:
        with self._lock:
            if task.id not in self._tasks:
                raise ValueError(f"Task with ID {task.id} not found.")
            del self._tasks[task.id]

    def save(self, task: Task) -> Task:
        with self._lock:
            self._tasks[task.id] = copy(task)
            return task