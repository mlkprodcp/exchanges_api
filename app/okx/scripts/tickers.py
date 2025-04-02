import json

def save_tickers_data_okx(data):
    with open('exchanges_data/okx_data/tickers.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_tickers_info_okx(data):
    tickers_data = {
        tickers["instId"]: {
            "instId": tickers.get("instId"),
            "last": tickers.get("last"),
            "lastSz": tickers.get("lastSz"),
            "askPx": tickers.get("askPx"),
            "askSz": tickers.get("askSz"),
            "bidPx": tickers.get("bidPx"),
            "bidSz": tickers.get("bidSz"),
            "open24h": tickers.get("open24h"),
            "high24h": tickers.get("high24h"),
            "low24h": tickers.get("low24h"),
            "volCcy24h": tickers.get("volCcy24h"),
            "vol24h": tickers.get("vol24h"),
            "ts": tickers.get("ts"),
            "sodUtc0": tickers.get("sodUtc0"),
            "sodUtc8": tickers.get("sodUtc8")
        }
        for tickers in data["data"]
    }
    return tickers_data