import asyncio
from ..scripts.fetcher import fetch_tickers_data_gateio
from ..scripts.tickers import save_ticker_data_gateio, extract_ticker_data_gateio

async def fetch_ticker_data():
    while True:
        ticker_data = fetch_tickers_data_gateio()
        if ticker_data:
            ticker_data_extracted = extract_ticker_data_gateio(ticker_data)
            save_ticker_data_gateio(ticker_data_extracted)
        
        await asyncio.sleep(5)