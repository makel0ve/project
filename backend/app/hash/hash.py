import hashlib
import time


async def generate_unique_code():
    return hashlib.sha256(str(time.time()).encode('utf-8')).hexdigest()[:6]
