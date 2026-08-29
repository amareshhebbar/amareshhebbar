import os
import json
from datetime import datetime, timezone, timedelta

RAW_PATH = "data/watch_raw.json"
STATE_PATH = "data/watchers_state.json"
HISTORY_PATH = "data/watch_history.json"
DAILY_LOG_PATH = "data/views_daily_log.json"
MAX_HISTORY_ENTRIES = 200
DAILY_LOG_RETENTION_DAYS = 400


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        content = f.read().strip()
    if not content:
        return default
    return json.loads(content)


def today_key(iso_timestamp):
    return iso_timestamp[:10]


def find_today_entry(views_daily, today):
    for entry in views_daily:
        if entry.get("timestamp", "")[:10] == today:
            return entry
    return None


def main():
    raw = load_json(RAW_PATH, None)
    if raw is None:
        raise RuntimeError("watch_raw.json missing, run fetch_watch_traffic.py first")

    prev_watchers_state = load_json(STATE_PATH, {})
    history = load_json(HISTORY_PATH, [])
    daily_log = load_json(DAILY_LOG_PATH, {})
    last_entry = history[-1] if history else None

    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    entry_repos = {}
    totals = {
        "watchers_total": 0,
        "watchers_new": 0,
        "views_today_count": 0,
        "views_today_uniques": 0,
        "views_delta_count": 0,
        "views_delta_uniques": 0,
        "views_total_14d": 0,
        "views_uniques_14d": 0
    }

    new_watchers_state = {}

    for repo, data in raw["repos"].items():
        current_watchers = set(data["watchers"])
        previous_watchers = set(prev_watchers_state.get(repo, []))
        new_watchers = sorted(current_watchers - previous_watchers)
        new_watchers_state[repo] = sorted(current_watchers)

        today_entry = find_today_entry(data["views_daily"], today)
        views_today_count = today_entry["count"] if today_entry else 0
        views_today_uniques = today_entry["uniques"] if today_entry else 0

        prev_repo_entry = None
        if last_entry and today_key(last_entry["timestamp"]) == today:
            prev_repo_entry = last_entry["repos"].get(repo)

        if prev_repo_entry:
            views_delta_count = max(views_today_count - prev_repo_entry["views_today_count"], 0)
            views_delta_uniques = max(views_today_uniques - prev_repo_entry["views_today_uniques"], 0)
        else:
            views_delta_count = views_today_count
            views_delta_uniques = views_today_uniques

        entry_repos[repo] = {
            "watchers_total": len(current_watchers),
            "watchers_new": new_watchers,
            "views_today_count": views_today_count,
            "views_today_uniques": views_today_uniques,
            "views_delta_count": views_delta_count,
            "views_delta_uniques": views_delta_uniques,
            "views_total_14d": data["views_count_total"],
            "views_uniques_14d": data["views_uniques_total"]
        }

        totals["watchers_total"] += len(current_watchers)
        totals["watchers_new"] += len(new_watchers)
        totals["views_today_count"] += views_today_count
        totals["views_today_uniques"] += views_today_uniques
        totals["views_delta_count"] += views_delta_count
        totals["views_delta_uniques"] += views_delta_uniques
        totals["views_total_14d"] += data["views_count_total"]
        totals["views_uniques_14d"] += data["views_uniques_total"]

        repo_log = daily_log.setdefault(repo, {})
        for date_entry in data["views_daily"]:
            date = date_entry.get("timestamp", "")[:10]
            if date:
                repo_log[date] = {
                    "count": date_entry.get("count", 0),
                    "uniques": date_entry.get("uniques", 0)
                }

    cutoff_date = (now - timedelta(days=DAILY_LOG_RETENTION_DAYS)).strftime("%Y-%m-%d")
    for repo in daily_log:
        daily_log[repo] = {d: v for d, v in daily_log[repo].items() if d >= cutoff_date}

    new_entry = {
        "timestamp": raw["timestamp"],
        "repos": entry_repos,
        "totals": totals
    }

    history.append(new_entry)
    history = history[-MAX_HISTORY_ENTRIES:]

    os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)
    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, indent=2)
    with open(STATE_PATH, "w") as f:
        json.dump(new_watchers_state, f, indent=2)
    with open(DAILY_LOG_PATH, "w") as f:
        json.dump(daily_log, f, indent=2)


if __name__ == "__main__":
    main()