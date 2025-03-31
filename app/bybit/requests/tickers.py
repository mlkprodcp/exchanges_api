import asyncio
from ..scripts.fetcher import fetch_tickers_data_bybit
from ..scripts.tickers import save_ticker_data_bybit, extract_ticker_data_bybit

async def fetch_ticker_data():
    while True:
        ticker_data = fetch_tickers_data_bybit()
        if ticker_data:
            ticker_data_extracted = extract_ticker_data_bybit(ticker_data)
            save_ticker_data_bybit(ticker_data_extracted)
        
        await asyncio.sleep(5)