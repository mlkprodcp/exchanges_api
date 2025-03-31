from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/huobi/currencies")
async def get_currencies():
    with open("exchanges_data/huobi_data/currencies.json", "r") as f:
        return json.load(f)