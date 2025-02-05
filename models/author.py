from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db.database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    nationality = Column(String(100), nullable=True)
    birthday = Column(Date, nullable=True)
    place_of_birth = Column(String(255), nullable=True)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")
