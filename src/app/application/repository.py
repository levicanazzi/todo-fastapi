
from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.tasks import Task

class TaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> Task: ...

    @abstractmethod
    def get_by_id(self, task_id: UUID) -> Task | None: ...

    @abstractmethod
    def get_all(self, status: str | None = None) -> list[Task]: ...

    @abstractmethod
    def update(self, task: Task) -> Task: ...

    @abstractmethod
    def delete(self, task: Task) -> None: ...