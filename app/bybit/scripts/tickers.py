import json

def save_ticker_data_bybit(data):
    with open('exchanges_data/bybit_data/tickers.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_ticker_data_bybit(data):
    result = data.get("result", {})
    ticker_list = result.get("list", [])
    
    return [
        {
            "symbol": ticker.get("symbol"),
            "bid1Price": ticker.get("bid1Price", ""),
            "bid1Size": ticker.get("bid1Size", ""),
            "ask1Price": ticker.get("ask1Price", ""),
            "ask1Size": ticker.get("ask1Size", ""),
            "lastPrice": ticker.get("lastPrice", ""),
            "prevPrice24h": ticker.get("prevPrice24h", ""),
            "price24hPcnt": ticker.get("price24hPcnt", ""),
            "highPrice24h": ticker.get("highPrice24h", ""),
            "lowPrice24h": ticker.get("lowPrice24h", ""),
            "turnover24h": ticker.get("turnover24h", ""),
            "volume24h": ticker.get("volume24h", "")
        }
        for ticker in ticker_list
    ]