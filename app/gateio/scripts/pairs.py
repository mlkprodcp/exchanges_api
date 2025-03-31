import json

def save_pair_info_gateio(data):
    with open('exchanges_data/gateio_data/pairs.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_trade_pair_info_gateio(data):
    trade_pair_info = [
        {
            "id": pair.get("id"),
            "base_currency": pair.get("base"),
            "base_name": pair.get("base_name"),
            "quote_currency": pair.get("quote"),
            "quote_name": pair.get("quote_name"),
            "fee": pair.get("fee"),
            "min_base_amount": pair.get("min_base_amount"),
            "min_quote_amount": pair.get("min_quote_amount"),
            "max_base_amount": pair.get("max_base_amount"),
            "max_quote_amount": pair.get("max_quote_amount"),
            "amount_precision": pair.get("amount_precision"),
            "precision": pair.get("precision"),
            "trade_status": pair.get("trade_status"),
            "sell_start": pair.get("sell_start"),
            "buy_start": pair.get("buy_start"),
            "type": pair.get("type")
        }
        for pair in data
    ]
    
    return trade_pair_info