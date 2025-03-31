import asyncio
from ..scripts.fetcher import fetch_chains_data_huobi
from ..scripts.chains_info import save_chains_info_huobi, extract_chains_info_huobi

async def fetch_chains_info():
    while True:
        chains_info = fetch_chains_data_huobi()
        if chains_info:
            chains_info_data = extract_chains_info_huobi(chains_info)
            save_chains_info_huobi(chains_info_data)
        
        await asyncio.sleep(5)