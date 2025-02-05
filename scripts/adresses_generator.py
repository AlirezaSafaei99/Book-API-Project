import asyncio
import random
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import SessionLocal
from models import Address
from utils.random_data_list import CITIES, STREETS, COUNTRIES

async def insert_addresses():
    async with SessionLocal() as session:
        user_ids = [row[0] for row in (await session.execute("SELECT id FROM users")).fetchall()]  # Fetch user IDs
        addresses = [
            Address(
                street=random.choice(STREETS), 
                city=random.choice(CITIES), 
                country=random.choice(COUNTRIES), 
                user_id=random.choice(user_ids)
            ) for _ in range(1000)
        ]
        session.add_all(addresses)
        await session.commit()
        print("Inserted 1000 addresses")

if __name__ == "__main__":
    asyncio.run(insert_addresses())
