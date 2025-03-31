import asyncio
from ..scripts.fetcher import fetch_coins_info_bitget
from ..scripts.chains_info import save_coins_info_bitget, extract_coins_info_bitget

async def fetch_coins_info():
    while True:
        exchange_info = fetch_coins_info_bitget()
        if exchange_info:
            exchange_info_data = extract_coins_info_bitget(exchange_info)
            save_coins_info_bitget(exchange_info_data)
        
        await asyncio.sleep(5)