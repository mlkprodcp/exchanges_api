from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/bybit/tickers")
async def get_tickers():
    with open("exchanges_data/bybit_data/tickers.json", "r") as f:
        return json.load(f)