from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.agent import AgentCreate, AgentStatusUpdate, AgentOut
from app.services.delivery_service import create_agent, update_agent_status, get_available_agents

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=AgentOut)
def register_agent(data: AgentCreate, db: Session = Depends(get_db)):
    return create_agent(db, data)

@router.patch("/update-status", response_model=AgentOut)
def update_status(data: AgentStatusUpdate, db: Session = Depends(get_db)):
    updated = update_agent_status(db, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Agent not found")
    return updated

@router.get("/available")
def list_available(db: Session = Depends(get_db)):
    return get_available_agents(db)
