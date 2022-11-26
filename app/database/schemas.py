from pydantic import BaseModel

class LetterCreate(BaseModel):
    author: str
    content: str

    class Config:
        orm_mode = True