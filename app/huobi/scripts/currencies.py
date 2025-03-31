import json

def save_currencies_data_huobi(data):
    with open('exchanges_data/huobi_data/currencies.json', 'w') as f:
        json.dump(data, f, indent=4)


def extract_currencies_data_huobi(data):
    currencies_data = {
        "status": data.get("status"),
        "data": [
            {
                "tags": item.get("tags"),
                "cawt": item.get("cawt"),
                "fc": item.get("fc"),
                "sc": item.get("sc"),
                "de": item.get("de"),
                "wed": item.get("wed"),
                "cd": item.get("cd"),
                "qc": item.get("qc"),
                "wp": item.get("wp"),
                "fn": item.get("fn"),
                "cc": item.get("cc"),
                "sp": item.get("sp"),
                "at": item.get("at"),
                "w": item.get("w"),
                "dma": item.get("dma"),
                "wma": item.get("wma"),
                "ft": item.get("ft"),
                "v": item.get("v"),
                "whe": item.get("whe"),
                "state": item.get("state"),
                "dn": item.get("dn"),
                "svd": item.get("svd"),
                "swd": item.get("swd"),
                "sdd": item.get("sdd"),
                "wd": item.get("wd")
            }
            for item in data.get("data", [])
        ],
        "ts": data.get("ts"),
        "full": data.get("full")
    }
    return currencies_data