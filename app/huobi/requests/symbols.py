import asyncio
from ..scripts.fetcher import fetch_symbols_info_huobi
from ..scripts.symbols import save_symbols_info_huobi, extract_symbols_info_huobi

async def fetch_symbols_info():
    while True:
        symbols_info = fetch_symbols_info_huobi()
        if symbols_info:
            symbols_info_data = extract_symbols_info_huobi(symbols_info)
            save_symbols_info_huobi(symbols_info_data)
        
        await asyncio.sleep(5)