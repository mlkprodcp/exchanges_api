from fastapi import FastAPI
import asyncio
from contextlib import asynccontextmanager

from .requests.chains_info import fetch_chains_info
from .requests.tickers import fetch_tickers_data
from .requests.server_time import fetch_server_time
from .requests.currencies import fetch_currencies_data
from .requests.symbols import fetch_symbols_info

from .api.chains_info import router as chains_info_router
from .api.tickers import router as tickers_router
from .api.server_time import router as server_time_router
from .api.currencies import router as currencies_router
from .api.symbols import router as symbols_info_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    task_symbols_info = asyncio.create_task(fetch_symbols_info())
    task_tickers_data = asyncio.create_task(fetch_tickers_data())
    task_currencies_data = asyncio.create_task(fetch_currencies_data())
    task_server_time = asyncio.create_task(fetch_server_time())
    task_chains_info = asyncio.create_task(fetch_chains_info())

    yield

    task_symbols_info.cancel()
    task_tickers_data.cancel()
    task_currencies_data.cancel()
    task_server_time.cancel()
    task_chains_info.cancel()

app = FastAPI(lifespan=lifespan)

app.include_router(symbols_info_router)
app.include_router(tickers_router)
app.include_router(currencies_router)
app.include_router(server_time_router)
app.include_router(chains_info_router)