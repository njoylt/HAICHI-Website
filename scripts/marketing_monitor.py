#!/usr/bin/env python3
"""Collect public HAICHI campaign signals for the scheduled GitHub workflow."""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SITE_URL = "https://haichi.app/"
DEV_API_URL = (
    "https://dev.to/api/articles/haichi_ops_861a9ec315b1e7/"
    "i-got-tired-of-juggling-ollama-tabs-terminals-and-agent-chats-glj"
)
YOUTUBE_URL = "https://www.youtube.com/watch?v=US1zJvdP2c0"
CAMPAIGN_STARTED_AT = datetime(2026, 7, 13, 18, 55, 41, tzinfo=timezone.utc)
USER_AGENT = "HAICHI-Marketing-Monitor/1.0 (+https://haichi.app/)"

ALERT_TITLES = {
    "site_down": "[Marketing monitor] HAICHI site needs attention",
    "promo_review": "[Marketing monitor] Promo review signal",
    "campaign_refresh": "[Marketing monitor] Campaign refresh due",
    "first_engagement": "[Marketing monitor] First public engagement",
}


def fetch(url: str, *, accept: str = "text/html") -> tuple[int | None, bytes, str | None]:
    request = urllib.request.Request(
        url,
        headers={"Accept": accept, "User-Agent": USER_AGENT},
    )
    last_error: str | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.status, response.read(), None
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = str(exc)
            if attempt < 2:
                time.sleep(2**attempt)
    return None, b"", last_error


def extract_youtube_views(html: str) -> int | None:
    patterns = (
        r'<meta itemprop="interactionCount" content="(\d+)"',
        r'"viewCount":"(\d+)"',
    )
    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            return int(match.group(1))
    return None


def count_feedback_issues(repository: str, token: str) -> tuple[int | None, str | None]:
    if not repository or not token:
        return None, "GitHub repository context is unavailable"

    url = f"https://api.github.com/repos/{repository}/issues?state=all&per_page=100"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": USER_AGENT,
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            issues = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return None, str(exc)

    count = sum(
        1
        for issue in issues
        if "pull_request" not in issue
        and str(issue.get("title", "")).startswith("First workflow feedback:")
    )
    return count, None


def choose_alert(metrics: dict[str, Any]) -> str:
    if metrics["site"]["status"] != 200:
        return "site_down"

    qualified_signals = metrics["qualified_signals"]
    public_engagement = metrics["public_engagement"]
    if qualified_signals >= 3:
        return "promo_review"
    if metrics["campaign_age_hours"] >= 72 and public_engagement == 0:
        return "campaign_refresh"
    if public_engagement > 0:
        return "first_engagement"
    return "none"


def collect_metrics(now: datetime | None = None) -> dict[str, Any]:
    now = now or datetime.now(timezone.utc)

    site_status, _, site_error = fetch(SITE_URL)

    dev_status, dev_body, dev_error = fetch(DEV_API_URL, accept="application/json")
    dev_data: dict[str, Any] = {}
    if dev_status == 200:
        try:
            dev_data = json.loads(dev_body.decode("utf-8"))
        except json.JSONDecodeError as exc:
            dev_error = str(exc)

    youtube_status, youtube_body, youtube_error = fetch(YOUTUBE_URL)
    youtube_views = None
    if youtube_status == 200:
        youtube_views = extract_youtube_views(youtube_body.decode("utf-8", errors="ignore"))

    feedback_count, feedback_error = count_feedback_issues(
        os.environ.get("GITHUB_REPOSITORY", ""),
        os.environ.get("GITHUB_TOKEN", ""),
    )

    dev_reactions = int(dev_data.get("public_reactions_count") or 0)
    dev_comments = int(dev_data.get("comments_count") or 0)
    known_feedback = feedback_count or 0
    qualified_signals = dev_comments + known_feedback

    metrics = {
        "checked_at": now.isoformat(),
        "campaign_age_hours": round((now - CAMPAIGN_STARTED_AT).total_seconds() / 3600, 1),
        "site": {"status": site_status, "error": site_error},
        "dev_to": {
            "status": dev_status,
            "reactions": dev_reactions,
            "comments": dev_comments,
            "views": dev_data.get("page_views_count"),
            "error": dev_error,
        },
        "youtube": {
            "status": youtube_status,
            "views": youtube_views,
            "error": youtube_error,
        },
        "github_feedback_issues": feedback_count,
        "github_feedback_error": feedback_error,
        "qualified_signals": qualified_signals,
        "public_engagement": dev_reactions + qualified_signals,
    }
    metrics["alert"] = choose_alert(metrics)
    return metrics


def render_summary(metrics: dict[str, Any]) -> str:
    alert = metrics["alert"]
    action = {
        "site_down": "Check the deployment and DNS before sending more traffic.",
        "promo_review": (
            "Qualified feedback reached the promo-review threshold. Check Lemon Squeezy "
            "for Pro conversions before enabling a discount."
        ),
        "campaign_refresh": (
            "The campaign is at least 72 hours old without public engagement. Prepare a "
            "new organic hook or channel experiment."
        ),
        "first_engagement": "Review the response and reply personally before changing the offer.",
        "none": "No marketing change is needed yet.",
    }[alert]

    return "\n".join(
        [
            "## HAICHI marketing monitor",
            "",
            f"- Checked: `{metrics['checked_at']}`",
            f"- Campaign age: `{metrics['campaign_age_hours']} hours`",
            f"- haichi.app HTTP status: `{metrics['site']['status']}`",
            f"- DEV.to reactions/comments: `{metrics['dev_to']['reactions']}` / `{metrics['dev_to']['comments']}`",
            f"- YouTube views: `{metrics['youtube']['views']}`",
            f"- First-workflow feedback issues: `{metrics['github_feedback_issues']}`",
            f"- Decision: `{alert}`",
            "",
            action,
            "",
            "This monitor uses public signals only. It does not publish posts, spend money, "
            "or enable Lemon Squeezy discounts.",
        ]
    )


def write_github_output(path: Path, alert: str, title: str) -> None:
    with path.open("a", encoding="utf-8") as output:
        output.write(f"alert={alert}\n")
        output.write(f"title={title}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", type=Path, default=Path("marketing-monitor-summary.md"))
    parser.add_argument("--json", dest="json_path", type=Path)
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()

    metrics = collect_metrics()
    summary = render_summary(metrics)
    args.summary.write_text(summary + "\n", encoding="utf-8")
    if args.json_path:
        args.json_path.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    if args.github_output:
        title = ALERT_TITLES.get(metrics["alert"], "")
        write_github_output(args.github_output, metrics["alert"], title)

    print(json.dumps(metrics, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
