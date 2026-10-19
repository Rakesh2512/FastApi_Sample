
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import TaskCreate, TaskUpdate, TaskResponse
from app import services

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"],
)


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    return services.create_task(db, data)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return services.get_all_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = services.get_task(db, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
):
    task = services.update_task(db, task_id, data)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = services.delete_task(db, task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return None
