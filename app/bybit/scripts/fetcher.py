import requests
from ..config.domains import BYBIT_DOMAINS
from ..config.endpoints import BYBIT_TICKERS_PATH, BYBIT_TIME_PATH, BYBIT_INSTRUMENTS_PATH#, BYBIT_CHAINS_PATH

def fetch_data_from_bybit(path):
    domain = BYBIT_DOMAINS
    url = domain + path
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None
    
"""def fetch_coins_info_bybit():
    return fetch_coins_info_bybit(BYBIT_CHAINS_PATH)
    """
def fetch_instruments_info_bybit():
    return fetch_data_from_bybit(BYBIT_INSTRUMENTS_PATH)

def fetch_tickers_data_bybit():
    return fetch_data_from_bybit(BYBIT_TICKERS_PATH)

def fetch_server_time_bybit():
    return fetch_data_from_bybit(BYBIT_TIME_PATH)