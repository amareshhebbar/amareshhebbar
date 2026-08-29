import os
import time
import json
import requests
from datetime import datetime, timezone

API_ROOT = "https://api.github.com"
OUT_PATH = "data/watch_raw.json"


def gh_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def paginated_get(url, headers, params=None):
    items = []
    params = dict(params or {})
    params["per_page"] = 100
    page = 1
    while True:
        params["page"] = page
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return items


def get_authenticated_login(token):
    headers = gh_headers(token)
    resp = requests.get(f"{API_ROOT}/user", headers=headers)
    resp.raise_for_status()
    return resp.json()["login"]


def list_owned_public_repos(token, owner):
    headers = gh_headers(token)
    repos = paginated_get(f"{API_ROOT}/user/repos", headers, {"affiliation": "owner"})
    return [r["name"] for r in repos if r["owner"]["login"] == owner and not r["private"]]


def fetch_subscribers(token, owner, repo, exclude_login):
    headers = gh_headers(token)
    try:
        subs = paginated_get(f"{API_ROOT}/repos/{owner}/{repo}/subscribers", headers)
        return [s["login"] for s in subs if s["login"] != exclude_login]
    except requests.exceptions.HTTPError:
        return []


def fetch_traffic_views(token, owner, repo):
    headers = gh_headers(token)
    resp = requests.get(f"{API_ROOT}/repos/{owner}/{repo}/traffic/views", headers=headers)
    if resp.status_code != 200:
        return {"count": 0, "uniques": 0, "views": []}
    data = resp.json()
    return {
        "count": data.get("count", 0),
        "uniques": data.get("uniques", 0),
        "views": data.get("views", [])
    }


def main():
    token = os.environ["STATS_TOKEN"]
    owner = get_authenticated_login(token)
    repo_names = list_owned_public_repos(token, owner)

    snapshot = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "repos": {}
    }

    for name in repo_names:
        watchers = fetch_subscribers(token, owner, name, owner)
        traffic = fetch_traffic_views(token, owner, name)
        snapshot["repos"][name] = {
            "watchers": watchers,
            "views_count_total": traffic["count"],
            "views_uniques_total": traffic["uniques"],
            "views_daily": traffic["views"]
        }
        print(f"{name}: watchers={len(watchers)} views_total={traffic['count']} uniques_total={traffic['uniques']}")
        time.sleep(0.3)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(snapshot, f, indent=2)


if __name__ == "__main__":
    main()