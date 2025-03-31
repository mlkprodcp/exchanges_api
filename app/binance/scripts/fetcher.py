import requests
from ..config.domains import BINANCE_DOMAINS
from ..config.endpoints import BINANCE_EXCHANGE_INFO_PATH, BINANCE_TICKERS_PATH, BINANCE_TIME_PATH

def fetch_data_from_binance(path):
    domain = BINANCE_DOMAINS
    url = domain + path
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None

def fetch_exchange_info_binance():
    return fetch_data_from_binance(BINANCE_EXCHANGE_INFO_PATH)

def fetch_ticker_data_binance():
    return fetch_data_from_binance(BINANCE_TICKERS_PATH)

def fetch_server_time_binance():
    return fetch_data_from_binance(BINANCE_TIME_PATH)