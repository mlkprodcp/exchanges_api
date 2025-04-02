import uvicorn
import multiprocessing
from app.binance.server import app as binance_app
from app.bitget.server import app as bitget_app
from app.bybit.server import app as bybit_app
from app.gateio.server import app as gateio_app
from app.huobi.server import app as huobi_app
from app.mexc.server import app as mexc_app
from app.okx.server import app as okx_app

def run_binance():
    uvicorn.run(binance_app, host="0.0.0.0", port=8000)

def run_bitget():
    uvicorn.run(bitget_app, host="0.0.0.0", port=8001)

def run_bybit():
    uvicorn.run(bybit_app, host="0.0.0.0", port=8002)

def run_gateio():
    uvicorn.run(gateio_app, host="0.0.0.0", port=8003)

def run_huobi():
    uvicorn.run(huobi_app, host="0.0.0.0", port=8004)

def run_mexc():
    uvicorn.run(mexc_app, host="0.0.0.0", port=8005)

def run_okx():
    uvicorn.run(okx_app, host="0.0.0.0", port=8006)

if __name__ == "__main__":
    binance_process = multiprocessing.Process(target=run_binance)
    bitget_process = multiprocessing.Process(target=run_bitget)
    bybit_process = multiprocessing.Process(target=run_bybit)
    gateio_process = multiprocessing.Process(target=run_gateio)
    huobi_process = multiprocessing.Process(target=run_huobi)
    mexc_process = multiprocessing.Process(target=run_mexc)
    okx_process = multiprocessing.Process(target=run_okx)

    binance_process.start()
    bitget_process.start()
    bybit_process.start()
    gateio_process.start()
    huobi_process.start()
    mexc_process.start()
    okx_process.start()

    binance_process.join()
    bitget_process.join()
    bybit_process.join()
    gateio_process.join()
    huobi_process.join()
    mexc_process.join()
    okx_process.join()