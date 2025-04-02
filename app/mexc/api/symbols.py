from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/mexc/symbols")
async def get_instruments_info():
    with open("exchanges_data/mexc_data/symbols.json", "r") as f:
        return json.load(f)