from pydantic import BaseModel


class Letter(BaseModel):
    author: str
    content: str