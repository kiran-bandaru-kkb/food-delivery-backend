from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime

from datetime import datetime
from app.db.base import Base
import uuid

class DeliveryAgent(Base):
    __tablename__ = "delivery_agents"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)


class DeliveryOrder(Base):
    __tablename__ = "delivery_orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    restaurant_id = Column(String, nullable=False)
    agent_id = Column(Integer, ForeignKey("delivery_agents.id"))
    status = Column(String, default="pending")