#!/usr/bin/env python3
"""블로그 글 백로그 관리 스크립트.

content/ 아래의 마크다운 파일 frontmatter를 읽어서
- status : 전체 현황 + 이번 주 발행 계획 리포트 (마크다운)
- alerts : 마감이 다가오는 시즌 글 목록 (JSON)
을 출력한다. 외부 패키지 없이 표준 라이브러리만 사용한다.
"""

import argparse
import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
KST = ZoneInfo("Asia/Seoul")

# 주간 목표 발행 수
WEEKLY_QUOTA = {"food": 2, "dev": 1, "ai": 1}
CATEGORY_LABEL = {"food": "맛집·추천", "dev": "개발 공부", "ai": "AI 활용기(유입용)"}
STATUS_ORDER = ["idea", "draft", "ready", "published"]
STATUS_LABEL = {"idea": "아이디어", "draft": "초안", "ready": "발행 대기", "published": "발행 완료"}


def today_kst() -> date:
    return datetime.now(KST).date()


def parse_frontmatter(text: str) -> dict:
    """'---'로 감싼 단순 key: value frontmatter만 지원한다."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        value = value.split(" #", 1)[0].strip().strip('"').strip("'")
        meta[key.strip()] = value
    return meta


def to_date(value):
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def load_posts(content_dir: Path = CONTENT_DIR) -> list:
    posts = []
    for path in sorted(content_dir.rglob("*.md")):
        if path.name.startswith("_"):
            continue
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not meta:
            continue
        posts.append({
            "path": str(path.relative_to(ROOT)),
            "title": meta.get("title") or path.stem,
            "category": meta.get("category", ""),
            "status": meta.get("status", "idea"),
            "visited": to_date(meta.get("visited")),
            "planned": to_date(meta.get("planned")),
            "published": to_date(meta.get("published")),
            "season": meta.get("season", "").lower() == "true",
            "season_end": to_date(meta.get("season_end")),
            "priority": int(meta.get("priority") or 3),
        })
    return posts


def week_range(day: date):
    start = day - timedelta(days=day.weekday())  # 월요일
    return start, start + timedelta(days=6)


def season_alerts(posts, today, days):
    alerts = []
    for p in posts:
        if not p["season"] or p["status"] == "published" or not p["season_end"]:
            continue
        left = (p["season_end"] - today).days
        if left <= days:
            alerts.append({
                "title": p["title"],
                "path": p["path"],
                "category": p["category"],
                "status": p["status"],
                "season_end": p["season_end"].isoformat(),
                "days_left": left,
                "planned": p["planned"].isoformat() if p["planned"] else None,
            })
    return sorted(alerts, key=lambda a: a["days_left"])


def sort_key(p):
    # 시즌 마감이 가까운 글 → 우선순위 숫자가 작은 글 → 경험한 지 오래된 글
    season_end = p["season_end"] if p["season"] and p["season_end"] else date.max
    return (season_end, p["priority"], p["visited"] or date.max)


def status_report(posts, today) -> str:
    start, end = week_range(today)
    out = [f"# 블로그 주간 체크 ({start} ~ {end})", ""]

    # 1. 이번 주 목표 대비
    out += ["## 이번 주 목표", "", "| 카테고리 | 목표 | 발행 완료 | 예정 | 부족 |", "|---|---|---|---|---|"]
    for cat, quota in WEEKLY_QUOTA.items():
        done = [p for p in posts if p["category"] == cat and p["status"] == "published"
                and p["published"] and start <= p["published"] <= end]
        planned = [p for p in posts if p["category"] == cat and p["status"] != "published"
                   and p["planned"] and start <= p["planned"] <= end]
        lack = max(quota - len(done) - len(planned), 0)
        out.append(f"| {CATEGORY_LABEL[cat]} | {quota} | {len(done)} | {len(planned)} | {lack} |")
    out.append("")

    # 2. 이번 주 발행 예정
    week_posts = sorted((p for p in posts if p["status"] != "published" and p["planned"]
                         and start <= p["planned"] <= end), key=lambda p: p["planned"])
    out += ["## 이번 주 발행 예정", ""]
    out += [f"- [ ] {p['planned']} · {CATEGORY_LABEL.get(p['category'], p['category'])} · "
            f"**{p['title']}** ({STATUS_LABEL.get(p['status'], p['status'])}) — `{p['path']}`"
            for p in week_posts] or ["- 없음"]
    out.append("")

    # 3. 예정일이 지났는데 아직 안 올린 글
    overdue = sorted((p for p in posts if p["status"] != "published" and p["planned"]
                      and p["planned"] < start), key=lambda p: p["planned"])
    if overdue:
        out += ["## ⚠️ 예정일 지남", ""]
        out += [f"- {p['planned']} · **{p['title']}** — `{p['path']}`" for p in overdue]
        out.append("")

    # 4. 일정 미정 후보 (부족분 채우기용)
    out += ["## 일정 미정 후보 (우선순위순)", ""]
    for cat in WEEKLY_QUOTA:
        cands = sorted((p for p in posts if p["category"] == cat and p["status"] != "published"
                        and not p["planned"]), key=sort_key)
        out.append(f"**{CATEGORY_LABEL[cat]}**")
        for p in cands[:5]:
            tag = f" 🔥시즌 ~{p['season_end']}" if p["season"] and p["season_end"] else ""
            out.append(f"- {p['title']} ({STATUS_LABEL.get(p['status'], p['status'])}){tag} — `{p['path']}`")
        if not cands:
            out.append("- 없음")
        out.append("")

    # 5. 전체 현황
    out += ["## 전체 현황", "", "| 상태 | " + " | ".join(CATEGORY_LABEL[c] for c in WEEKLY_QUOTA) + " |",
            "|---|" + "---|" * len(WEEKLY_QUOTA)]
    for st in STATUS_ORDER:
        counts = [sum(1 for p in posts if p["status"] == st and p["category"] == c) for c in WEEKLY_QUOTA]
        out.append(f"| {STATUS_LABEL[st]} | " + " | ".join(map(str, counts)) + " |")
    out.append("")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["status", "alerts"])
    parser.add_argument("--days", type=int, default=14, help="시즌 마감 며칠 전부터 알릴지")
    parser.add_argument("--today", help="기준 날짜 (YYYY-MM-DD, 테스트용)")
    args = parser.parse_args()

    today = date.fromisoformat(args.today) if args.today else today_kst()
    posts = load_posts()
    if args.command == "status":
        print(status_report(posts, today))
    else:
        json.dump(season_alerts(posts, today, args.days), sys.stdout, ensure_ascii=False, indent=2)
        print()


if __name__ == "__main__":
    main()
