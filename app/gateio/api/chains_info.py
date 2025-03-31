from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/gateio/chains_info")
async def get_exchange_info():
    with open("exchanges_data/gateio_data/chains_info.json", "r") as f:
        return json.load(f)