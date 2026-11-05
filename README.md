# todo-fastapi

A TODO list REST API built with FastAPI and an in-memory database, following clean code principles and design patterns. Data is lost when the server restarts.

## Requirements

- Python 3.12+

## Getting started

```bash
pip install -r requirements.txt
cd src
uvicorn main:app --reload
```

Interactive docs (Swagger UI): http://127.0.0.1:8000/docs

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/tasks` | Create a task |
| GET | `/tasks?status=pending\|done` | List tasks, optionally filtered by status |
| GET | `/tasks/{task_id}` | Get a task by id |
| PATCH | `/tasks/{task_id}` | Update title and/or description |
| POST | `/tasks/{task_id}/complete` | Mark a task as done |
| POST | `/tasks/{task_id}/reopen` | Mark a task as pending |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Project structure

```
src/
  main.py                      Application entrypoint
  app/
    domain/tasks.py            Task entity and TaskStatus
    application/
      repository.py            TaskRepository (abstract contract)
      task_service.py          Use cases
      models/schemas.py        Request/response DTOs
    infrastructure/
      memory_repository.py     Thread-safe in-memory TaskRepository
    api/
      routes.py                HTTP routes
      dependencies.py          Dependency injection providers
      error_handlers.py        Exception to HTTP response mapping
```

## Design

- **Repository pattern**: the service depends on the `TaskRepository` abstraction, not on a concrete storage.
- **Service layer**: business use cases live in `TaskService`, keeping routes thin.
- **Dependency injection**: FastAPI `Depends` wires the service and a single shared repository instance.
- **DTOs**: Pydantic schemas validate input and shape output, separate from the domain entity.

Dependencies point inward (api, then application, then domain), so replacing the in-memory store with a real database only requires a new `TaskRepository` implementation and a change in `dependencies.py`.
