import json

def save_server_time_bitget(data):
    with open('exchanges_data/bitget_data/time.json', 'w') as f:
        json.dump(data, f, indent=4)