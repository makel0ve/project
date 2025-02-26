from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)