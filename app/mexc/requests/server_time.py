import asyncio
from ..scripts.fetcher import fetch_server_time_mexc
from ..scripts.server_time import save_server_time_mexc

async def fetch_server_time():
    while True:
        server_time = fetch_server_time_mexc()
        if server_time:
            save_server_time_mexc(server_time)

        await asyncio.sleep(5)