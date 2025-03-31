import json

def save_exchange_info_binance(data):
    with open('exchanges_data/binance_data/chains_info.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_exchange_info_binance(data):
    exchange_info = {
        "timezone": data.get("timezone"),
        "serverTime": data.get("serverTime"),
        "symbols": [
            {
                "symbol": symbol.get("symbol"),
                "status": symbol.get("status"),
                "baseAsset": symbol.get("baseAsset"),
                "baseAssetPrecision": symbol.get("baseAssetPrecision", 0),
                "quoteAsset": symbol.get("quoteAsset"),
                "quotePrecision": symbol.get("quotePrecision", 0),
                "quoteAssetPrecision": symbol.get("quoteAssetPrecision", 0),
                "baseCommissionPrecision": symbol.get("baseCommissionPrecision", 0),
                "quoteCommissionPrecision": symbol.get("quoteCommissionPrecision", 0),
                "orderTypes": symbol.get("orderTypes"),
                "filters": [
                    {
                        "filterType": symbol.get("filterType"),
                        "minPrice": symbol.get("minPrice"),
                        "maxPrice": symbol.get("maxPrice"),
                        "tickSize": symbol.get("tickSize")
                    },
                    {
                        "filterType": symbol.get("filterType"),
                        "minQty": symbol.get("minQty"),
                        "maxQty": symbol.get("maxQty"),
                        "stepSize": symbol.get("stepSize")
                    },
                    {
                        "filterType": symbol.get("filterType"),
                        "minQty": symbol.get("minQty"),
                        "maxQty": symbol.get("maxQty"),
                        "stepSize": symbol.get("stepSize")
                    },
                    {
                        "filterType": symbol.get("filterType"),
                        "minNotional": symbol.get("minNotional"),
                        "applyMinToMarket": symbol.get("applyMinToMarket", "false").lower() == "true",
                        "maxNotional": symbol.get("maxNotional"),
                        "applyMaxToMarket": symbol.get("applyMaxToMarket", "false").lower() == "true",
                        "avgPriceMins": symbol.get("avgPriceMins", 0)
                    },
                    {
                        "filterType": symbol.get("filterType"),
                        "maxNumOrders": symbol.get("avgPriceMins", 0)
                    }
                ],
                "permissions": symbol.get("permissions"),
                "permissionSets": [
                    [group for group in symbol.get("permissionSets", [])[0] if not group.startswith("TRD_GRP_")]
                ],
                "defaultSelfTradePreventionMode": symbol.get("defaultSelfTradePreventionMode"),
                "allowedSelfTradePreventionModes": symbol.get("allowedSelfTradePreventionModes")
            }
            for symbol in data.get("symbols", [])
        ]
    }
    return exchange_info