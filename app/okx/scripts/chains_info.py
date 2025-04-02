import json

def save_chains_info_okx(data):
    with open('exchanges_data/okx_data/chains_info.json', 'w') as f:
        json.dump(data, f, indent=4)