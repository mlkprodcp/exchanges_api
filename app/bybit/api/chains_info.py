"""from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/bybit/chains_info")
async def get_coins_info():
    with open("exchanges_data/bybit_data/chains_info.json", "r") as f:
        return json.load(f)"""