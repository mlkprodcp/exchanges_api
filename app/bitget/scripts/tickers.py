import json

def save_tickers_data_bitget(data):
    with open('exchanges_data/bitget_data/tickers.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_tickers_data_bitget(data):
    tickers_info = {
        "symbols": [
            {
                "symbol": symbol.get("symbol"),
                "baseCoin": symbol.get("baseCoin"),
                "quoteCoin": symbol.get("quoteCoin"),
                "minTradeAmount": symbol.get("minTradeAmount"),
                "maxTradeAmount": symbol.get("maxTradeAmount"),
                "takerFeeRate": symbol.get("takerFeeRate"),
                "makerFeeRate": symbol.get("makerFeeRate"),
                "pricePrecision": symbol.get("pricePrecision"),
                "quantityPrecision": symbol.get("quantityPrecision"),
                "quotePrecision": symbol.get("quotePrecision"),
                "status": symbol.get("status"),
                "minTradeUSDT": symbol.get("minTradeUSDT"),
                "buyLimitPriceRatio": symbol.get("buyLimitPriceRatio"),
                "sellLimitPriceRatio": symbol.get("sellLimitPriceRatio"),
                "areaSymbol": symbol.get("areaSymbol"),
                "orderQuantity": symbol.get("orderQuantity"),
                "openTime": symbol.get("openTime")
            }
            for symbol in data.get("data", [])
        ]
    }
    return tickers_info