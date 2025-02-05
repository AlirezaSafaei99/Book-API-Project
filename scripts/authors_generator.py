import asyncio
import random
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import SessionLocal
from models import Author
from utils.random_data_list import NAMES, SURNAMES, COUNTRIES, CITIES

async def insert_authors():
    async with SessionLocal() as session:
        authors = [
            Author(
                name=f"{random.choice(NAMES)} {random.choice(SURNAMES)}", 
                nationality=random.choice(COUNTRIES), 
                birthday=f"{random.randint(1900, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}", 
                place_of_birth=random.choice(CITIES)
            ) for _ in range(1000)
        ]
        session.add_all(authors)
        await session.commit()
        print("Inserted 1000 authors")

if __name__ == "__main__":
    asyncio.run(insert_authors())
