from sqlalchemy import Column, Integer, String

from .database import Base


class LetterDB(Base):
    __tablename__ = "letters"

    letter_id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    author = Column(String)