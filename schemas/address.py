from pydantic import BaseModel

class AddressBase(BaseModel):
    street: str
    city: str
    country: str
    user_id: int

class AddressCreate(AddressBase):
    pass

class AddressUpdate(AddressBase):
    pass

class AddressResponse(AddressBase):
    id: int

    class Config:
        orm_mode = True
