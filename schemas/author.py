from pydantic import BaseModel
from typing import Optional
from datetime import date

class AuthorBase(BaseModel):
    name: str
    nationality: Optional[str] = None
    birthday: Optional[date] = None
    place_of_birth: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int

    class Config:
        orm_mode = True
