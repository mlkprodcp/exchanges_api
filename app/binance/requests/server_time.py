import asyncio
from ..scripts.fetcher import fetch_server_time_binance
from ..scripts.server_time import save_server_time_binance

async def fetch_server_time():
    while True:
        server_time = fetch_server_time_binance()
        if server_time:
            save_server_time_binance(server_time)

        await asyncio.sleep(5)