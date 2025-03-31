from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/binance/time")
async def get_time():
    with open("exchanges_data/binance_data/time.json", "r") as f:
        return json.load(f)