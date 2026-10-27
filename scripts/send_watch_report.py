import os
import json
import argparse
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timezone, timedelta

HISTORY_PATH = "data/watch_history.json"
DAILY_LOG_PATH = "data/views_daily_log.json"
RECIPIENT = "reshama0302@gmail.com"
IST = timezone(timedelta(hours=5, minutes=30))
RECENT_DAYS = 4
LAG_DAYS = 2


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        content = f.read().strip()
    if not content:
        return default
    return json.loads(content)


def views(n):
    return f"{n} view" if n == 1 else f"{n} views"


def format_generated(iso_timestamp):
    ts = datetime.fromisoformat(iso_timestamp)
    return f"{ts.astimezone(IST).strftime('%Y-%m-%d %H:%M')} IST ({ts.astimezone(timezone.utc).strftime('%H:%M')} UTC)"


def shift_date(date, days):
    return (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=days)).strftime("%Y-%m-%d")


def totals_by_date(daily_log):
    out = {}
    for days in daily_log.values():
        for date, v in days.items():
            agg = out.setdefault(date, {"count": 0, "uniques": 0})
            agg["count"] += v["count"]
            agg["uniques"] += v["uniques"]
    return out


def sum_range(by_date, start, end):
    count = 0
    uniques = 0
    for date, v in by_date.items():
        if start <= date <= end:
            count += v["count"]
            uniques += v["uniques"]
    return count, uniques


def format_new_days(new_days):
    parts = [f"{d}: +{v['count']}" for d, v in sorted(new_days.items())]
    return ", ".join(parts)


def build_recent_days(by_date, today):
    lines = ["Recent Days (UTC days, all repos):"]
    for i in range(RECENT_DAYS):
        date = shift_date(today, i)
        v = by_date.get(date, {"count": 0, "uniques": 0})
        note = "  (GitHub may still be filling this in)" if i < LAG_DAYS else ""
        lines.append(f"  {date}: {views(v['count'])}, {v['uniques']} unique{note}")
    active = sorted(d for d, v in by_date.items() if v["count"] > 0)
    if active:
        last = active[-1]
        lines.append(f"  Latest day with views: {last} ({views(by_date[last]['count'])})")
    return "\n".join(lines)


def build_period_summary(daily_log, latest_entry):
    today = latest_entry["timestamp"][:10]
    by_date = totals_by_date(daily_log)
    week = sum_range(by_date, shift_date(today, 6), today)
    month = sum_range(by_date, shift_date(today, 29), today)
    all_time = sum_range(by_date, "0000-00-00", "9999-99-99")
    t = latest_entry["totals"]

    lines = [build_recent_days(by_date, today), ""]
    lines.append("Views Summary (all public repos):")
    lines.append(f"  Last 7 Days: {views(week[0])}, {week[1]} unique")
    lines.append(f"  Last 30 Days: {views(month[0])}, {month[1]} unique")
    lines.append(f"  Last 14 Days (as GitHub reports it): {views(t['views_total_14d'])}, {t['views_uniques_14d']} unique")
    lines.append(f"  All Time (since tracking began): {views(all_time[0])}, {all_time[1]} unique")
    lines.append("")
    lines.append(f"Watchers (excluding you): {t['watchers_total']}")
    lines.append("")
    lines.append("Note: GitHub publishes traffic per UTC day and usually 1 to 2 days late.")
    lines.append("Unique counts over 7/30 days and all time are daily uniques added together.")
    failed = sorted(r for r, v in latest_entry["repos"].items() if not v.get("traffic_ok", True))
    if failed:
        lines.append(f"Traffic fetch failed for: {', '.join(failed)}")
    return "\n".join(lines)


def build_watcher_lines(repo_new_watchers):
    lines = []
    for repo in sorted(repo_new_watchers):
        names = sorted(repo_new_watchers[repo])
        if names:
            lines.append(f"  {repo}: {len(names)} new ({', '.join(names)})")
    return lines or ["  None"]


def build_window_report(history, daily_log):
    if not history:
        return "No data available yet."

    entry = history[-1]
    lines = ["GitHub Activity Report: Last 6 Hours", f"Generated: {format_generated(entry['timestamp'])}", ""]

    lines.append("New Views Reported Since Last Run:")
    active = [(repo, r) for repo, r in sorted(entry["repos"].items(), key=lambda x: -x[1]["views_delta_count"]) if r["views_delta_count"] > 0]
    if active:
        for repo, r in active:
            detail = format_new_days(r.get("views_new_days", {}))
            lines.append(f"  {repo}: {views(r['views_delta_count'])}, {r['views_delta_uniques']} unique  [{detail}]")
        t = entry["totals"]
        lines.append(f"  Total: {views(t['views_delta_count'])}, {t['views_delta_uniques']} unique")
    else:
        lines.append("  Nothing new from GitHub this window")
    lines.append("")

    lines.append("New Watchers This Window:")
    lines.extend(build_watcher_lines({repo: r["watchers_new"] for repo, r in entry["repos"].items()}))
    lines.append("")
    lines.append(build_period_summary(daily_log, entry))
    return "\n".join(lines)


def build_daily_report(history, daily_log):
    if not history:
        return "No data available yet."

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=24)
    window_entries = [e for e in history if datetime.fromisoformat(e["timestamp"]) >= cutoff] or [history[-1]]
    latest = history[-1]

    repo_agg = {}
    for e in window_entries:
        for repo, r in e["repos"].items():
            agg = repo_agg.setdefault(repo, {"views": 0, "uniques": 0, "days": {}, "new_watchers": set()})
            agg["views"] += r["views_delta_count"]
            agg["uniques"] += r["views_delta_uniques"]
            agg["new_watchers"].update(r["watchers_new"])
            for d, v in r.get("views_new_days", {}).items():
                day = agg["days"].setdefault(d, {"count": 0, "uniques": 0})
                day["count"] += v["count"]
                day["uniques"] += v["uniques"]

    lines = ["GitHub Daily Activity Report", f"Generated: {format_generated(latest['timestamp'])}", ""]
    lines.append("New Views Reported In Last 24 Hours:")
    active = sorted(((r, a) for r, a in repo_agg.items() if a["views"] > 0), key=lambda x: -x[1]["views"])
    if active:
        for repo, a in active:
            lines.append(f"  {repo}: {views(a['views'])}, {a['uniques']} unique  [{format_new_days(a['days'])}]")
        lines.append(f"  Total: {views(sum(a['views'] for _, a in active))}, {sum(a['uniques'] for _, a in active)} unique")
    else:
        lines.append("  Nothing new from GitHub in the last 24 hours")
    lines.append("")

    lines.append("New Watchers Today:")
    lines.extend(build_watcher_lines({r: a["new_watchers"] for r, a in repo_agg.items()}))
    lines.append("")
    lines.append(build_period_summary(daily_log, latest))
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
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    history = load_json(HISTORY_PATH, [])
    daily_log = load_json(DAILY_LOG_PATH, {})

    if args.mode == "daily":
        subject = "GitHub Daily Activity Report"
        body = build_daily_report(history, daily_log)
    else:
        subject = "GitHub Activity Report: 6 Hour Update"
        body = build_window_report(history, daily_log)

    if args.dry_run:
        print(subject)
        print(body)
        return

    send_email(subject, body)
    print(f"sent {args.mode} report")


if __name__ == "__main__":
    main()