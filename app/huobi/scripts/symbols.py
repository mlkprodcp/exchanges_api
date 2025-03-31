import json

def save_symbols_info_huobi(data):

    with open('exchanges_data/huobi_data/symbols.json', 'w') as f:
        json.dump(data, f, indent=4)

def extract_symbols_info_huobi(data):
    symbols_info = {
        "status": data.get("status"),
        "data": [
            {
                "tags": item.get("tags"),
                "state": item.get("state"),
                "wr": item.get("wr"),
                "p1": item.get("p1"),
                "sm": item.get("sm"),
                "tpp": item.get("tpp"),
                "tap": item.get("tap"),
                "ttp": item.get("ttp"),
                "bcdn": item.get("bcdn"),
                "qcdn": item.get("qcdn"),
                "elr": item.get("elr"),
                "si": item.get("si"),
                "scr": item.get("scr"),
                "bc": item.get("bc"),
                "smlr": item.get("smlr"),
                "qc": item.get("qc"),
                "flr": item.get("flr"),
                "mbph": item.get("mbph"),
                "mspl": item.get("mspl"),
                "lr": item.get("lr"),
                "toa": item.get("toa"),
                "sc": item.get("sc"),
                "sp": item.get("sp"),
                "d": item.get("d"),
                "w": item.get("w"),
                "whe": item.get("whe"),
                "fp": item.get("fp"),
                "cd": item.get("cd"),
                "te": item.get("te"),
                "dn": item.get("dn"),
                "suspend_desc": item.get("suspend_desc")
            }
            for item in data.get("data", [])
        ],
        "ts": data.get("ts"),
        "full": data.get("full")
    }
    return symbols_info