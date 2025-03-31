import asyncio
from ..scripts.fetcher import fetch_tickers_data_huobi
from ..scripts.tickers import save_tickers_data_huobi, extract_tickers_data_huobi

async def fetch_tickers_data():
    while True:
        tickers_data = fetch_tickers_data_huobi()
        if tickers_data:
            ticker_data_extracted = extract_tickers_data_huobi(tickers_data)
            save_tickers_data_huobi(ticker_data_extracted)
        
        await asyncio.sleep(5)