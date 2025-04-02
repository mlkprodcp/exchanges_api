import asyncio
from ..scripts.fetcher import fetch_chains_info_mexc
from ..scripts.chains_info import save_chains_info_mexc, extract_chains_info_mexc

async def fetch_chains_info():
    while True:
        chains_info = fetch_chains_info_mexc()
        if chains_info:
            chains_info_data = extract_chains_info_mexc(chains_info)
            save_chains_info_mexc(chains_info_data)
        
        await asyncio.sleep(5)