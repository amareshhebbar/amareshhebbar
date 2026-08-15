import os
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

from gh_client import run_query
from cache_manager import load_cache, save_cache, upsert_month

CACHE_PATH = "data/stats_cache.json"

MONTH_QUERY = """
query($from: DateTime!, $to: DateTime!) {
  viewer {
    createdAt
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
      totalIssueContributions
      restrictedContributionsCount
    }
  }
}
"""


def month_bounds(year, month):
    start = datetime(year, month, 1, tzinfo=timezone.utc)
    end = start + relativedelta(months=1)
    return start, end


def month_key(dt):
    return dt.strftime("%Y-%m")


def fetch_month(token, year, month):
    start, end = month_bounds(year, month)
    data = run_query(token, MONTH_QUERY, {
        "from": start.isoformat(),
        "to": end.isoformat()
    })
    viewer = data["data"]["viewer"]
    cc = viewer["contributionsCollection"]
    entry = {
        "month": month_key(start),
        "commits": cc["totalCommitContributions"],
        "prs": cc["totalPullRequestContributions"],
        "reviews": cc["totalPullRequestReviewContributions"],
        "issues": cc["totalIssueContributions"],
        "restricted": cc["restrictedContributionsCount"]
    }
    return viewer["createdAt"], entry


def months_between(start_dt, end_dt):
    cur = datetime(start_dt.year, start_dt.month, 1, tzinfo=timezone.utc)
    out = []
    while cur <= end_dt:
        out.append((cur.year, cur.month))
        cur += relativedelta(months=1)
    return out


def main():
    token = os.environ["STATS_TOKEN"]
    cache = load_cache(CACHE_PATH)
    now = datetime.now(timezone.utc)

    if not cache:
        created_at_str, _ = fetch_month(token, now.year, now.month)
        created_at = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
        targets = months_between(created_at, now)
    else:
        prev = now - relativedelta(months=1)
        targets = [(prev.year, prev.month), (now.year, now.month)]

    for year, month in targets:
        _, entry = fetch_month(token, year, month)
        upsert_month(cache, entry)
        print(f"synced {entry['month']}: commits={entry['commits']} prs={entry['prs']}")

    save_cache(CACHE_PATH, cache)


if __name__ == "__main__":
    main()