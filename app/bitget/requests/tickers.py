import asyncio
from ..scripts.fetcher import fetch_tickers_data_bitget
from ..scripts.tickers import save_tickers_data_bitget, extract_tickers_data_bitget

async def fetch_tickers_data():
    while True:
        ticker_data = fetch_tickers_data_bitget()
        if ticker_data:
            ticker_data_extracted = extract_tickers_data_bitget(ticker_data)
            save_tickers_data_bitget(ticker_data_extracted)
        
        await asyncio.sleep(5)