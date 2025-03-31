import requests
from ..config.domains import BITGET_DOMAINS
from ..config.endpoints import BITGET_COINS_PATH, BITGET_TICKERS_PATH, BITGET_TIME_PATH

def fetch_data_from_bitget(path):
    domain = BITGET_DOMAINS
    url = domain + path
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None

def fetch_coins_info_bitget():
    return fetch_data_from_bitget(BITGET_COINS_PATH)

def fetch_tickers_data_bitget():
    return fetch_data_from_bitget(BITGET_TICKERS_PATH)

def fetch_server_time_bitget():
    return fetch_data_from_bitget(BITGET_TIME_PATH)