from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/mexc/tickers")
async def get_tickers():
    with open("exchanges_data/mexc_data/tickers.json", "r") as f:
        return json.load(f)