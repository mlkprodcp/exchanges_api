from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/bitget/time")
async def get_time():
    with open("exchanges_data/bitget_data/time.json", "r") as f:
        return json.load(f)