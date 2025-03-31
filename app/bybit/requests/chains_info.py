"""import asyncio
from ..scripts.fetcher import fetch_coins_info_bybit
from ..scripts.chains_info import save_coins_info_bybit

async def fetch_coins_info():
    while True:
        exchange_info = fetch_coins_info_bybit()
        if exchange_info:
            exchange_info_data = fetch_coins_info_bybit(exchange_info)
            save_coins_info_bybit(exchange_info_data)
        
        await asyncio.sleep(10)"""