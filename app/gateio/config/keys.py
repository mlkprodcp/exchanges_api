import os
from dotenv import load_dotenv

load_dotenv()

GATEIO_API_KEY = os.getenv("GATEIO_API_KEY", "")
GATEIO_SECRET_KEY = os.getenv("GATEIO_SECRET_KEY", "")