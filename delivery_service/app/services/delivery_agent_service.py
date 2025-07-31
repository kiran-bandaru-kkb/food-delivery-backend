from sqlalchemy.orm import Session
from app.models.agent import DeliveryAgent, DeliveryOrder
from app.schemas.delivery_agent import DeliveryAgentCreate


def create_delivery_agent(db: Session, data: DeliveryAgentCreate):
    agent = DeliveryAgent(name=data.name, phone=data.phone)
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent