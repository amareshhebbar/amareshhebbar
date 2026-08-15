import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA_PATH = "data/repo_focus.json"
OUT_PATH = "assets/stats/repo_focus.svg"

FG = "#c9d1d9"
MUTED = "#8b949e"
BAR_COLOR = "#58a6ff"


def main():
    with open(DATA_PATH, "r") as f:
        entries = json.load(f)

    entries = list(reversed(entries))
    labels = [e["repo"] for e in entries]
    values = [e["commits"] for e in entries]

    fig, ax = plt.subplots(figsize=(7, 3), dpi=150)
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)

    bars = ax.barh(labels, values, color=BAR_COLOR, height=0.5)
    ax.set_title("Repo Focus — This Month", color=FG, fontsize=10, loc="left")
    ax.tick_params(colors=FG, labelsize=8)
    ax.set_xticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    max_val = max(values + [1])
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_width() + max_val * 0.03,
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