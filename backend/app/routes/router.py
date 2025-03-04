from datetime import datetime

from fastapi import APIRouter, Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession

from .router_config import router_settings
from db.db_helper import get_db, add_data_db, get_data_db
from hash.hash import generate_unique_code
from storage.s3_client import get_session_s3, upload_file, get_data_from_file


router = APIRouter(prefix='/paste')
MAX_SIZE_TEXT = router_settings.get_max_size_text()


@router.get('/{hashid}')
async def root(
    hashid: str,
    db: AsyncSession = Depends(get_db),
    s3 = Depends(get_session_s3)
):
    data = await get_data_db(db=db, hashid=hashid)
    
    if not data.text:
        data.text = await get_data_from_file(s3=s3, hashid=hashid)
    
    return {"message": "Hello World", "data": data}


@router.post('/')
async def add_paste(
    text: str = Form(),
    end_life: datetime = Form(),
    db: AsyncSession = Depends(get_db),
    s3 = Depends(get_session_s3)
):
    hashid = await generate_unique_code()
    
    if len(text) > MAX_SIZE_TEXT:
        await upload_file(s3=s3, text=text, hashid=hashid)
        await add_data_db(db=db, hashid=hashid, end_life=end_life)
    else:
        await add_data_db(db=db, hashid=hashid, text=text, end_life=end_life)
        
    return {"hashid": hashid}