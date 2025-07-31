from sqlalchemy.orm import Session
from app import models, schemas

def create_order(db: Session, order: schemas.order.OrderCreate):
    db_order = models.order.Order(
        user_id=order.user_id,
        restaurant_id=order.restaurant_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def rate_order(db: Session, rating: schemas.order.OrderRating):
    db_order = db.query(models.order.Order).filter(models.order.Order.id == rating.order_id).first()
    if not db_order:
        return None
    if rating.food_rating is not None:
        db_order.food_rating = rating.food_rating
    if rating.agent_rating is not None:
        db_order.agent_rating = rating.agent_rating
    db.commit()
    db.refresh(db_order)
    return db_order
