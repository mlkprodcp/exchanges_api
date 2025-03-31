from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/gateio/pairs")
async def get_pair():
    with open("exchanges_data/gateio_data/pairs.json", "r") as f:
        return json.load(f)