"""import json
from pybit.unified_trading import HTTP
from ..config.keys import BYBIT_API_KEY, BYBIT_SECRET_KEY

# Инициализация сессии Bybit
session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_SECRET_KEY,
)

def save_coins_info_bybit(data):
    with open('exchanges_data/bybit_data/chains_info.json', 'w') as f:
        json.dump(data, f, indent=4)

def fetch_coins_info_bybit(coin):
    try:
        response = session.get_coin_info(coin=coin)
        return response
    except Exception as e:
        print(f"Ошибка при запросе информации о монете {coin}: {e}")
        return None
"""