from database import crud
from deps.dependencies import db_conn
from fastapi import APIRouter, Depends, Form
from models.letter import Letter
from sqlalchemy.orm import Session

router = APIRouter(tags=["letters"])

@router.get("/get_letter", response_model=Letter)
async def get_letter(db: Session = Depends(db_conn)):
    if not crud.get_letter(db):
        return {"message": "No entries yet! Be the first one!"}
    return crud.get_letter(db).__dict__


@router.post("/send_letter")
async def send_letter(author: str = Form("Anonymous"), content: str = Form(), db: Session = Depends(db_conn)):
    letter = Letter(author=author, content=content)
    crud.create_letter(db, letter)
    return {"message": "Letter sent!"}