import json

def save_server_time_binance(data):
    with open('exchanges_data/binance_data/time.json', 'w') as f:
        json.dump(data, f, indent=4)