import json

def save_server_time_okx(data):
    with open('exchanges_data/okx_data/time.json', 'w') as f:
        json.dump(data, f, indent=4)