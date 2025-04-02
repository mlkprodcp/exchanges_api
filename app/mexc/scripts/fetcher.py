import requests
from ..config.domains import MEXC_DOMAINS
from ..config.endpoints import MEXC_CHAINS_PATH, MEXC_TICKERS_PATH, MEXC_SYMBOLS_PATH, MEXC_TIME_PATH

def fetch_data_from_mexc(path):
    domain = MEXC_DOMAINS
    url = domain + path
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None

def fetch_chains_info_mexc():
    return fetch_data_from_mexc(MEXC_CHAINS_PATH)

def fetch_ticker_data_mexc():
    return fetch_data_from_mexc(MEXC_TICKERS_PATH)

def fetch_symbols_data_mexc():
    return fetch_data_from_mexc(MEXC_SYMBOLS_PATH)

def fetch_server_time_mexc():
    return fetch_data_from_mexc(MEXC_TIME_PATH)