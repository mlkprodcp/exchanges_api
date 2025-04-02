import json

def save_tickers_data_mexc(data):
    with open('exchanges_data/mexc_data/tickers.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_tickers_info_mexc(data):
    tickers_info = {
        "data": [
            {
                "symbol": item.get("symbol"),
                "volume": item.get("volume"),
                "amount": item.get("amount"),
                "high": item.get("high"),
                "low": item.get("low"),
                "bid": item.get("bid"),
                "ask": item.get("ask"),
                "open": item.get("open"),
                "last": item.get("last"),
                "time": item.get("time"),
                "change_rate": item.get("change_rate")
            }
            for item in data.get("data", [])
        ]
    }
    return tickers_info