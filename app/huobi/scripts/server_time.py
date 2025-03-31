import json

def save_server_time_huobi(data):
    # Сохраняем данные из time в файл time.json
    with open('exchanges_data/huobi_data/time.json', 'w') as f:
        json.dump(data, f, indent=4)