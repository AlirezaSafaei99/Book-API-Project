from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    price: float
    quantity: int
    author_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
