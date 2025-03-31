import requests
from ..config.domains import HUOBI_DOMAINS
from ..config.endpoints import HUOBI_SYMBOLS_INFO_PATH, HUOBI_CURRENCIES_PATH, HUOBI_CHAINS_PATH, HUOBI_TIME_PATH, HUOBI_TICKERS_PATH

def fetch_data_from_huobi(path):
    domain = HUOBI_DOMAINS
    url = domain + path
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None

def fetch_tickers_data_huobi():
    return fetch_data_from_huobi(HUOBI_TICKERS_PATH)

def fetch_symbols_info_huobi():
    return fetch_data_from_huobi(HUOBI_SYMBOLS_INFO_PATH)

def fetch_currencies_data_huobi():
    return fetch_data_from_huobi(HUOBI_CURRENCIES_PATH)

def fetch_chains_data_huobi():
    return fetch_data_from_huobi(HUOBI_CHAINS_PATH)

def fetch_server_time_huobi():
    return fetch_data_from_huobi(HUOBI_TIME_PATH)