from fastapi import FastAPI
from app.db import engine
from app.models import Base
from app.routes import student
from app.routes import student, quiz
from app.routes import student, quiz, flashcard

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student.router)
app.include_router(quiz.router)
app.include_router(flashcard.router)

@app.get("/")
def root():
    return {"message": "Backend Running 🚀"}