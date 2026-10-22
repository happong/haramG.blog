---
title: 파이썬 break와 continue
dashboard_id: dev-python-03-break-continue
category: dev
status: draft
stage: draft
visited: 
planned: 
published: 
tistory_done: false
tistory_published: 
season: false
season_end: 
priority: 2
photos: 0
place_shots: 0
no_place: false
---

## 경험 메모

for문 글 마지막에 다음 편으로 예고함. 공부하면서 헷갈렸던 점이나 직접 실행해 본 코드를 적어주세요.

## 네이버 초안

[확인 필요 — 확인 후 이 블록은 지우고 올려주세요]
- 제목 제안: break와 continue로 반복문 멈추고 건너뛰기
- 메모가 비어 있어서 공부하며 헷갈렸던 점 같은 개인 경험은 넣지 않았어요. 있으면 알려주세요.

안녕하세요! 하해입니다.

오늘은 break와 continue에 대해 다뤄보려 해요. 지난 글에서 for문으로 "같은 작업을 여러 번 반복"하는 걸 배웠다면, 오늘 배울 break와 continue는 반복을 "중간에 멈추거나 건너뛰는" 방법이에요! 마지막에 퀴즈도 있으니 함께 풀어보면 좋을 것 같아요.

break와 continue란?

- break: 반복문을 그 자리에서 완전히 끝내요.
- continue: 이번 차례만 건너뛰고, 다음 차례로 넘어가요.

게임 PM 업무로 비유하면,
- break는 QA 중에 "출시를 막는 치명적인 버그를 찾으면 테스트를 바로 멈춰라"
- continue는 "이번 빌드에 포함 안 된 기능은 넘어가고 다음 항목을 테스트해라"
와 비슷해요.

break 사용하기

bugs = ["Minor", "Minor", "Critical", "Minor"]
for bug in bugs:
    if bug == "Critical":
        print("치명적 버그 발견! 테스트 중단")
        break
    print(bug, "버그 기록")
#결과
Minor 버그 기록
Minor 버그 기록
치명적 버그 발견! 테스트 중단

리스트에 "Minor"가 하나 더 남아 있지만, break를 만나는 순간 for문이 끝나서 더 이상 반복하지 않아요.

continue 사용하기

features = ["로그인", "결제(미포함)", "랭킹", "채팅(미포함)"]
for feature in features:
    if "미포함" in feature:
        continue
    print(feature, "테스트 완료")
#결과
로그인 테스트 완료
랭킹 테스트 완료

continue를 만나면 그 아래 코드(print)는 실행하지 않고 바로 다음 항목으로 넘어가요.

한눈에 비교

- break → 반복 "끝"
- continue → 이번 차례만 "건너뛰기"

중요한 점 하나! break는 가장 가까운 반복문 하나만 빠져나와요

for문 안에 for문이 있을 때 안쪽에서 break를 쓰면, 안쪽 for문만 끝나고 바깥 for문은 계속 돌아요.

for team in ["QA", "Dev"]:
    for day in [1, 2, 3]:
        if day == 2:
            break
        print(team, day, "일차")
#결과
QA 1 일차
Dev 1 일차

안쪽 for문은 day가 2일 때 끝나지만, 바깥 for문은 "Dev"까지 계속 돌아요. 이 부분 꼭 기억해주세요!

콜론(:)과 들여쓰기도 그대로예요

break와 continue는 보통 if문 안에 들어가요. 그래서 if문 끝의 콜론(:)과 들여쓰기를 지난 글들에서 배운 것처럼 똑같이 맞춰줘야 해요.

자주 하는 실수

반복문 밖에서 break를 쓰면 에러가 나요.

score = 90
if score >= 80:
    break
#결과
SyntaxError: 'break' outside loop

break와 continue는 for문 같은 반복문 안에서만 쓸 수 있어요.

실무에서 이렇게 쓰여요

빌드 로그를 한 줄씩 보면서, 빈 줄은 건너뛰고 에러가 나오면 거기서 멈추는 코드예요.

logs = ["빌드 시작", "", "에셋 로드", "Error: 텍스처 누락", "빌드 완료"]
for log in logs:
    if log == "":
        continue
    if log.startswith("Error"):
        print("에러 발견 →", log)
        break
    print("확인:", log)
#결과
확인: 빌드 시작
확인: 에셋 로드
에러 발견 → Error: 텍스처 누락

지난 글들에서 배운 for문, if문에 break와 continue까지 더하니까, 반복을 훨씬 원하는 대로 다룰 수 있어요. 재밌죠!

간단한 퀴즈!

그럼 마지막으로 간단한 문제를 내도록 하겠습니다. 어렵지 않으니 다들 풀어보시고 답도 맞혀보세요!

1. 코드 읽기
for i in range(1, 6):
    if i == 4:
        break
    print(i)
위 코드를 실행하면 무엇이 출력될까요?

2. 빈칸 채우기
아래 코드가 짝수만 건너뛰고 1, 3, 5를 출력하도록 빈칸을 채워보세요.
for i in range(1, 6):
    if i % 2 == 0:
        _____
    print(i)

3. 코드 고치기
아래 코드는 에러가 납니다. 무엇이 문제일까요?
level = 10
if level > 5:
    continue

4. 출력 결과 맞추기
for name in ["QA", "", "Dev", "Art"]:
    if name == "":
        continue
    if name == "Art":
        break
    print(name)
위 코드를 실행하면 무엇이 출력될까요?

정답은..! 모두 직접 실행을 한 번 해보시죠!

다 같이 즐거운 코드 공부 ♬ break와 continue까지 알면 반복문을 원하는 순간에 멈추고, 필요 없는 건 건너뛸 수 있어요!

#Python #파이썬 #파이썬기초 #파이썬독학 #파이썬공부 #코딩공부 #프로그래밍기초 #개발자공부 #비전공자코딩 #코딩입문 #break #continue #파이썬break #파이썬continue #반복문 #파이썬반복문 #for문 #파이썬문법 #코딩기초 #SyntaxError #개발자되기 #코딩스터디 #혼자공부하는파이썬 #프로그래밍입문 #IT공부 #직장인코딩 #직무전환 #PM #커리어전환 #실무코딩

편하실 때 코드 실행해보시고, 퀴즈 정답 확인 필요하시면 말씀해주세요!

## 티스토리 초안

# 파이썬 break와 continue 차이 정리 (중첩 반복문, 자주 나는 에러, 연습문제 정답 포함)

안녕하세요, 하해입니다! ☺️

`break`는 **반복문을 끝내고**, `continue`는 **이번 차례만 건너뛰고 다음 차례로 넘어가요.**
이름은 짧지만 헷갈리기 쉬워서, 차이와 자주 쓰는 패턴을 표와 예제로 정리했어요. (파이썬 3.13 기준, 예제는 모두 직접 실행해서 확인했어요)

## 1. 한눈에 비교

| 구분 | `break` | `continue` |
|---|---|---|
| 하는 일 | 반복문을 즉시 종료 | 이번 차례의 남은 코드를 건너뜀 |
| 다음 동작 | 반복문 다음 줄로 이동 | 다음 차례 반복으로 이동 |
| 자주 쓰는 곳 | 원하는 값을 찾았을 때 | 처리하지 않을 값을 걸러낼 때 |
| 쓸 수 있는 곳 | 반복문 안에서만 | 반복문 안에서만 |

## 2. break: 찾으면 바로 멈추기

```python
orders = [12000, 8000, 55000, 3000]
for price in orders:
    if price >= 50000:
        print("고액 주문 발견:", price)
        break
    print("일반 주문:", price)
# 결과
# 일반 주문: 12000
# 일반 주문: 8000
# 고액 주문 발견: 55000
```

55000을 찾은 뒤에는 남은 3000을 확인하지 않고 반복이 끝나요.

## 3. continue: 조건에 맞는 값만 건너뛰기

```python
scores = [80, -1, 95, -1, 70]
total = 0
for s in scores:
    if s < 0:
        continue
    total += s
print("유효 점수 합계:", total)
# 결과
# 유효 점수 합계: 245
```

-1(미응시)은 `continue`로 건너뛰어서 합계에 들어가지 않아요.

## 4. 중첩 반복문에서는 가장 가까운 반복문 하나만

```python
for row in range(1, 4):
    for col in range(1, 4):
        if col == 3:
            break
        print(row, col)
# 결과
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2
```

`break`는 안쪽 `for col` 반복만 끝내요. 바깥 `for row` 반복은 3까지 계속돼요. `continue`도 마찬가지로 가장 가까운 반복문에만 적용돼요.

## 5. 자주 나는 에러와 실수

### ① 반복문 밖에서 사용

```python
x = 5
if x > 3:
    break
# SyntaxError: 'break' outside loop
```

```python
x = 5
if x > 3:
    continue
# SyntaxError: 'continue' not properly in loop
```

에러 메시지는 파이썬 3.13 기준이에요. 버전에 따라 문장이 조금 다를 수 있어요.

### ② continue 아래 코드가 실행될 거라고 생각함

| 상황 | 결과 |
|---|---|
| `continue` 다음 줄에 `print()` | 그 차례에는 `print()`가 실행되지 않음 |
| `break` 다음 줄에 코드 | 반복이 끝나서 실행되지 않음 |

## 6. 연습문제

**문제 1.** 1부터 10까지 중 3의 배수만 건너뛰고 한 줄로 출력하세요.

**문제 2.** 아래 리스트에서 처음 나오는 음수를 찾아 출력하고 멈추세요.

```python
nums = [4, 7, 0, -2, 5, -8]
```

**문제 3.** 아래 코드의 출력 결과는?

```python
for i in range(5):
    if i == 1:
        continue
    if i == 3:
        break
    print(i)
```

## 7. 정답과 해설

**문제 1**

```python
for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n, end=" ")
# 결과
# 1 2 4 5 7 8 10
```

**문제 2**

```python
nums = [4, 7, 0, -2, 5, -8]
for n in nums:
    if n < 0:
        print("첫 음수:", n)
        break
# 결과
# 첫 음수: -2
```

-2를 찾는 순간 멈추기 때문에 -8은 확인하지 않아요.

**문제 3**

```python
for i in range(5):
    if i == 1:
        continue
    if i == 3:
        break
    print(i)
# 결과
# 0
# 2
```

1은 `continue`로 건너뛰고, 3에서 `break`로 끝나서 0과 2만 출력돼요.

## 요약

| 하고 싶은 것 | 코드 |
|---|---|
| 원하는 값을 찾으면 반복 종료 | `if 조건: break` |
| 특정 값만 건너뛰기 | `if 조건: continue` |
| 중첩 반복문에서 break | 가장 가까운 반복문 하나만 종료 |
| 반복문 밖에서 사용 | `SyntaxError` |

헷갈리는 예제가 있으면 댓글로 편하게 물어봐주세요!

태그: 파이썬, python, 파이썬break, 파이썬continue, break, continue, 반복문, 중첩반복문, 파이썬기초, 코딩입문
