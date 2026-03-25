from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str
    interest: str

class QuizSubmit(BaseModel):
    student_id: int
    topic: str
    score: float

class FlashcardCreate(BaseModel):
    student_id: int
    question: str
    answer: str