from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/huobi/tickers")
async def get_tickers_info():
    with open("exchanges_data/huobi_data/tickers.json", "r") as f:
        return json.load(f)