import json

def save_server_time_bybit(data):
    with open('exchanges_data/bybit_data/time.json', 'w') as f:
        json.dump(data, f, indent=4)