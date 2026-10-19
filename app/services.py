
from sqlalchemy.orm import Session
from app.model import Task
from app.schemas import TaskCreate, TaskUpdate


def create_task(db: Session, data: TaskCreate) -> Task:
    task = Task(**data.model_dump())

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_all_tasks(db: Session) -> list[Task]:
    return db.query(Task).order_by(Task.id).all()


def get_task(db: Session, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(
    db: Session,
    task_id: int,
    data: TaskUpdate,
) -> Task | None:
    task = get_task(db, task_id)

    if task is None:
        return None

    changes = data.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task_id: int) -> bool:
    task = get_task(db, task_id)

    if task is None:
        return False

    db.delete(task)
    db.commit()

    return True
