import asyncio
from ..scripts.fetcher import fetch_currencies_data_huobi
from ..scripts.currencies import save_currencies_data_huobi, extract_currencies_data_huobi

async def fetch_currencies_data():
    while True:
        currencies_data = fetch_currencies_data_huobi()
        if currencies_data:
            currencies_data_extracted = extract_currencies_data_huobi(currencies_data)
            save_currencies_data_huobi(currencies_data_extracted)
        
        await asyncio.sleep(5)