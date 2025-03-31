import asyncio
from ..scripts.fetcher import fetch_exchange_info_binance
from ..scripts.chains_info import save_exchange_info_binance, extract_exchange_info_binance

async def fetch_exchange_info():
    while True:
        exchange_info = fetch_exchange_info_binance()
        if exchange_info:
            exchange_info_data = extract_exchange_info_binance(exchange_info)
            save_exchange_info_binance(exchange_info_data)
        
        await asyncio.sleep(60)