import asyncio
from ..scripts.fetcher import fetch_server_time_gateio
from ..scripts.server_time import save_server_time_gateio

async def fetch_server_time():
    while True:
        server_time = fetch_server_time_gateio()
        if server_time:
            save_server_time_gateio(server_time)

        await asyncio.sleep(5)