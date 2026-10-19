from pydantic import BaseModel,Field,ConfigDict
from typing import Optional
from typing import Literal


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    priority: Literal["low", "medium", "high"] | None = None
    completed: bool | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool