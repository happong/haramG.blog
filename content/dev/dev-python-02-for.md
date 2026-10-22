---
title: for문으로 반복 작업 간단히 하기
dashboard_id: dev-python-02-for
category: dev
status: published
stage: draft
visited: 
planned: 
published: 
tistory_done: false
tistory_published: 
season: false
season_end: 
priority: 3
photos: 0
place_shots: 0
no_place: false
---

## 경험 메모

네이버 발행 완료. 발행일 미기록.

## 티스토리 초안

# 파이썬 for문과 range() 정리 (문자열 반복, enumerate, 합계 구하기, 연습문제 정답 포함)

안녕하세요, 하해입니다! ☺️

for문은 **정해진 범위나 묶음 안의 값을 하나씩 꺼내면서 같은 코드를 반복**하는 문법이에요.
이번 글은 자주 쓰는 패턴과 실수를 모아서, 연습문제와 **정답·해설**까지 한 번에 볼 수 있게 정리했어요. (파이썬 3.13 기준, 예제는 모두 직접 실행해서 확인했어요)

## 1. 기본 구조

```python
for 변수 in 반복할_대상:
    반복할 코드
```

`반복할_대상`에는 `range()`, 리스트, 문자열처럼 값을 하나씩 꺼낼 수 있는 것이 들어가요.

## 2. range() 한눈에 보기

| 코드 | 만들어지는 숫자 | 설명 |
|---|---|---|
| `range(4)` | 0, 1, 2, 3 | 0부터 4 **직전**까지 |
| `range(2, 6)` | 2, 3, 4, 5 | 2부터 6 직전까지 |
| `range(0, 10, 3)` | 0, 3, 6, 9 | 3씩 증가 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 | 1씩 감소 (거꾸로) |

```python
for sec in range(3, 0, -1):
    print(f"배포까지 {sec}초")
print("배포 시작!")
# 결과
# 배포까지 3초
# 배포까지 2초
# 배포까지 1초
# 배포 시작!
```

## 3. 리스트와 문자열 반복

```python
patch_notes = ["로그인 오류 수정", "UI 개선", "성능 최적화"]
for note in patch_notes:
    print("-", note)
# 결과
# - 로그인 오류 수정
# - UI 개선
# - 성능 최적화
```

문자열도 **글자 하나씩** 꺼낼 수 있어요.

```python
for ch in "QA":
    print(ch)
# 결과
# Q
# A
```

## 4. enumerate(): 번호와 값을 같이 꺼내기

```python
test_cases = ["로그인", "결제", "로그아웃"]
for i, case in enumerate(test_cases, start=1):
    print(f"TC-{i}: {case}")
# 결과
# TC-1: 로그인
# TC-2: 결제
# TC-3: 로그아웃
```

`start=1`을 빼면 번호가 0부터 시작해요.

## 5. 자주 쓰는 패턴: 합계·개수 구하기

반복 **전에** 0을 담은 변수를 만들고, 반복하면서 더해가는 패턴이에요.

```python
daily_bugs = [3, 0, 5, 2]
total = 0
for n in daily_bugs:
    total += n
print("이번 주 버그:", total)
# 결과
# 이번 주 버그: 10
```

`total += n` 은 `total = total + n` 을 줄여 쓴 거예요.

## 6. 자주 하는 실수

| 실수 | 증상 | 해결 |
|---|---|---|
| `for i in range(5)` 끝에 `:` 없음 | `SyntaxError` | 줄 끝에 콜론 |
| 반복할 코드 들여쓰기 안 함 | `IndentationError` | 스페이스 4칸 |
| `range(1, 5)`에 5가 나올 거라 생각함 | 1~4까지만 나옴 | 끝 숫자는 **포함 안 됨** → `range(1, 6)` |
| 합계 변수를 for문 **안에서** 0으로 만듦 | 매번 0으로 초기화돼서 마지막 값만 남음 | 합계 변수는 for문 **위에서** 만들기 |

## 7. 연습문제

**문제 1.** 1부터 10까지의 합을 출력하세요.

**문제 2.** 아래 코드의 결과는?

```python
for i in range(0, 7, 2):
    print(i, end=" ")
```

**문제 3.** 리스트에서 `"fail"`이 몇 개인지 세어 출력하세요.

```python
results = ["pass", "fail", "pass", "fail", "fail"]
```

## 8. 정답과 해설

**문제 1**

```python
total = 0
for n in range(1, 11):
    total += n
print(total)
# 결과
# 55
```

`range(1, 11)`이어야 10까지 포함돼요.

**문제 2**

```python
for i in range(0, 7, 2):
    print(i, end=" ")
# 결과
# 0 2 4 6
```

0부터 2씩 증가하고, 7 직전에서 멈춰요. `end=" "` 때문에 한 줄에 띄어쓰기로 이어서 출력돼요.

**문제 3**

```python
results = ["pass", "fail", "pass", "fail", "fail"]
fail_count = 0
for r in results:
    if r == "fail":
        fail_count += 1
print("실패:", fail_count)
# 결과
# 실패: 3
```

for문 안에 if문을 넣어서, 조건에 맞을 때만 개수를 올리는 패턴이에요.

## 요약

| 하고 싶은 것 | 코드 |
|---|---|
| n번 반복 | `for i in range(n):` |
| 리스트 값 하나씩 | `for x in 리스트:` |
| 번호와 값 같이 | `for i, x in enumerate(리스트, start=1):` |
| 거꾸로 반복 | `range(시작, 끝, -1)` |
| 합계 | 반복 전 `total = 0` → 안에서 `total += x` |

연습문제를 다른 방법으로 풀었다면 댓글로 공유해주세요. 같이 비교해봐요!

태그: 파이썬, python, 파이썬for문, for문, range, enumerate, 반복문, 파이썬반복문, 파이썬기초, 코딩입문
