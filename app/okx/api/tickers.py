from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/okx/tickers")
async def get_tickers():
    with open("exchanges_data/okx_data/tickers.json", "r") as f:
        return json.load(f)