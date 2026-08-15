import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA_PATH = "data/daily_activity.json"
OUT_PATH = "assets/stats/today_activity.svg"

FG = "#c9d1d9"
MUTED = "#8b949e"
TODAY_COLOR = "#58a6ff"
YDAY_COLOR = "#3fb950"


def main():
    with open(DATA_PATH, "r") as f:
        d = json.load(f)

    today, yesterday = d["today"], d["yesterday"]

    labels = ["Yesterday", "Today"]
    commits = [yesterday["commits"], today["commits"]]
    prs = [yesterday["prs"], today["prs"]]

    fig, axes = plt.subplots(1, 2, figsize=(6, 2.2), dpi=150)
    fig.patch.set_alpha(0)

    panels = [
        (axes[0], commits, "Commits", TODAY_COLOR),
        (axes[1], prs, "Pull Requests", YDAY_COLOR)
    ]

    for ax, values, title, color in panels:
        ax.patch.set_alpha(0)
        bars = ax.barh(labels, values, color=color, height=0.45)
        ax.set_title(title, color=FG, fontsize=9, pad=6)
        ax.tick_params(colors=FG, labelsize=8)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xticks([])
        max_val = max(values + [1])
        for bar, value in zip(bars, values):
            ax.text(
                bar.get_width() + max_val * 0.05,
                bar.get_y() + bar.get_height() / 2,
                str(value),
                va="center",
                color=MUTED,
                fontsize=8
            )

    fig.tight_layout()
    fig.savefig(OUT_PATH, transparent=True, format="svg")


if __name__ == "__main__":
    main()