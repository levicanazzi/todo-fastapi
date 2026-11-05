from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

class TaskStatus(str, Enum):
    PENDING = "pending"
    DONE = "done"

def _utcnow() -> datetime:
    return datetime.now(timezone.utc)  

@dataclass
class Task:
    title: str
    description: str = ""
    id: UUID = field(default_factory=uuid4)
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=_utcnow)
    updated_at: datetime = field(default_factory=_utcnow)

    def update_task(self, title: str | None, description: str | None) -> None:
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
            self.updated_at = _utcnow()

    def complete(self) -> None:
        self.status = TaskStatus.DONE
        self.updated_at = _utcnow()

    def reopen(self) -> None:
        self.status = TaskStatus.PENDING
        self.updated_at = _utcnow()    