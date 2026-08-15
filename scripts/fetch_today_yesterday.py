import os
import json
from datetime import datetime, timedelta, timezone

from gh_client import run_query

OUT_PATH = "data/daily_activity.json"

QUERY = """
query($from: DateTime!, $to: DateTime!) {
  viewer {
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      totalPullRequestContributions
    }
  }
}
"""


def day_bounds(date):
    start = datetime(date.year, date.month, date.day, tzinfo=timezone.utc)
    end = start + timedelta(days=1)
    return start, end


def fetch_day(token, date):
    start, end = day_bounds(date)
    data = run_query(token, QUERY, {
        "from": start.isoformat(),
        "to": end.isoformat()
    })
    cc = data["data"]["viewer"]["contributionsCollection"]
    return {
        "date": start.strftime("%Y-%m-%d"),
        "commits": cc["totalCommitContributions"],
        "prs": cc["totalPullRequestContributions"]
    }


def main():
    token = os.environ["STATS_TOKEN"]
    now = datetime.now(timezone.utc)
    today = fetch_day(token, now)
    yesterday = fetch_day(token, now - timedelta(days=1))

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump({"today": today, "yesterday": yesterday}, f, indent=2)

    print(f"today: commits={today['commits']} prs={today['prs']}")
    print(f"yesterday: commits={yesterday['commits']} prs={yesterday['prs']}")


if __name__ == "__main__":
    main()