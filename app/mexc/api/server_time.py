from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/mexc/time")
async def get_time():
    with open("exchanges_data/mexc_data/time.json", "r") as f:
        return json.load(f)