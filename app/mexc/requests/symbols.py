import asyncio
from ..scripts.fetcher import fetch_symbols_data_mexc
from ..scripts.symbols import save_symbols_data_mexc, extract_symbols_info_mexc

async def fetch_symbols_data():
    while True:
        symbols_data = fetch_symbols_data_mexc()
        if symbols_data:
            symbols_data_extracted = extract_symbols_info_mexc(symbols_data)
            save_symbols_data_mexc(symbols_data_extracted)
        
        await asyncio.sleep(5)