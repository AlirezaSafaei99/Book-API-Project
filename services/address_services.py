from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.address import Address
from schemas.address import AddressCreate, AddressUpdate

async def create_address(db: AsyncSession, address: AddressCreate):
    new_address = Address(**address.dict())
    db.add(new_address)
    await db.commit()
    await db.refresh(new_address)
    return new_address

async def get_address(db: AsyncSession, address_id: int):
    result = await db.execute(select(Address).filter(Address.id == address_id))
    return result.scalars().first()

async def update_address(db: AsyncSession, address_id: int, address_update: AddressUpdate):
    address = await get_address(db, address_id)
    if not address:
        return None

    for key, value in address_update.dict(exclude_unset=True).items():
        setattr(address, key, value)

    await db.commit()
    await db.refresh(address)
    return address

async def delete_address(db: AsyncSession, address_id: int):
    address = await get_address(db, address_id)
    if not address:
        return None

    await db.delete(address)
    await db.commit()
    return True
