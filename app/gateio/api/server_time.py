from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/gateio/time")
async def get_time():
    with open("exchanges_data/gateio_data/time.json", "r") as f:
        return json.load(f)