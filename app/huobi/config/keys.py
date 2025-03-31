import os
from dotenv import load_dotenv

load_dotenv()

HUOBI_API_KEY = os.getenv("HUOBI_API_KEY", "")
HUOBI_SECRET_KEY = os.getenv("HUOBI_SECRET_KEY", "")