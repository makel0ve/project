import asyncio

from celery import Celery

from db.db_helper import delete_data
from storage.s3_client import delete_file_from_s3
from .tasks_config import tasks_settings


REDIS_URL = tasks_settings.get_redis_url()

celery = Celery('tasks', broker=REDIS_URL, broker_connection_retry_on_startup=True)


@celery.task()
def delete_data_and_file(delete_id):
    asyncio.run(delete_data_task(delete_id))


async def delete_data_task(delete_id):
    delete_url = await delete_data(delete_id)

    await delete_data_file(delete_url)


async def delete_data_file(delete_url):
    await delete_file_from_s3(delete_url)