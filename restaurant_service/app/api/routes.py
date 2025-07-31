from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.restaurant import RestaurantCreate, RestaurantOut, RestaurantUpdate
from app.services.restaurant_service import create_restaurant, update_restaurant, get_online_restaurants
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add", response_model=RestaurantOut)
def add_restaurant(data: RestaurantCreate, db: Session = Depends(get_db)):
    return create_restaurant(db, data)

@router.put("/update", response_model=RestaurantOut)
def update(data: RestaurantUpdate, db: Session = Depends(get_db)):
    updated = update_restaurant(db, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return updated

@router.get("/available")
def available_restaurants(hour: int, db: Session = Depends(get_db)):
    # hour is ignored for now
    return get_online_restaurants(db)
