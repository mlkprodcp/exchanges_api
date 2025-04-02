import asyncio
from ..scripts.fetcher import fetch_ticker_data_mexc
from ..scripts.tickers import save_tickers_data_mexc, extract_tickers_info_mexc

async def fetch_ticker_data():
    while True:
        ticker_data = fetch_ticker_data_mexc()
        if ticker_data:
            ticker_data_extracted = extract_tickers_info_mexc(ticker_data)
            save_tickers_data_mexc(ticker_data_extracted)
        
        await asyncio.sleep(5)