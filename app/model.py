
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False, default="")
    #priority = Column(String(10), nullable=False, default="medium")
    completed = Column(Boolean, nullable=False, default=False)
