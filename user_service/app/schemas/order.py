from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    user_id: str
    restaurant_id: str

class OrderOut(BaseModel):
    id: str
    user_id: str
    restaurant_id: str
    status: str

    class Config:
        orm_mode = True

class OrderRating(BaseModel):
    order_id: str
    food_rating: Optional[int] = None
    agent_rating: Optional[int] = None
