from sqlalchemy.orm import Session
from app.models.agent import DeliveryAgent, DeliveryOrder
from app.schemas.delivery import DeliveryCreate, DeliveryOut

def assign_delivery(db: Session, data: DeliveryCreate):
    # Assign agent_id=1 for now (in real-world: available agent)
    delivery = DeliveryOrder(
        user_id=data.user_id,
        restaurant_id=data.restaurant_id,
        agent_id=1,
        status="assigned"
    )
    db.add(delivery)
    db.commit()
    db.refresh(delivery)
    return delivery

def list_deliveries(db: Session):
    return db.query(DeliveryOrder).all()