from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/flashcards")
def create_flashcard(data: schemas.FlashcardCreate, db: Session = Depends(get_db)):
    return crud.create_flashcard(db, data)


@router.get("/flashcards")
def get_flashcards(db: Session = Depends(get_db)):
    return crud.get_flashcards(db)