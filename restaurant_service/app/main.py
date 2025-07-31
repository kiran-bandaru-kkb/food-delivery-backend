from fastapi import FastAPI
from app.api.routes import router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Restaurant Service")

# Create tables
Base.metadata.create_all(bind=engine)

# Include your API routes here
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Restaurant Service OK"}