# haramG.blog
블로그 히스토리 작성 — 경험한 콘텐츠를 쌓아두고, 나눠서 발행하고, 놓치지 않게 관리하는 저장소입니다.

## 구조

```
content/
  food/   맛집·추천 (주 2회)
  dev/    개발 공부 (주 1회)
  ai/     AI 활용기 – 유입용 (주 1회)
templates/  카테고리별 글 템플릿 (frontmatter 포함)
guides/
  style-guide.md      말투 가이드 (기존 글 기반으로 채움)
  platform-formats.md 네이버 / 티스토리 / 블로거 포맷 차이
images/     글에 들어갈 사진
scripts/backlog.py  현황 리포트 · 시즌 알림 계산
.github/workflows/blog-alerts.yml  GitHub 이슈 알림
```

## 사용 흐름

1. 경험하면 `templates/<카테고리>.md`를 복사해 `content/<카테고리>/날짜-이름.md`로 저장하고 **경험 메모**만 채웁니다.
2. Claude에게 초안 작성을 요청 → `status: draft` → 검토 후 `ready`.
3. 발행 날짜를 정하면 `planned`에 입력.
4. 네이버에 올린 뒤 `status: published`, `published`, `naver_url`을 채웁니다.

시즌 콘텐츠는 `season: true`, `season_end: YYYY-MM-DD`를 넣으면 우선순위가 올라가고 알림 대상이 됩니다.

## 상태값

| status | 의미 |
|---|---|
| idea | 경험만 하고 메모 전 |
| draft | 초안 작성됨 |
| ready | 검토 끝, 발행 대기 |
| published | 발행 완료 |

## GitHub 이슈 알림

| 언제 | 무엇을 |
|---|---|
| 매일 08:47 KST | `season_end`까지 14일 이하로 남은 미발행 시즌 글마다 `[시즌 알림]` 이슈 생성. D-7·3·1·0 및 마감 이후에는 댓글 추가, 발행하면 자동으로 닫힘 |
| 매주 월요일 08:41 KST | 주간 목표(맛집 2 · 개발 1 · AI 1) 대비 현황, 이번 주 예정 글, 예정일 지난 글, 후보 목록을 `weekly-report` 이슈로 생성 |

- 예약 실행(schedule)은 **기본 브랜치(main)에 있는 워크플로만** 동작합니다.
- Actions 탭 → Blog alerts → Run workflow 로 즉시 테스트할 수 있습니다.
- 이슈 알림을 받으려면 저장소 Watch 설정에서 Issues 알림을 켜두세요.

## 로컬에서 확인

```bash
python3 scripts/backlog.py status            # 이번 주 현황
python3 scripts/backlog.py alerts --days 14  # 시즌 알림 대상
```
