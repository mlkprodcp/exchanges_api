from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/huobi/time")
async def get_time():
    with open("exchanges_data/huobi_data/time.json", "r") as f:
        return json.load(f)