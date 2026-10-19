
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app import model
from app.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure all model tables are registered before creation.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Task Management API",
    description="FastAPI CRUD with SQLite and SQLAlchemy",
    version="2.0.0",
    lifespan=lifespan,
)

app.include_router(router)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}
