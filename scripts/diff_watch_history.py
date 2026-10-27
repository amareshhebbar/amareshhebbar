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


def merge_repo_days(repo_log, views_daily):
    new_days = {}
    delta_count = 0
    delta_uniques = 0
    for entry in views_daily:
        date = entry.get("timestamp", "")[:10]
        if not date:
            continue
        count = entry.get("count", 0)
        uniques = entry.get("uniques", 0)
        old = repo_log.get(date, {"count": 0, "uniques": 0})
        dc = max(count - old["count"], 0)
        du = max(uniques - old["uniques"], 0)
        if dc or du:
            new_days[date] = {"count": dc, "uniques": du}
            delta_count += dc
            delta_uniques += du
        repo_log[date] = {
            "count": max(count, old["count"]),
            "uniques": max(uniques, old["uniques"])
        }
    return new_days, delta_count, delta_uniques


def main():
    raw = load_json(RAW_PATH, None)
    if raw is None:
        raise RuntimeError("watch_raw.json missing, run fetch_watch_traffic.py first")

    prev_watchers_state = load_json(STATE_PATH, {})
    history = load_json(HISTORY_PATH, [])
    daily_log = load_json(DAILY_LOG_PATH, {})

    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")

    entry_repos = {}
    totals = {
        "watchers_total": 0,
        "watchers_new": 0,
        "views_today_count": 0,
        "views_today_uniques": 0,
        "views_yesterday_count": 0,
        "views_yesterday_uniques": 0,
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

        repo_log = daily_log.setdefault(repo, {})
        if data.get("traffic_ok", True):
            new_days, delta_count, delta_uniques = merge_repo_days(repo_log, data["views_daily"])
        else:
            new_days, delta_count, delta_uniques = {}, 0, 0

        today_vals = repo_log.get(today, {"count": 0, "uniques": 0})
        yesterday_vals = repo_log.get(yesterday, {"count": 0, "uniques": 0})

        entry_repos[repo] = {
            "watchers_total": len(current_watchers),
            "watchers_new": new_watchers,
            "views_today_count": today_vals["count"],
            "views_today_uniques": today_vals["uniques"],
            "views_yesterday_count": yesterday_vals["count"],
            "views_yesterday_uniques": yesterday_vals["uniques"],
            "views_delta_count": delta_count,
            "views_delta_uniques": delta_uniques,
            "views_new_days": new_days,
            "views_total_14d": data["views_count_total"],
            "views_uniques_14d": data["views_uniques_total"],
            "traffic_ok": data.get("traffic_ok", True)
        }

        totals["watchers_total"] += len(current_watchers)
        totals["watchers_new"] += len(new_watchers)
        totals["views_today_count"] += today_vals["count"]
        totals["views_today_uniques"] += today_vals["uniques"]
        totals["views_yesterday_count"] += yesterday_vals["count"]
        totals["views_yesterday_uniques"] += yesterday_vals["uniques"]
        totals["views_delta_count"] += delta_count
        totals["views_delta_uniques"] += delta_uniques
        totals["views_total_14d"] += data["views_count_total"]
        totals["views_uniques_14d"] += data["views_uniques_total"]

    cutoff_date = (now - timedelta(days=DAILY_LOG_RETENTION_DAYS)).strftime("%Y-%m-%d")
    for repo in daily_log:
        daily_log[repo] = {d: v for d, v in sorted(daily_log[repo].items()) if d >= cutoff_date}

    history.append({
        "timestamp": raw["timestamp"],
        "repos": entry_repos,
        "totals": totals
    })
    history = history[-MAX_HISTORY_ENTRIES:]

    os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)
    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, indent=2)
    with open(STATE_PATH, "w") as f:
        json.dump(new_watchers_state, f, indent=2)
    with open(DAILY_LOG_PATH, "w") as f:
        json.dump(daily_log, f, indent=2)

    print(f"new views since last run: {totals['views_delta_count']} ({totals['views_delta_uniques']} unique)")


if __name__ == "__main__":
    main()