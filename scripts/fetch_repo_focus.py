import os
import json
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

from gh_client import run_query

OUT_PATH = "data/repo_focus.json"

QUERY = """
query($from: DateTime!, $to: DateTime!) {
  viewer {
    contributionsCollection(from: $from, to: $to) {
      commitContributionsByRepository(maxRepositories: 6) {
        repository {
          name
          isPrivate
        }
        contributions {
          totalCount
        }
      }
    }
  }
}
"""


def main():
    token = os.environ["STATS_TOKEN"]
    now = datetime.now(timezone.utc)
    start = datetime(now.year, now.month, 1, tzinfo=timezone.utc)
    end = start + relativedelta(months=1)

    data = run_query(token, QUERY, {
        "from": start.isoformat(),
        "to": end.isoformat()
    })

    repos = data["data"]["viewer"]["contributionsCollection"]["commitContributionsByRepository"]
    entries = [
        {
            "repo": r["repository"]["name"],
            "commits": r["contributions"]["totalCount"],
            "private": r["repository"]["isPrivate"]
        }
        for r in repos
    ]
    entries.sort(key=lambda x: x["commits"], reverse=True)

    with open(OUT_PATH, "w") as f:
        json.dump(entries, f, indent=2)

    for e in entries:
        print(f"{e['repo']}: {e['commits']} commits")


if __name__ == "__main__":
    main()