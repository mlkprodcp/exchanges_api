import json

def save_symbols_data_mexc(data):
    with open('exchanges_data/mexc_data/symbols.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_symbols_info_mexc(data):
    symbols_info = {
        "data": [
            {
                "symbol": item.get("symbol"),
                "state": item.get("state"),
                "full_name": item.get("fullName"),
                "trade_side_type": item.get("tradeSideType"),
                "price_scale": item.get("price_scale"),
                "quantity_scale": item.get("quantity_scale"),
                "min_amount": item.get("min_amount"),
                "max_amount": item.get("max_amount"),
                "maker_fee_rate": item.get("maker_fee_rate"),
                "taker_fee_rate": item.get("taker_fee_rate"),
                "limited": item.get("limited"),
                "etf_mark": item.get("etf_mark"),
                "symbol_partition": item.get("symbol_partition"),
                "max_amount_market": item.get("max_amount_market"),
                "min_amount_market": item.get("min_amount_market")
            }
            for item in data.get("data", [])
        ]
    }
    return symbols_info
