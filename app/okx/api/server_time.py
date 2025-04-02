from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/okx/time")
async def get_time():
    with open("exchanges_data/okx_data/time.json", "r") as f:
        return json.load(f)