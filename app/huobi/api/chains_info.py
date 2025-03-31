from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/huobi/chains")
async def get_chains():
    with open("exchanges_data/huobi_data/chains_info.json", "r") as f:
        return json.load(f)