from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/huobi/symbols")
async def get_symbols_info():
    with open("exchanges_data/huobi_data/symbols.json", "r") as f:
        return json.load(f)