from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from models.author import Author
from schemas.author import AuthorCreate, AuthorUpdate

async def create_author(db: AsyncSession, author: AuthorCreate):
    author_dict = author.dict()
    
    
    if isinstance(author_dict["birthday"], str):
        author_dict["birthday"] = datetime.strptime(author_dict["birthday"], "%Y-%m-%d").date()
    
    db_author = Author(**author_dict)
    db.add(db_author)
    await db.commit()
    await db.refresh(db_author)
    return db_author

async def get_author(db: AsyncSession, author_id: int):
    result = await db.execute(select(Author).filter(Author.id == author_id))
    return result.scalars().first()

async def update_author(db: AsyncSession, author_id: int, author_update: AuthorUpdate):
    author = await get_author(db, author_id)
    if not author:
        return None
    
    for key, value in author_update.dict(exclude_unset=True).items():
        setattr(author, key, value)

    await db.commit()
    await db.refresh(author)
    return author

async def delete_author(db: AsyncSession, author_id: int):
    author = await get_author(db, author_id)
    if not author:
        return None

    await db.delete(author)
    await db.commit()
    return True
