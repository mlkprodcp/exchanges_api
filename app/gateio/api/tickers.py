from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/gateio/tickers")
async def get_tickers():
    with open("exchanges_data/gateio_data/tickers.json", "r") as f:
        return json.load(f)