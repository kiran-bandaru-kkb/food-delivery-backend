from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.delivery import DeliveryCreate, DeliveryOut
from app.schemas.delivery_agent import DeliveryAgentOut, DeliveryAgentCreate
from app.services.delivery_service import assign_delivery, list_deliveries
from app.services.delivery_agent_service import create_delivery_agent

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/assign", response_model=DeliveryOut)
def assign(data: DeliveryCreate, db: Session = Depends(get_db)):
    return assign_delivery(db, data)

@router.get("/list", response_model=list[DeliveryOut])
def get_deliveries(db: Session = Depends(get_db)):
    return list_deliveries(db)

@router.post("/agents", response_model=DeliveryAgentOut)
def register_agent(data: DeliveryAgentCreate, db: Session = Depends(get_db)):
    return create_delivery_agent(db, data)