from fastapi import FastAPI
import asyncio
from contextlib import asynccontextmanager

from .requests.chains_info import fetch_coins_info
from .requests.tickers import fetch_tickers_data
from .requests.server_time import fetch_server_time

from .api.chains_info import router as chains_info_router
from .api.tickers import router as tickers_router
from .api.server_time import router as server_time_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    task_coins_info = asyncio.create_task(fetch_coins_info())
    task_tickers_data = asyncio.create_task(fetch_tickers_data())
    task_server_time = asyncio.create_task(fetch_server_time())

    yield

    task_coins_info.cancel()
    task_tickers_data.cancel()
    task_server_time.cancel()

app = FastAPI(lifespan=lifespan)

app.include_router(chains_info_router)
app.include_router(tickers_router)
app.include_router(server_time_router)