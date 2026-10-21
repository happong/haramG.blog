---
title: 변수와 자료형
dashboard_id: dev-python-types
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

네이버 발행 완료 (제목 목록으로 등록). 발행일 미기록.

## 티스토리 초안

# 파이썬 자료형 정리: int, float, str, bool, list와 type() 확인법

안녕하세요, 하해입니다! ☺️

변수에는 숫자도, 글자도, 참/거짓도 담을 수 있어요. 이렇게 **값의 종류**를 자료형이라고 해요.
자료형을 알아야 "왜 이 코드는 에러가 나지?"를 이해할 수 있어서, 처음에 한 번 정리해두면 좋아요. (파이썬 3.13 기준, 예제는 모두 직접 실행해서 확인했어요)

## 기본 자료형 한눈에 보기

| 자료형 | 이름 | 예시 | 용도 |
|---|---|---|---|
| `int` | 정수 | `10`, `-3` | 개수, 빌드 번호 |
| `float` | 실수 | `3.14`, `0.5` | 비율, 평균 |
| `str` | 문자열 | `"QA"`, `'1.0.0'` | 이름, 메시지 |
| `bool` | 불리언 | `True`, `False` | 성공/실패 같은 참·거짓 |
| `list` | 리스트 | `["Dev", "Art"]` | 여러 값을 순서대로 묶기 |

## 1. type()으로 자료형 확인하기

```python
print(type(10))
print(type(3.14))
print(type("QA"))
print(type(True))
print(type(["Dev", "Art"]))
# 결과
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
# <class 'list'>
```

헷갈릴 때는 `type()`으로 바로 확인하는 습관을 들이면 좋아요.

## 2. 숫자 계산할 때 알아둘 점

```python
print(10 / 2)
print(7 // 2)
print(7 % 2)
# 결과
# 5.0
# 3
# 1
```

| 연산자 | 의미 | 주의 |
|---|---|---|
| `/` | 나누기 | 나누어떨어져도 결과는 **float** (`5.0`) |
| `//` | 몫 | 소수점 아래 버림 |
| `%` | 나머지 | 짝수/홀수 판별에 자주 씀 |

## 3. 자료형 바꾸기 (형 변환)

```python
print(int("42") + 8)
print(str(42) + "번 빌드")
print(float("3.5"))
print(int(3.9))
# 결과
# 50
# 42번 빌드
# 3.5
# 3
```

`int(3.9)`는 반올림이 아니라 **소수점 아래를 버려서** `3`이 돼요.

## 4. 자주 하는 실수

### ① 문자열과 숫자를 + 로 붙이기

```python
count = 3
print("버그 " + count + "건")
# TypeError: can only concatenate str (not "int") to str
```

`str`과 `int`는 `+`로 바로 붙일 수 없어요. 해결 방법은 두 가지예요.

```python
count = 3
print("버그 " + str(count) + "건")
print(f"버그 {count}건")
# 결과
# 버그 3건
# 버그 3건
```

### ② 소수 모양 문자열을 int()로 바꾸기

```python
print(int("3.5"))
# ValueError: invalid literal for int() with base 10: '3.5'
```

`"3.5"`처럼 소수점이 있는 문자열은 `int()`로 바로 바꿀 수 없어요. `float("3.5")`를 쓰거나, 정수가 필요하면 `int(float("3.5"))`처럼 두 번 바꿔야 해요.

## 요약

| 상황 | 해결 |
|---|---|
| 자료형이 궁금할 때 | `type(값)` |
| 문자열 → 숫자 | `int("10")`, `float("3.5")` |
| 숫자 → 문자열 | `str(10)` 또는 f-string |
| 나누기 결과가 정수로 필요할 때 | `//` |

다음 글에서는 사용자에게 값을 입력받는 `input()`을 다뤄볼게요. `input()`은 자료형과 아주 밀접해서 이 글을 먼저 보고 오시면 이해가 쉬울 거예요!

헷갈리는 자료형이 있으면 댓글로 남겨주세요. 같이 정리해봐요!

태그: 파이썬, python, 파이썬자료형, 자료형, 형변환, type함수, 파이썬기초, 코딩입문, TypeError, 비전공자코딩
