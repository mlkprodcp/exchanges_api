import json

def save_server_time_gateio(data):
    with open('exchanges_data/gateio_data/time.json', 'w') as f:
        json.dump(data, f, indent=4)