import asyncio
from ..scripts.fetcher import fetch_server_time_bitget
from ..scripts.server_time import save_server_time_bitget

async def fetch_server_time():
    while True:
        server_time = fetch_server_time_bitget()
        if server_time:
            save_server_time_bitget(server_time)

        await asyncio.sleep(5)