from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/binance/tickers")
async def get_tickers():
    with open("exchanges_data/binance_data/tickers.json", "r") as f:
        return json.load(f)