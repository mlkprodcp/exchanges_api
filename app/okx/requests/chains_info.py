import asyncio
from ..scripts.fetcher import fetch_chains_info_okx
from ..scripts.chains_info import save_chains_info_okx

async def fetch_chains_info():
    while True:
        chains_info = fetch_chains_info_okx()
        if chains_info:
            save_chains_info_okx(chains_info)
        
        await asyncio.sleep(5)