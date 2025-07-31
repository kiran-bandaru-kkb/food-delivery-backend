# app/schemas/delivery_agent.py

from pydantic import BaseModel

class DeliveryAgentCreate(BaseModel):
    name: str
    phone: str

class DeliveryAgentOut(BaseModel):
    id: int
    name: str
    phone: str

    class Config:
        orm_mode = True
