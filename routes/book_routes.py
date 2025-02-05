from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from services.book_services import create_book, get_book, update_book, delete_book, search_books, sort_books
from schemas.book import BookCreate, BookUpdate, BookResponse
from typing import List

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponse)
async def create_book_api(book: BookCreate, db: AsyncSession = Depends(get_db)):
    return await create_book(db, book)

@router.get("/{book_id}", response_model=BookResponse)
async def get_book_api(book_id: int, db: AsyncSession = Depends(get_db)):
    book = await get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookResponse)
async def update_book_api(book_id: int, book_update: BookUpdate, db: AsyncSession = Depends(get_db)):
    book = await update_book(db, book_id, book_update)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}")
async def delete_book_api(book_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

@router.get("/search/", response_model=List[BookResponse])
async def search_books_api(title: str, nationality: str, db: AsyncSession = Depends(get_db)):
    return await search_books(db, title, nationality)

@router.get("/sort/", response_model=List[BookResponse])
async def sort_books_api(sort_by: str = "quantity", db: AsyncSession = Depends(get_db)):
    return await sort_books(db, sort_by)
