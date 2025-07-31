from sqlalchemy import Column, String, Boolean
from app.db.base import Base
import uuid

class DeliveryAgent(Base):
    __tablename__ = "agents"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    is_available = Column(Boolean, default=True)
    current_order_id = Column(String, nullable=True)
