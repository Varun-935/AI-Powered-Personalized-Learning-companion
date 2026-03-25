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


@router.post("/quiz")
def submit_quiz(data: schemas.QuizSubmit, db: Session = Depends(get_db)):
    return crud.add_quiz_result(db, data)


@router.get("/quiz")
def get_quiz(db: Session = Depends(get_db)):
    return crud.get_quiz_results(db)