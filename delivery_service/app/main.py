from fastapi import FastAPI
from app.api.routes import router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Delivery Service")
Base.metadata.create_all(bind=engine)
app.include_router(router)
