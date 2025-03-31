import json

def save_exchange_info_gateio(data):
    with open('exchanges_data/gateio_data/chains_info.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_exchange_info_gateio(data):
    exchange_info = [
        {
            "currency": currency.get("currency"),
            "name": currency.get("name"),
            "delisted": currency.get("delisted"),
            "withdraw_disabled": currency.get("withdraw_disabled"),
            "withdraw_delayed": currency.get("withdraw_delayed"),
            "deposit_disabled": currency.get("deposit_disabled"),
            "trade_disabled": currency.get("trade_disabled"),
            "fixed_rate": currency.get("fixed_rate"),
            "chain": currency.get("chain"),
            "chains": [
                {
                    "name": chain.get("name"),
                    "addr": chain.get("addr"),
                    "withdraw_disabled": chain.get("withdraw_disabled"),
                    "withdraw_delayed": chain.get("withdraw_delayed"),
                    "deposit_disabled": chain.get("deposit_disabled")
                }
                for chain in currency.get("chains", [])
            ]
        }
        for currency in data
    ]
    
    return exchange_info