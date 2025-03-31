import json

def save_chains_info_huobi(data):
    with open('exchanges_data/huobi_data/chains_info.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_chains_info_huobi(data):
    chains_info = {
        "status": data.get("code"),
        "data": [
            {
                "currency": item.get("currency"),
                "assetType": item.get("assetType"),
                "chains": [
                    {
                        "chain": chain.get("chain"),
                        "displayName": chain.get("displayName"),
                        "fullName": chain.get("fullName"),
                        "baseChain": chain.get("baseChain"),
                        "baseChainProtocol": chain.get("baseChainProtocol"),
                        "isDynamic": chain.get("isDynamic"),
                        "numOfConfirmations": chain.get("numOfConfirmations"),
                        "numOfFastConfirmations": chain.get("numOfFastConfirmations"),
                        "depositStatus": chain.get("depositStatus"),
                        "minDepositAmt": chain.get("minDepositAmt"),
                        "withdrawStatus": chain.get("withdrawStatus"),
                        "minWithdrawAmt": chain.get("minWithdrawAmt"),
                        "withdrawPrecision": chain.get("withdrawPrecision"),
                        "maxWithdrawAmt": chain.get("maxWithdrawAmt"),
                        "withdrawQuotaPerDay": chain.get("withdrawQuotaPerDay"),
                        "withdrawQuotaPerYear": chain.get("withdrawQuotaPerYear"),
                        "withdrawQuotaTotal": chain.get("withdrawQuotaTotal"),
                        "withdrawFeeType": chain.get("withdrawFeeType"),
                        "transactFeeWithdraw": chain.get("transactFeeWithdraw"),
                        "addrWithTag": chain.get("addrWithTag"),
                        "addrDepositTag": chain.get("addrDepositTag")
                    }
                    for chain in item.get("chains", [])
                ],
                "instStatus": item.get("instStatus")
            }
            for item in data.get("data", [])
        ],
        "ts": data.get("ts"),
        "full": data.get("full")
    }
    return chains_info