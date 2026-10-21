#!/usr/bin/env python3
"""대시보드 DB(posts) → content/ 마크다운 동기화.

대시보드가 원본(source of truth)이고, content/ 는 GitHub 이슈 알림과 기록용 사본이다.
ArtifactData list 를 out_dir 로 받은 폴더를 넘긴다:

    python3 scripts/sync_dashboard.py <dump_dir>/posts

content/{food,dev,ai,life}/*.md 를 모두 지우고 DB 기준으로 다시 만든다.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
CATEGORIES = ("food", "dev", "ai", "life")


def status_of(doc: dict) -> str:
    if doc.get("naverDone"):
        return "published"
    if doc.get("stage") == "draft":
        return "draft"
    return "idea"


def one_line(value) -> str:
    return str(value if value is not None else "").replace("\n", " ").strip()


def render(doc_id: str, doc: dict) -> str:
    meta = {
        "title": one_line(doc.get("title")) or doc_id,
        "dashboard_id": doc_id,
        "category": doc.get("category", "food"),
        "status": status_of(doc),
        "stage": doc.get("stage", "idea"),
        "visited": doc.get("visited", ""),
        "planned": doc.get("planned", ""),
        "published": doc.get("naverDoneAt", "") if doc.get("naverDone") else "",
        "tistory_done": str(bool(doc.get("tistoryDone"))).lower(),
        "tistory_published": doc.get("tistoryDoneAt", "") if doc.get("tistoryDone") else "",
        "season": str(bool(doc.get("season"))).lower(),
        "season_end": doc.get("seasonEnd", ""),
        "priority": doc.get("priority", 3),
        "photos": len(doc.get("photos") or []),
        "place_shots": len(doc.get("placeShots") or []),
        "no_place": str(bool(doc.get("noPlace"))).lower(),
    }
    lines = ["---"] + [f"{k}: {one_line(v)}" for k, v in meta.items()] + ["---", ""]
    sections = [
        ("경험 메모", doc.get("memo")),
        ("Claude 질문", doc.get("questions")),
        ("사진 배치 안내", doc.get("photoNotes")),
        ("네이버 초안", doc.get("draftNaver")),
        ("티스토리 초안", doc.get("draftTistory")),
    ]
    for heading, body in sections:
        if body:
            lines += [f"## {heading}", "", str(body).rstrip(), ""]
    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    docs = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(src.glob("*.json"))}
    if not docs:
        sys.exit(f"{src} 에 JSON 문서가 없습니다. 덤프 경로를 확인하세요.")

    for cat in CATEGORIES:
        (CONTENT_DIR / cat).mkdir(parents=True, exist_ok=True)
        for old in (CONTENT_DIR / cat).glob("*.md"):
            old.unlink()

    for doc_id, doc in docs.items():
        cat = doc.get("category") if doc.get("category") in CATEGORIES else "food"
        (CONTENT_DIR / cat / f"{doc_id}.md").write_text(render(doc_id, doc), encoding="utf-8")
    print(f"{len(docs)}개 문서를 content/ 로 동기화했습니다.")


if __name__ == "__main__":
    main()
