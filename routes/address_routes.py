from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from services.address_services import create_address, get_address, update_address, delete_address
from schemas.address import AddressCreate, AddressUpdate, AddressResponse

router = APIRouter(prefix="/addresses", tags=["Addresses"])

@router.post("/", response_model=AddressResponse)
async def create_address_api(address: AddressCreate, db: AsyncSession = Depends(get_db)):
    return await create_address(db, address)

@router.get("/{address_id}", response_model=AddressResponse)
async def get_address_api(address_id: int, db: AsyncSession = Depends(get_db)):
    address = await get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router.put("/{address_id}", response_model=AddressResponse)
async def update_address_api(address_id: int, address_update: AddressUpdate, db: AsyncSession = Depends(get_db)):
    address = await update_address(db, address_id, address_update)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router.delete("/{address_id}")
async def delete_address_api(address_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_address(db, address_id)
    if not success:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted successfully"}
