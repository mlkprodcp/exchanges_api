import json

def save_tickers_data_huobi(data):
    with open('exchanges_data/huobi_data/tickers.json', 'w') as f:
        json.dump(data, f, indent=4)


def extract_tickers_data_huobi(data):
    tickers_data = {
        tickers["symbol"]: {
            "symbol": tickers.get("symbol"),
            "open": tickers.get("open"),
            "high": tickers.get("high"),
            "low": tickers.get("low"),
            "close": tickers.get("close"),
            "amount": tickers.get("amount"),
            "vol": tickers.get("vol"),
            "count": tickers.get("count"),
            "bid": tickers.get("bid"),
            "bidSize": tickers.get("bidSize"),
            "ask": tickers.get("ask"),
            "askSize": tickers.get("askSize")
        }
        for tickers in data["data"]
    }
    return tickers_data