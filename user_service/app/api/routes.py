from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.order_service import create_order, rate_order
from app.schemas.order import OrderCreate, OrderOut, OrderRating
import httpx
from app.core.config import settings

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/order", response_model=OrderOut)
def place_order(order: OrderCreate, db: Session = Depends(get_db)):
    # TODO: Optionally validate restaurant_id using external service
    return create_order(db, order)

@router.post("/rate", response_model=OrderOut)
def rate(order_rating: OrderRating, db: Session = Depends(get_db)):
    updated = rate_order(db, order_rating)
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated

@router.get("/restaurants")
async def get_restaurants(hour: int):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{settings.RESTAURANT_SERVICE_URL}/available?hour={hour}")
        return res.json()
