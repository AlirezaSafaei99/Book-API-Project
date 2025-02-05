import asyncio
import random
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import SessionLocal
from models import User
from utils.random_data_list import NAMES, SURNAMES, generate_email, generate_password

async def insert_users():
    async with SessionLocal() as session:
        users = [
            User(
                name=f"{random.choice(NAMES)} {random.choice(SURNAMES)}", 
                email=generate_email(random.choice(NAMES), random.choice(SURNAMES)), 
                password_hash=generate_password()
            ) for _ in range(1000)
        ]
        session.add_all(users)
        await session.commit()
        print("Inserted 1000 users")

if __name__ == "__main__":
    asyncio.run(insert_users())
