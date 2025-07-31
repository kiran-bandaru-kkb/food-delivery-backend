from sqlalchemy.orm import Session
from app import models, schemas
from app.schemas.user import UserCreate
from app.models.user import User


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
