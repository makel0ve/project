import io

from aiobotocore.session import get_session, AioBaseClient

from .s3_config import storage_settings


SERVICE_NAME = storage_settings.get_service_name()
ENDPOINT_URL = storage_settings.get_endpoint_url()
ACCESS_KEY_ID = storage_settings.get_access_key_id()
SECRET_KEY = storage_settings.get_secret_key()
REGION = storage_settings.get_region()
BUCKET_NAME = storage_settings.get_bucket_name()


async def get_session_s3():
    session = get_session()

    async with session.create_client(
        service_name=SERVICE_NAME,
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_KEY,
        region_name=REGION
    ) as s3_client:
        yield s3_client
        

async def upload_file(s3: AioBaseClient, text: str, hashid: str):
    s3 = s3
    text = text

    data = io.BytesIO(text.encode('utf-8'))

    await s3.put_object(Bucket=BUCKET_NAME, Key=f'{hashid}', Body=data)
    
    
async def get_data_from_file(s3: AioBaseClient, hashid: str):
    s3 = s3
    hashid = hashid
    
    response = await s3.get_object(Bucket=BUCKET_NAME, Key=hashid)

    async with response['Body'] as stream:
        file_data = await stream.read()
    
    return file_data.decode('utf-8')


async def delete_file_from_s3(s3:AioBaseClient, hashid: str):
    s3 = s3
    hashid = hashid
    
    response = await s3.delete_object(Bucket=BUCKET_NAME, Key=hashid)
    return response
    