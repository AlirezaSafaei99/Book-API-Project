import asyncio
from scripts.authors_generator import insert_authors
from scripts.books_generator import insert_books
from scripts.users_generators import insert_users
from scripts.adresses_generator import insert_addresses

async def seed_all():
    await insert_authors()
    await insert_books()
    await insert_users()
    await insert_addresses()
    print("All tables seeded successfully!")

if __name__ == "__main__":
    asyncio.run(seed_all())
