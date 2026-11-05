from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, Response, status
from app.api.dependencies import get_task_service
from app.application.models.schemas import CreateTaskRequest, TaskResponse, UpdateTaskRequest
from app.application.task_service import TaskService
from app.domain.tasks import TaskStatus

router = APIRouter(prefix ="/tasks", tags=["tasks"])
Service = Annotated[TaskService, Depends(get_task_service)]

@router.get("", response_model=list[TaskResponse])
def get_tasks(service: Service, status: TaskStatus | None = None):
    return service.get_tasks(status)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: UUID, service: Service):
    return service.get_task_by_id(task_id)

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: CreateTaskRequest, service: Service):
    return service.create_task(payload.title, payload.description)

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: UUID, payload: UpdateTaskRequest, service: Service):
    return service.update_task(task_id, payload.title, payload.description)

@router.post("/{task_id}/complete", response_model=TaskResponse) 
def complete_task(task_id: UUID, service: Service):
    return service.complete_task(task_id)

@router.post("/{task_id}/reopen", response_model=TaskResponse) 
def reopen_task(task_id: UUID, service: Service):
    return service.reopen_task(task_id)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID, service: Service):
    service.delete_task(task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)