import json
import os


def load_cache(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_cache(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = sorted(data, key=lambda x: x["month"])
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def upsert_month(cache, entry):
    for i, item in enumerate(cache):
        if item["month"] == entry["month"]:
            cache[i] = entry
            return
    cache.append(entry)