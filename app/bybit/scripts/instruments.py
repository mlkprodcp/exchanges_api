import json
from ..config.keys import client_bybit

def save_instruments_info_bybit(data):
    with open('exchanges_data/bybit_data/instruments.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_instruments_info_bybit(data):
    instruments_info = {
        "retCode": data.get("retCode", 0),
        "retMsg": data.get("retMsg"),
        "result": {
            "category": data.get("result", {}).get("category"),
            "list": [
                {
                    "symbol": item.get("symbol"),
                    "baseCoin": item.get("baseCoin"),
                    "quoteCoin": item.get("quoteCoin"),
                    "innovation": item.get("innovation"),
                    "status": item.get("status"),
                    "marginTrading": item.get("marginTrading"),
                    "stTag": item.get("stTag"),
                    "lotSizeFilter": {
                        "basePrecision": item.get("lotSizeFilter", {}).get("basePrecision"),
                        "quotePrecision": item.get("lotSizeFilter", {}).get("quotePrecision"),
                        "minOrderQty": item.get("lotSizeFilter", {}).get("minOrderQty"),
                        "maxOrderQty": item.get("lotSizeFilter", {}).get("maxOrderQty"),
                        "minOrderAmt": item.get("lotSizeFilter", {}).get("minOrderAmt"),
                        "maxOrderAmt": item.get("lotSizeFilter", {}).get("maxOrderAmt")
                    },
                    "priceFilter": {
                        "tickSize": item.get("priceFilter", {}).get("tickSize")
                    }
                }
                for item in data.get("result", {}).get("list", [])
            ]
        },
        "time": data.get("time", 0)
    }
    return instruments_info