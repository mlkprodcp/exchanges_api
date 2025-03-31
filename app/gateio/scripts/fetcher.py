import requests
from ..config.domains import GATEIO_DOMAINS
from ..config.endpoints import GATEIO_TICKERS_PATH, GATEIO_PAIRS_PATH, GATEIO_EXCHANGE_INFO_PATH, GATEIO_TIME_PATH

def fetch_data_from_gateio(path, params=None):
    domain = GATEIO_DOMAINS
    url = f"{domain}{path}"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None
    
def fetch_server_time_gateio():
    return fetch_data_from_gateio(GATEIO_TIME_PATH)

def fetch_tickers_data_gateio():
    return fetch_data_from_gateio(GATEIO_TICKERS_PATH)

def fetch_pairs_gateio():
    return fetch_data_from_gateio(GATEIO_PAIRS_PATH)

def fetch_exchange_info_gateio():
    return fetch_data_from_gateio(GATEIO_EXCHANGE_INFO_PATH)
