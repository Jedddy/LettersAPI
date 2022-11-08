from sqlalchemy import func
from sqlalchemy.orm import Session

from . import db_models, schemas


def get_letter(db: Session):
    return db.query(db_models.LetterDB).order_by(func.random()).first()


def create_letter(db: Session, letter: schemas.LetterCreate):
    db_letter = db_models.LetterDB(**letter.dict())
    db.add(db_letter)
    db.commit()
    db.refresh(db_letter)
    return db_letter