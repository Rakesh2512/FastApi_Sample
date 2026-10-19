
from app.schemas import TaskCreate, TaskUpdate

tasks: list[dict] = []
next_id = 1


def create_task(data: TaskCreate) -> dict:
    global next_id

    task = {
        "id": next_id,
        **data.model_dump(),
        "completed": False,
    }

    tasks.append(task)
    next_id += 1

    return task


def get_all_tasks() -> list[dict]:
    return tasks


def get_task(task_id: int) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_task(task_id: int, data: TaskUpdate) -> dict | None:
    task = get_task(task_id)

    if task is None:
        return None

    changes = data.model_dump(exclude_unset=True)
    task.update(changes)

    return task


def delete_task(task_id: int) -> bool:
    task = get_task(task_id)

    if task is None:
        return False

    tasks.remove(task)
    return True
