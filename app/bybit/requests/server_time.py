import asyncio
from ..scripts.fetcher import fetch_server_time_bybit
from ..scripts.server_time import save_server_time_bybit

async def fetch_server_time():
    while True:
        server_time = fetch_server_time_bybit()
        if server_time:
            save_server_time_bybit(server_time)

        await asyncio.sleep(5)