import json
from ..config.keys import client_binance

def save_ticker_data_binance(data):
    # Сохраняем данные из ticker/24hr в файл tickers.json
    with open('exchanges_data/binance_data/tickers.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_ticker_data_binance(data):
    # Извлекаем нужные данные из ответа
    result = []

    # Получаем информацию о всех монетах
    all_coins = client_binance.get_all_coins_info()

    def find_coin_info(coin):
        for c in all_coins:
            if c["coin"] == coin:
                return c
        return None

    for ticker in data:
        symbol = ticker.get("symbol")
        
        if not symbol:  # Если symbol отсутствует, пропускаем текущий элемент
            continue

        # Извлекаем base_coin и quote_coin
        if len(symbol) > 4:
            base_coin = symbol[:-4]
            quote_coin = symbol[-4:]
        else:
            base_coin = symbol
            quote_coin = ""

        # Получаем информацию о базовой и котируемой монетах
        base_asset_info = find_coin_info(base_coin)
        quote_asset_info = find_coin_info(quote_coin) if quote_coin else None

        # Добавляем информацию в результат
        result.append({
            "symbol": symbol,
            "priceChange": ticker.get("priceChange"),
            "lastPrice": ticker.get("lastPrice"),
            "lastQty": ticker.get("lastQty"),
            "bidPrice": ticker.get("bidPrice"),
            "bidQty": ticker.get("bidQty"),
            "askPrice": ticker.get("askPrice"),
            "askQty": ticker.get("askQty"),
            "coin_info": {
                "base_asset_info": base_asset_info,
                "quote_asset_info": quote_asset_info
            }
        })
    
    return result