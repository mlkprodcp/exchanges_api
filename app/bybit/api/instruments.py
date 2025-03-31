from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/bybit/instruments")
async def get_instruments_info():
    with open("exchanges_data/bybit_data/instruments.json", "r") as f:
        return json.load(f)