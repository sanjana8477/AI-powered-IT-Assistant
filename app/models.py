from pydantic import BaseModel

class Ticket(BaseModel):
    description: str

class Question(BaseModel):
    question: str