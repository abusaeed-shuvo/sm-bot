from sqlalchemy import Column, Integer, String, Text
from database.base import Base

class Snippet(Base):
    __tablename__ = "snippets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(String(50), nullable=False)
    