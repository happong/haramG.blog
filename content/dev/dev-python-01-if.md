---
title: if문으로 조건에 따라 다르게 동작시키기
dashboard_id: dev-python-01-if
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
---

## 경험 메모

네이버 발행 완료 (for문 글에서 '지난 글'로 언급). 발행일 미기록.

## 티스토리 초안

# 파이썬 if / elif / else 문법 정리 (비교·논리 연산자, 자주 나는 에러까지)

안녕하세요, 하해입니다! ☺️

if문은 **조건에 따라 다른 코드를 실행**하게 만드는 문법이에요.
이번 글은 문법, 연산자, 자주 나는 에러를 표로 정리해서 필요할 때 바로 찾아볼 수 있게 만들어봤어요. (파이썬 3.13 기준, 예제는 모두 직접 실행해서 확인했어요)

## 1. 기본 구조

```python
severity = 2
if severity == 1:
    print("즉시 핫픽스")
elif severity == 2:
    print("다음 패치에 포함")
else:
    print("백로그에 등록")
# 결과
# 다음 패치에 포함
```

| 부분 | 의미 |
|---|---|
| `if 조건:` | 조건이 참이면 아래 코드 실행 |
| `elif 조건:` | 앞의 조건이 거짓이고, 이 조건이 참이면 실행 (여러 개 가능) |
| `else:` | 위의 조건이 모두 거짓일 때 실행 |

기억할 두 가지: **조건 끝에 콜론(:)**, 실행할 코드는 **들여쓰기(보통 스페이스 4칸)**.

## 2. 비교 연산자

| 연산자 | 의미 | 예시 (`x = 5`) | 결과 |
|---|---|---|---|
| `==` | 같다 | `x == 5` | `True` |
| `!=` | 다르다 | `x != 5` | `False` |
| `>` / `<` | 크다 / 작다 | `x > 3` | `True` |
| `>=` / `<=` | 이상 / 이하 | `x <= 4` | `False` |

## 3. 논리 연산자: and, or, not

```python
is_crash = True
users = 1200
if is_crash and users >= 1000:
    print("긴급 대응")
if not is_crash or users < 100:
    print("일반 처리")
else:
    print("모니터링")
# 결과
# 긴급 대응
# 모니터링
```

| 연산자 | 참이 되는 경우 |
|---|---|
| `A and B` | A, B **둘 다** 참 |
| `A or B` | A, B 중 **하나라도** 참 |
| `not A` | A가 거짓 |

## 4. elif는 순서가 중요해요

위에서부터 검사하다가 **처음 참이 되는 곳 하나만** 실행돼요.

```python
score = 95
if score >= 60:
    print("C")
elif score >= 90:
    print("A")
# 결과
# C
```

95점인데 `C`가 나왔어요. `score >= 60`이 먼저 참이 돼서 거기서 끝났기 때문이에요. **범위가 좁은 조건(큰 숫자)부터** 써야 해요.

```python
score = 95
if score >= 90:
    print("A")
elif score >= 60:
    print("C")
# 결과
# A
```

## 5. 자주 나는 에러

### ① = 와 == 헷갈림

```python
x = 3
if x = 3:
    print("3")
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

`=`는 값을 **담는** 것, `==`는 **비교**하는 것이에요. 조건에는 `==`를 써야 해요.

### ② 들여쓰기를 안 함

```python
bug = "critical"
if bug == "critical":
print("핫픽스")
# IndentationError: expected an indented block after 'if' statement on line 2
```

에러 메시지에 **몇 번째 줄**의 if문인지 나오니까, 그 줄 바로 아래를 확인하면 돼요.

### ③ 콜론 빠뜨림

`if bug == "critical"` 처럼 끝에 `:`가 없으면 `SyntaxError`가 나요. if, elif, else 줄 끝에는 항상 콜론!

## 요약

| 체크 | 내용 |
|---|---|
| 콜론 | `if`, `elif`, `else` 줄 끝에 `:` |
| 들여쓰기 | 실행할 코드는 스페이스 4칸 |
| 비교 | 같은지 볼 때는 `==` |
| elif 순서 | 좁은 조건부터 |
| 여러 조건 | `and`, `or`, `not` |

다음 글에서는 같은 작업을 여러 번 반복하는 **for문**을 정리할게요. if문과 같이 쓰면 할 수 있는 게 훨씬 많아져요!

이해가 안 되는 예제가 있으면 댓글로 편하게 물어봐주세요!

태그: 파이썬, python, 파이썬if문, if문, elif, 조건문, 비교연산자, 논리연산자, IndentationError, 파이썬기초
