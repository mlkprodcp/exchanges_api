from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/bybit/time")
async def get_time():
    with open("exchanges_data/bybit_data/time.json", "r") as f:
        return json.load(f)