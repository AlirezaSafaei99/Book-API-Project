import asyncio
import random
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import SessionLocal
from models import Book
from models import Author
from utils.random_data_list import BOOK_TITLES

async def insert_books():
    async with SessionLocal() as session:
        author_ids = [row[0] for row in (await session.execute("SELECT id FROM authors")).fetchall()]  # Fetch author IDs
        books = [
            Book(
                title=random.choice(BOOK_TITLES), 
                price=round(random.uniform(5, 100), 2), 
                quantity=random.randint(1, 100), 
                author_id=random.choice(author_ids)
            ) for _ in range(1000)
        ]
        session.add_all(books)
        await session.commit()
        print("Inserted 1000 books")

if __name__ == "__main__":
    asyncio.run(insert_books())
