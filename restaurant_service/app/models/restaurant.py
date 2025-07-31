from sqlalchemy import Column, String, Boolean, Float
from app.db.base import Base
import uuid

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    is_online = Column(Boolean, default=True)
    menu = Column(String)  # JSON string or plain text for now
    price = Column(Float, default=0.0)
