from sqlalchemy.orm import Session
from app.models.agent import DeliveryAgent
from app.schemas.agent import AgentCreate, AgentStatusUpdate

def create_agent(db: Session, data: AgentCreate):
    agent = DeliveryAgent(name=data.name)
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

def update_agent_status(db: Session, data: AgentStatusUpdate):
    agent = db.query(DeliveryAgent).filter(DeliveryAgent.id == data.agent_id).first()
    if not agent:
        return None
    agent.is_available = data.is_available
    agent.current_order_id = data.current_order_id
    db.commit()
    db.refresh(agent)
    return agent

def get_available_agents(db: Session):
    return db.query(DeliveryAgent).filter(DeliveryAgent.is_available == True).all()
