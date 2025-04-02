import json

def save_server_time_mexc(data):
    with open('exchanges_data/mexc_data/time.json', 'w') as f:
        json.dump(data, f, indent=4)