import asyncio
from ..scripts.fetcher import fetch_ticker_data_binance
from ..scripts.tickers import save_ticker_data_binance, extract_ticker_data_binance

async def fetch_ticker_data():
    while True:
        ticker_data = fetch_ticker_data_binance()
        if ticker_data:
            ticker_data_extracted = extract_ticker_data_binance(ticker_data)
            save_ticker_data_binance(ticker_data_extracted)
        
        await asyncio.sleep(5)