import asyncio
from ..scripts.fetcher import fetch_ticker_data_okx
from ..scripts.tickers import save_tickers_data_okx, extract_tickers_info_okx

async def fetch_ticker_data():
    while True:
        ticker_data = fetch_ticker_data_okx()
        if ticker_data:
            ticker_data_extracted = extract_tickers_info_okx(ticker_data)
            save_tickers_data_okx(ticker_data_extracted)
        
        await asyncio.sleep(5)