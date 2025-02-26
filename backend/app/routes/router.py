from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_helper import get_db


router = APIRouter(prefix='/paste')


@router.get('/')
async def root(
    db: AsyncSession = Depends(get_db)
):
    return {"message": "Hello World"}