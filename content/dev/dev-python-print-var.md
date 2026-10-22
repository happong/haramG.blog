---
title: 코딩 첫걸음, print()와 변수 이해하기
dashboard_id: dev-python-print-var
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

# 파이썬 print() 사용법과 변수 정리 (sep, end, f-string까지)

안녕하세요, 하해입니다! ☺️

파이썬을 처음 시작하면 가장 먼저 만나는 게 `print()`와 **변수**예요.
이번 글은 나중에 다시 찾아볼 수 있게 **문법 위주로 정리**해봤어요. 예제 코드는 모두 직접 실행해서 결과를 확인했습니다. (파이썬 3.13 기준)

## 한 줄 정리

| 개념 | 한 줄 정의 |
|---|---|
| `print()` | 괄호 안의 값을 화면에 출력하는 함수 |
| 변수 | 값에 붙이는 이름표. `이름 = 값` 으로 만든다 |

## 1. print() 기본 사용법

```python
print("안녕하세요")
print("빌드", 101, "완료")
# 결과
# 안녕하세요
# 빌드 101 완료
```

쉼표(,)로 여러 값을 넣으면 **사이에 띄어쓰기 한 칸**이 자동으로 들어가요.

### sep: 값 사이에 넣을 문자 바꾸기

```python
print("QA", "Dev", "Art", sep=" / ")
# 결과
# QA / Dev / Art
```

### end: 줄바꿈 대신 다른 문자로 끝내기

`print()`는 기본적으로 출력이 끝나면 줄을 바꿔요. `end`를 쓰면 이걸 바꿀 수 있어요.

```python
print("로딩 중", end="...")
print("완료")
# 결과
# 로딩 중...완료
```

## 2. 변수 만들기

변수는 **값에 이름표를 붙이는 것**이에요. `=` 는 "같다"가 아니라 **"오른쪽 값을 왼쪽 이름에 담아라"**라는 뜻이에요.

```python
version = "1.0.0"
print(version)
version = "1.0.1"
print(version)
# 결과
# 1.0.0
# 1.0.1
```

같은 이름에 다시 값을 넣으면 **마지막에 넣은 값**으로 바뀌어요.

### 변수 이름 규칙

| 규칙 | 가능 | 불가능 |
|---|---|---|
| 영문자, 숫자, 밑줄(_) 사용 | `build_no`, `qa2` | `build-no` |
| 숫자로 시작하면 안 됨 | `build1` | `1st_build` |
| 대소문자 구분 | `Version` 과 `version` 은 다른 변수 | |
| 파이썬 예약어는 못 씀 | | `if`, `for`, `class` |

## 3. f-string으로 변수와 문장 섞어 출력하기

따옴표 앞에 `f`를 붙이고, 중괄호 `{}` 안에 변수 이름을 넣으면 값이 그 자리에 들어가요.

```python
build_no = 102
status = "성공"
print(f"빌드 #{build_no} {status}")
# 결과
# 빌드 #102 성공
```

## 4. 자주 하는 실수

### ① 문자열에 따옴표를 빼먹음

```python
print(hello)
# NameError: name 'hello' is not defined. Did you mean: 'help'?
```

따옴표가 없으면 파이썬은 `hello`를 **변수 이름**으로 읽어요. 글자를 그대로 출력하려면 `print("hello")`처럼 따옴표로 감싸야 해요.

### ② 변수를 만들기 전에 사용

```python
print(patch_note)
patch_note = "버그 수정"
# NameError: name 'patch_note' is not defined
```

코드는 **위에서 아래로** 실행돼요. 변수는 쓰기 전에 먼저 만들어야 해요.

### ③ 숫자로 시작하는 변수 이름

```python
1st_build = 10
# SyntaxError: invalid decimal literal
```

## 요약

| 하고 싶은 것 | 코드 |
|---|---|
| 글자 출력 | `print("내용")` |
| 여러 값 출력 | `print(a, b, c)` |
| 구분자 바꾸기 | `print(a, b, sep=", ")` |
| 줄바꿈 없이 출력 | `print(a, end="")` |
| 변수 만들기 | `name = "값"` |
| 변수 넣어서 출력 | `print(f"{name}님")` |

여기까지가 파이썬의 가장 기본이에요!

궁금한 점이나 실행했는데 결과가 다르게 나온다면 댓글로 편하게 남겨주세요!

태그: 파이썬, python, 파이썬기초, print, 파이썬print, 파이썬변수, fstring, 파이썬입문, 코딩입문, 비전공자코딩
