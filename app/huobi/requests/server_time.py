import asyncio
from ..scripts.fetcher import fetch_server_time_huobi
from ..scripts.server_time import save_server_time_huobi

async def fetch_server_time():
    while True:
        server_time = fetch_server_time_huobi()
        if server_time:
            save_server_time_huobi(server_time)

        await asyncio.sleep(5)