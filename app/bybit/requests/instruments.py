import asyncio
from ..scripts.fetcher import fetch_instruments_info_bybit
from ..scripts.instruments import save_instruments_info_bybit, extract_instruments_info_bybit

async def fetch_instruments_info():
    while True:
        exchange_info = fetch_instruments_info_bybit()
        if exchange_info:
            exchange_info_data = extract_instruments_info_bybit(exchange_info)
            save_instruments_info_bybit(exchange_info_data)
        
        await asyncio.sleep(10)