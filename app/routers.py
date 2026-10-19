from fastapi import APIRouter,HTTPException
from app.schemas import TaskCreate, TaskResponse,TaskUpdate
from app import services
from app.services import get_all_tasks,create_task,update_task


router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"],
)


@router.get("/", response_model=list[TaskResponse])
def get_tasks():
    return services.get_all_tasks()


@router.post("/", response_model=TaskResponse, status_code=201)
def add_task(task: TaskCreate):
    return services.create_task(task)

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate):
    task = services.update_task(task_id, data)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task



@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    deleted = services.delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return None
