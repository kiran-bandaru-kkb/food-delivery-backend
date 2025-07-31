from pydantic import BaseModel
from typing import Optional

class DeliveryCreate(BaseModel):
    user_id: str
    restaurant_id: str
    agent_id: str

class DeliveryOut(BaseModel):
    id: int
    user_id: str
    restaurant_id: str
    agent_id: int
    status: str

    class Config:
        from_attributes = True