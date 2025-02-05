from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.book import Book
from schemas.book import BookCreate, BookUpdate

async def create_book(db: AsyncSession, book: BookCreate):
    new_book = Book(**book.dict())
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book

async def get_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(Book).filter(Book.id == book_id))
    return result.scalars().first()

async def update_book(db: AsyncSession, book_id: int, book_update: BookUpdate):
    book = await get_book(db, book_id)
    if not book:
        return None

    for key, value in book_update.dict(exclude_unset=True).items():
        setattr(book, key, value)

    await db.commit()
    await db.refresh(book)
    return book

async def delete_book(db: AsyncSession, book_id: int):
    book = await get_book(db, book_id)
    if not book:
        return None

    await db.delete(book)
    await db.commit()
    return True

async def search_books(db: AsyncSession, title: str, nationality: str):
    query = select(Book).join(Book.author).filter(
        Book.title.ilike(f"%{title}%"),
        Book.author.nationality.ilike(f"%{nationality}%")
    )
    result = await db.execute(query)
    return result.scalars().all()

async def sort_books(db: AsyncSession, sort_by: str = "quantity"):
    valid_sort_fields = {"quantity": Book.quantity, "price": Book.price}
    order_by_field = valid_sort_fields.get(sort_by, Book.quantity)

    query = select(Book).order_by(order_by_field)
    result = await db.execute(query)
    return result.scalars().all()
