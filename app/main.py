
from fastapi import FastAPI
from app.routers import router

app = FastAPI(
    title="Advanced Task API",
    description="A structured REST API built with FastAPI",
    version="1.0.0",
)

app.include_router(router)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy Rakesh Paswan"}
