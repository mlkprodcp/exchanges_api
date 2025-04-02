import json

def save_chains_info_mexc(data):
    with open('exchanges_data/mexc_data/chains_info.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_chains_info_mexc(data):
    chains_info = {
        "data": [
            {
                "currency": item.get("currency"),
                "full_name": item.get("full_name"),
                "coins": [
                    {
                        "chain": coin.get("chain"),
                        "precision": coin.get("precision"),
                        "fee": coin.get("fee"),
                        "is_withdraw_enabled": coin.get("is_withdraw_enabled"),
                        "is_deposit_enabled": coin.get("is_deposit_enabled"),
                        "deposit_min_confirm": coin.get("deposit_min_confirm"),
                        "withdraw_limit_max": coin.get("withdraw_limit_max"),
                        "withdraw_limit_min": coin.get("withdraw_limit_min")
                    }
                    for coin in item.get("coins", [])
                ]
            }
            for item in data.get("data", [])
        ]
    }
    return chains_info