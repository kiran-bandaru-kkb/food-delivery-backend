from sqlalchemy import Column, String, ForeignKey, Integer
from app.db.base import Base
import uuid

class Order(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    restaurant_id = Column(String)
    delivery_agent_id = Column(String, nullable=True)
    status = Column(String, default="pending")  # pending, accepted, delivered
    food_rating = Column(Integer, nullable=True)
    agent_rating = Column(Integer, nullable=True)
