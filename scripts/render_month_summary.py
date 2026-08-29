import json
import os
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CACHE_PATH = "data/stats_cache.json"
OUT_PATH = "assets/stats/month_summary.svg"

FG = "#c9d1d9"
MUTED = "#8b949e"
ACCENT = "#58a6ff"
BORDER = "#30363d"


def month_key(dt):
    return dt.strftime("%Y-%m")


def commits_for(cache_by_month, key):
    entry = cache_by_month.get(key)
    return entry["commits"] if entry else 0


def main():
    with open(CACHE_PATH, "r") as f:
        data = json.load(f)

    cache_by_month = {d["month"]: d for d in data}
    now = datetime.now(timezone.utc)
    this_month_key = month_key(now)
    last_month_key = month_key(now - relativedelta(months=1))
    two_months_ago_key = month_key(now - relativedelta(months=2))

    this_month_commits = commits_for(cache_by_month, this_month_key)
    last_month_commits = commits_for(cache_by_month, last_month_key)
    two_months_ago_commits = commits_for(cache_by_month, two_months_ago_key)

    fig = plt.figure(figsize=(6, 2.6), dpi=150)
    fig.patch.set_alpha(0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    box = plt.Rectangle((0.02, 0.05), 0.96, 0.9, transform=ax.transAxes,
                         facecolor="none", edgecolor=BORDER, linewidth=1.2)
    ax.add_patch(box)

    ax.text(0.5, 0.68, str(this_month_commits), transform=ax.transAxes,
            ha="center", va="center", fontsize=42, color=ACCENT, fontweight="bold")
    ax.text(0.5, 0.42, "Commits This Month", transform=ax.transAxes,
            ha="center", va="center", fontsize=10, color=FG)

    ax.plot([0.02, 0.98], [0.28, 0.28], transform=ax.transAxes, color=BORDER, linewidth=1)

    ax.text(0.27, 0.15, str(last_month_commits), transform=ax.transAxes,
            ha="center", va="center", fontsize=16, color=FG, fontweight="bold")
    ax.text(0.27, 0.06, "Last Month", transform=ax.transAxes,
            ha="center", va="center", fontsize=8, color=MUTED)

    ax.plot([0.5, 0.5], [0.05, 0.28], transform=ax.transAxes, color=BORDER, linewidth=1)

    ax.text(0.73, 0.15, str(two_months_ago_commits), transform=ax.transAxes,
            ha="center", va="center", fontsize=16, color=FG, fontweight="bold")
    ax.text(0.73, 0.06, "2 Months Ago", transform=ax.transAxes,
            ha="center", va="center", fontsize=8, color=MUTED)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    fig.savefig(OUT_PATH, transparent=True, format="svg")


if __name__ == "__main__":
    main()