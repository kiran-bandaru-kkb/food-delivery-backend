from pydantic import BaseModel
from typing import Optional

class RestaurantCreate(BaseModel):
    name: str
    is_online: bool
    menu: str
    price: float

class RestaurantOut(RestaurantCreate):
    id: str

    class Config:
        def __init__(self):
            pass

        orm_mode = True

class RestaurantUpdate(BaseModel):
    id: str
    is_online: Optional[bool] = None
    menu: Optional[str] = None
    price: Optional[float] = None
