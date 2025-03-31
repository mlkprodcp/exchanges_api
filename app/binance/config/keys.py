import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY", "")

client_binance = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)