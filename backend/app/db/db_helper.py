from fastapi import Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from .db_config import db_settings
from models.pastes import Paste


DATABASE_URL = db_settings.get_database_url()


engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session


async def add_data_db(db: AsyncSession, hashid: str, end_life: str, text: str = None, url: str = None):
    new_paste = Paste(hashid=hashid, end_life=end_life, text=text, url=url)
    db.add(new_paste)
    await db.commit()
    