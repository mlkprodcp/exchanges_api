import json

def save_coins_info_bitget(data):
    with open('exchanges_data/bitget_data/chains_info.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_coins_info_bitget(data):
    coins_info = {
        "coins": [
            {
                "coin": coin.get("coin"),
                "transfer": coin.get("transfer"),
                "chains": [
                    {
                        "chain": chain.get("chain"),
                        "withdrawable": chain.get("withdrawable"),
                        "rechargeable": chain.get("rechargeable"),
                        "withdrawFee": chain.get("withdrawFee"),
                        "extraWithdrawFee": chain.get("extraWithdrawFee"),
                        "depositConfirm": chain.get("depositConfirm"),
                        "withdrawConfirm": chain.get("withdrawConfirm"),
                        "minDepositAmount": chain.get("minDepositAmount"),
                        "minWithdrawAmount": chain.get("minWithdrawAmount"),
                        "browserUrl": chain.get("browserUrl"),
                        "contractAddress": chain.get("contractAddress"),
                        "withdrawStep": chain.get("withdrawStep"),
                        "withdrawMinScale": chain.get("withdrawMinScale"),
                        "congestion": chain.get("congestion")
                    }
                    for chain in coin.get("chains", [])
                ],
                "areaCoin": coin.get("areaCoin")
            }
            for coin in data.get("data", [])
        ]
    }
    return coins_info