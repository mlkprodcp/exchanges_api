from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/bitget/chains_info")
async def get_coins_info():
    with open("exchanges_data/bitget_data/chains_info.json", "r") as f:
        return json.load(f)