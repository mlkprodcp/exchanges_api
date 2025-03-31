import asyncio
from ..scripts.fetcher import fetch_exchange_info_gateio
from ..scripts.chains_info import save_exchange_info_gateio, extract_exchange_info_gateio

async def fetch_exchange_info():
    while True:
        exchange_info = fetch_exchange_info_gateio()
        if exchange_info:
            exchange_info_data = extract_exchange_info_gateio(exchange_info)
            save_exchange_info_gateio(exchange_info_data)
        
        await asyncio.sleep(5)