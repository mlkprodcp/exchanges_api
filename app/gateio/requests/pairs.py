import asyncio
from ..scripts.fetcher import fetch_pairs_gateio
from ..scripts.pairs import save_pair_info_gateio, extract_trade_pair_info_gateio

async def fetch_pairs_data():
    while True:
        ticker_data = fetch_pairs_gateio()
        if ticker_data:
            ticker_data_extracted = extract_trade_pair_info_gateio(ticker_data)
            save_pair_info_gateio(ticker_data_extracted)
        
        await asyncio.sleep(5)