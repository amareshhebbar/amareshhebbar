import os
import json
import argparse
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timezone, timedelta

HISTORY_PATH = "data/watch_history.json"
RECIPIENT = "reshama0302@gmail.com"


def load_history():
    with open(HISTORY_PATH, "r") as f:
        return json.load(f)


def build_window_report(history):
    if not history:
        return "No data available yet."

    entry = history[-1]
    lines = []
    lines.append("GitHub Activity Report — Last 6 Hours")
    lines.append(f"Generated: {entry['timestamp']}")
    lines.append("")
    lines.append("Repo Views:")
    for repo, r in sorted(entry["repos"].items()):
        lines.append(f"  {repo}: {r['views_delta_count']} views, {r['views_delta_uniques']} unique")
    lines.append("")
    lines.append("New Watchers This Window:")
    any_new = False
    for repo, r in sorted(entry["repos"].items()):
        if r["watchers_new"]:
            any_new = True
            names = ", ".join(r["watchers_new"])
            lines.append(f"  {repo}: {len(r['watchers_new'])} new ({names})")
    if not any_new:
        lines.append("  None")
    lines.append("")
    t = entry["totals"]
    lines.append(
        f"Totals right now: {t['watchers_total']} watchers across all repos, "
        f"{t['views_today_count']} views today, {t['views_today_uniques']} unique today"
    )
    return "\n".join(lines)


def build_daily_report(history):
    if not history:
        return "No data available yet."

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=24)
    window_entries = [e for e in history if datetime.fromisoformat(e["timestamp"]) >= cutoff]
    if not window_entries:
        window_entries = [history[-1]]

    latest = history[-1]
    repo_agg = {}
    for e in window_entries:
        for repo, r in e["repos"].items():
            agg = repo_agg.setdefault(repo, {"views": 0, "uniques": 0, "new_watchers": set()})
            agg["views"] += r["views_delta_count"]
            agg["uniques"] += r["views_delta_uniques"]
            agg["new_watchers"].update(r["watchers_new"])

    lines = []
    lines.append("GitHub Daily Activity Report")
    lines.append(f"Generated: {latest['timestamp']}")
    lines.append("")
    lines.append("Per Repo:")
    for repo in sorted(repo_agg):
        agg = repo_agg[repo]
        current_watchers = latest["repos"].get(repo, {}).get("watchers_total", 0)
        lines.append(
            f"  {repo}: {agg['views']} views today, {agg['uniques']} unique, "
            f"{len(agg['new_watchers'])} new watchers, {current_watchers} total watchers"
        )
    lines.append("")
    lines.append("Overall Totals:")
    lines.append(f"  Total watchers across all repos: {latest['totals']['watchers_total']}")
    lines.append(f"  New watchers today: {sum(len(a['new_watchers']) for a in repo_agg.values())}")
    lines.append(f"  Total views today: {sum(a['views'] for a in repo_agg.values())}")
    lines.append(f"  Unique visitors today: {sum(a['uniques'] for a in repo_agg.values())}")
    return "\n".join(lines)


def send_email(subject, body):
    sender = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_APP_PASSWORD"]

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = RECIPIENT

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, [RECIPIENT], msg.as_string())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["window", "daily"], required=True)
    args = parser.parse_args()

    history = load_history()

    if args.mode == "daily":
        subject = "GitHub Daily Activity Report"
        body = build_daily_report(history)
    else:
        subject = "GitHub Activity Report — 6 Hour Update"
        body = build_window_report(history)

    send_email(subject, body)
    print(f"sent {args.mode} report")


if __name__ == "__main__":
    main()