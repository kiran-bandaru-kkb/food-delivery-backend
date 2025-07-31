from pydantic import BaseModel
from typing import Optional

class AgentCreate(BaseModel):
    name: str

class AgentStatusUpdate(BaseModel):
    agent_id: str
    is_available: bool
    current_order_id: Optional[str] = None

class AgentOut(AgentCreate):
    id: str
    is_available: bool
    class Config:
        orm_mode = True
