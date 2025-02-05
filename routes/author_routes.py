from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from services.author_services import create_author, get_author, update_author, delete_author
from schemas.author import AuthorCreate, AuthorUpdate, AuthorResponse

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/", response_model=AuthorResponse)
async def create_author_api(author: AuthorCreate, db: AsyncSession = Depends(get_db)):
    return await create_author(db, author)

@router.get("/{author_id}", response_model=AuthorResponse)
async def get_author_api(author_id: int, db: AsyncSession = Depends(get_db)):
    author = await get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.put("/{author_id}", response_model=AuthorResponse)
async def update_author_api(author_id: int, author_update: AuthorUpdate, db: AsyncSession = Depends(get_db)):
    author = await update_author(db, author_id, author_update)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.delete("/{author_id}")
async def delete_author_api(author_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_author(db, author_id)
    if not success:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}
