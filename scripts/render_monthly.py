import json
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CACHE_PATH = "data/stats_cache.json"
OUT_PATH = "assets/stats/monthly_activity.svg"

FG = "#c9d1d9"
COMMIT_COLOR = "#58a6ff"
PR_COLOR = "#3fb950"
REVIEW_COLOR = "#d29922"
ISSUE_COLOR = "#f778ba"
GRID_COLOR = "#21262d"


def style_axis(ax_bar, ax_line, bar_color, line_color):
    ax_bar.tick_params(axis="y", colors=bar_color, labelsize=8)
    ax_line.tick_params(axis="y", colors=line_color, labelsize=8)
    ax_bar.tick_params(axis="x", colors=FG, labelsize=8, rotation=45)
    for spine in ax_bar.spines.values():
        spine.set_color(GRID_COLOR)
    for spine in ax_line.spines.values():
        spine.set_visible(False)
    ax_bar.grid(axis="y", color=GRID_COLOR, linewidth=0.6, alpha=0.5)
    ax_bar.set_axisbelow(True)


def main():
    with open(CACHE_PATH, "r") as f:
        data = json.load(f)

    months = [d["month"] for d in data]
    commits = [d["commits"] for d in data]
    prs = [d["prs"] for d in data]
    reviews = [d.get("reviews", 0) for d in data]
    issues = [d.get("issues", 0) for d in data]

    fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(11, 6.5), dpi=150, sharex=True)
    fig.patch.set_alpha(0)
    ax1.patch.set_alpha(0)
    ax2 = ax1.twinx()
    ax1.bar(months, prs, color=PR_COLOR, alpha=0.55, width=0.5, label="Pull Requests")
    ax2.plot(months, commits, color=COMMIT_COLOR, linewidth=2.4, marker="o", markersize=4, label="Commits")
    ax1.set_ylabel("Pull Requests", color=PR_COLOR, fontsize=9)
    ax2.set_ylabel("Commits", color=COMMIT_COLOR, fontsize=9)
    style_axis(ax1, ax2, PR_COLOR, COMMIT_COLOR)
    ax1.set_title("Output", color=FG, fontsize=10, loc="left")

    ax3.patch.set_alpha(0)
    ax4 = ax3.twinx()
    ax3.bar(months, issues, color=ISSUE_COLOR, alpha=0.55, width=0.5, label="Issues")
    ax4.plot(months, reviews, color=REVIEW_COLOR, linewidth=2.4, marker="o", markersize=4, label="Code Reviews")
    ax3.set_ylabel("Issues", color=ISSUE_COLOR, fontsize=9)
    ax4.set_ylabel("Code Reviews", color=REVIEW_COLOR, fontsize=9)
    style_axis(ax3, ax4, ISSUE_COLOR, REVIEW_COLOR)
    ax3.set_title("Collaboration", color=FG, fontsize=10, loc="left")

    fig.legend(
        handles=[
            plt.Line2D([0], [0], color=COMMIT_COLOR, marker="o", label="Commits"),
            plt.Rectangle((0, 0), 1, 1, color=PR_COLOR, alpha=0.55, label="Pull Requests"),
            plt.Line2D([0], [0], color=REVIEW_COLOR, marker="o", label="Code Reviews"),
            plt.Rectangle((0, 0), 1, 1, color=ISSUE_COLOR, alpha=0.55, label="Issues")
        ],
        loc="upper center",
        bbox_to_anchor=(0.5, 1.02),
        frameon=False,
        labelcolor=FG,
        fontsize=8,
        ncol=4
    )

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    fig.savefig(OUT_PATH, transparent=True, format="svg")


if __name__ == "__main__":
    main()