from uuid import UUID
from app.domain.tasks import Task, TaskStatus
from app.application.repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    def create_task(self, title: str, description: str = "") -> Task:
       return self._repository.add(Task(title=title, description=description))

    def get_tasks(self, status: TaskStatus) -> list[Task]:
        return self._repository.get_all(status)

    def get_task_by_id(self, task_id: UUID) -> Task:
        task = self._repository.get_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found.")
        return task
       
    def update_task(
            self, task_id: UUID, title: str | None = None, description: str | None = None
        ) -> Task:
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found.")
        task.update_task(title, description)
        return self._repository.update(task)

    def complete_task(self, task_id: UUID) -> Task:
        task = self.get_task_by_id(task_id)
        if task.status == TaskStatus.COMPLETED:
            raise ValueError(f"Task with ID {task_id} is already completed.")
        task.complete()
        return self._repository.update(task)

    def reopen_task(self, task_id: UUID) -> Task:
        task = self.get_task_by_id(task_id)
        if task.status != TaskStatus.COMPLETED:
            raise ValueError(f"Task with ID {task_id} is not completed and cannot be reopened.")
        task.reopen()
        return self._repository.update(task)

    def delete_task(self, task_id: UUID) -> None:
        task = self.get_task_by_id(task_id)
        if task is not None:
            self._repository.delete(task)
        else:
            raise ValueError(f"Task with ID {task_id} not found.")