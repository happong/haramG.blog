---
title: input()으로 사용자와 대화하는 법
dashboard_id: dev-python-input
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

# 파이썬 input() 사용법: 입력값은 항상 문자열! int() 변환과 여러 값 입력받기

안녕하세요, 하해입니다! ☺️

`input()`은 프로그램이 **사용자에게 값을 입력받는** 함수예요.
처음 쓸 때 거의 모두가 한 번씩 겪는 실수가 있어서, 그 부분을 중심으로 정리했어요. (파이썬 3.13 기준, 예제는 모두 직접 실행해서 확인했어요)

## 핵심 한 줄

> **`input()`으로 받은 값은 숫자를 입력해도 항상 문자열(`str`)이에요.**

## 1. 기본 사용법

```python
name = input("이름을 입력하세요: ")
print(f"{name}님, 반가워요!")
```

실행 예시 (하해 를 입력한 경우)

```
이름을 입력하세요: 하해
하해님, 반가워요!
```

괄호 안의 문장은 입력 전에 화면에 보여주는 **안내 문구**예요. 사용자가 입력하고 엔터를 누르면, 입력한 내용이 변수에 담겨요.

## 2. 입력값은 항상 문자열

```python
age = input("나이: ")
print(type(age))
```

실행 예시 (30 을 입력한 경우)

```
나이: 30
<class 'str'>
```

숫자 `30`을 입력해도 자료형은 `str`이에요.

## 3. 그래서 생기는 실수: 더하기가 이상해요

```python
a = input("첫 번째 숫자: ")
b = input("두 번째 숫자: ")
print(a + b)
```

실행 예시 (10, 5 를 입력한 경우)

```
첫 번째 숫자: 10
두 번째 숫자: 5
105
```

`15`가 아니라 `105`가 나와요. 문자열끼리 `+`를 하면 **글자를 이어 붙이기** 때문이에요.

### 해결: int()로 감싸기

```python
a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
print(a + b)
```

실행 예시 (10, 5 를 입력한 경우)

```
첫 번째 숫자: 10
두 번째 숫자: 5
15
```

## 4. 한 줄에 여러 값 입력받기

```python
a, b = map(int, input("숫자 두 개(띄어쓰기): ").split())
print(a * b)
```

실행 예시 (3 4 를 입력한 경우)

```
숫자 두 개(띄어쓰기): 3 4
12
```

| 부분 | 하는 일 |
|---|---|
| `input()` | `"3 4"` 를 문자열로 받음 |
| `.split()` | 띄어쓰기 기준으로 나눠서 `["3", "4"]` |
| `map(int, ...)` | 각각을 `int`로 바꿈 |
| `a, b = ...` | 두 변수에 차례로 담음 |

## 5. 숫자가 아닌 값을 입력하면?

```python
n = int(input("숫자: "))
```

실행 예시 (열 을 입력한 경우)

```
숫자: 열
ValueError: invalid literal for int() with base 10: '열'
```

`int()`는 숫자 모양의 문자열만 바꿀 수 있어요.

## 요약

| 하고 싶은 것 | 코드 |
|---|---|
| 글자 입력받기 | `name = input("안내: ")` |
| 정수 입력받기 | `n = int(input("안내: "))` |
| 실수 입력받기 | `x = float(input("안내: "))` |
| 여러 정수 한 줄에 | `a, b = map(int, input().split())` |

`input()` + `int()` 조합은 자주 쓰이니까 꼭 익혀두세요!

직접 실행해보다가 막히는 부분이 있으면 댓글로 알려주세요!

태그: 파이썬, python, 파이썬input, input함수, 파이썬입력, 형변환, split, map함수, 파이썬기초, 코딩입문
