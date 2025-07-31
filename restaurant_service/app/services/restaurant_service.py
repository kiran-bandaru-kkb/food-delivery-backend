from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate

def create_restaurant(db: Session, data: RestaurantCreate):
    rest = Restaurant(**data.dict())
    db.add(rest)
    db.commit()
    db.refresh(rest)
    return rest

def update_restaurant(db: Session, data: RestaurantUpdate):
    rest = db.query(Restaurant).filter(Restaurant.id == data.id).first()
    if not rest:
        return None
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(rest, attr, value)
    db.commit()
    db.refresh(rest)
    return rest

def get_online_restaurants(db: Session):
    return db.query(Restaurant).filter(Restaurant.is_online == True).all()
