import json

def save_ticker_data_gateio(data):
    # Сохраняем данные из ticker/24hr в файл tickers.json
    with open('exchanges_data/gateio_data/tickers.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_ticker_data_gateio(data):
    tickers_data = [
        {
            "currency_pair": pair.get("currency_pair"),
            "last_price": pair.get("last"),
            "lowest_ask": pair.get("lowest_ask"),
            "highest_bid": pair.get("highest_bid"),
            "change_percentage": pair.get("change_percentage"),
            "change_utc0": pair.get("change_utc0"),
            "change_utc8": pair.get("change_utc8"),
            "base_volume": pair.get("base_volume"),
            "quote_volume": pair.get("quote_volume"),
            "high_24h": pair.get("high_24h"),
            "low_24h": pair.get("low_24h")
        }
        for pair in data
    ]
    
    return tickers_data