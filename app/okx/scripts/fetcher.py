import requests
from ..config.domains import OKX_DOMAINS
from ..config.endpoints import OKX_TICKERS_PATH, OKX_TIME_PATH
from ..config.keys import OKX_API_KEY, OKX_SECRET_KEY, OKX_PASSPHRASE
import okx.Funding as Funding

# API initialization
apikey = OKX_API_KEY
secretkey = OKX_SECRET_KEY
passphrase = OKX_PASSPHRASE

flag = "0"

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
result = fundingAPI.get_currencies()

def fetch_data_from_okx(path):
    domain = OKX_DOMAINS
    url = domain + path
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None
    
def fetch_chains_info_okx():
    return result

def fetch_ticker_data_okx():
    return fetch_data_from_okx(OKX_TICKERS_PATH)

def fetch_server_time_okx():
    return fetch_data_from_okx(OKX_TIME_PATH)