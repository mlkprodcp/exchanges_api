import asyncio
from ..scripts.fetcher import fetch_server_time_okx
from ..scripts.server_time import save_server_time_okx

async def fetch_server_time():
    while True:
        server_time = fetch_server_time_okx()
        if server_time:
            save_server_time_okx(server_time)

        await asyncio.sleep(5)