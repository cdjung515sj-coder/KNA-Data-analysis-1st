# 03. `while` 반복문

[⬅️ 이전: for 반복문](./02_for.md)
[🏠 전체 목차로 돌아가기](../README.md)
[➡️ 다음: break와 continue](./04_break_continue.md)

---

## 💡 한 줄 요약

`while`문은 반복 횟수가 정해지지 않았을 때, 특정 조건이 `False`가 될 때까지 코드를 반복한다.

---

## ✅ 핵심 요약

| 개념           | 의미             | 사용하는 상황       |
| ------------ | -------------- | ------------- |
| `while 조건:`  | 조건이 참인 동안 반복   | 종료 시점을 모르는 반복 |
| 시작 변수        | 반복 시작 상태       | `count = 1`   |
| 종료 조건        | 반복을 멈추는 기준     | `count <= 3`  |
| 증감 코드        | 조건이 거짓이 되도록 변경 | `count += 1`  |
| `while True` | 의도적인 무한 반복     | 사용자 입력 반복     |
| `break`      | 반복문 즉시 종료      | `q` 입력 시 종료   |

---

## 📍 언제 사용하는가?

* 사용자가 종료 명령을 입력할 때까지 반복할 때
* 입력값의 누적 합계가 기준을 넘을 때까지 반복할 때
* 반복 횟수를 미리 알 수 없을 때
* 특정 상태가 발생할 때까지 계속 검사할 때
* 메뉴 프로그램을 계속 실행할 때

---

## 📌 목차

* [1. while문이란?](#1-while문이란)
* [2. 기본 구조](#2-기본-구조)
* [3. while문 체크리스트](#3-while문-체크리스트)
* [4. 무한루프](#4-무한루프)
* [5. while True와 break](#5-while-true와-break)
* [6. 사용자 입력 반복](#6-사용자-입력-반복)
* [7. 누적값 기준 반복 종료](#7-누적값-기준-반복-종료)
* [8. for문과 while문 차이](#8-for문과-while문-차이)
* [9. 자주 하는 실수](#9-자주-하는-실수)
* [10. 이해도 점검](#10-이해도-점검)

---

# 1. `while`문이란?

조건이 참인 동안 코드를 계속 반복한다.

## 기본 문법

```python
while 조건식:
    반복할 코드
```

예시:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

```text
1
2
3
```

## 동작 과정

| 반복 | `count <= 3` |     출력 | 변경 후 `count` |
| -: | ------------ | -----: | -----------: |
|  1 | `True`       |      1 |            2 |
|  2 | `True`       |      2 |            3 |
|  3 | `True`       |      3 |            4 |
| 종료 | `False`      | 실행 안 함 |            4 |

---

# 2. 기본 구조

안전한 `while`문에는 세 가지가 필요하다.

```python
count = 1          # 1. 시작값

while count <= 3:  # 2. 종료 조건
    print(count)
    count += 1     # 3. 값 변경
```

## 1. 시작값

```python
count = 1
```

반복을 시작할 기준값이다.

## 2. 종료 조건

```python
while count <= 3:
```

언젠가 `False`가 되어야 한다.

## 3. 값 변경

```python
count += 1
```

조건이 거짓이 되는 방향으로 값을 변경한다.

---

# 3. `while`문 체크리스트

`while`문을 작성할 때 다음을 확인한다.

1. 반복 전에 시작 변수가 있는가?
2. 반복을 끝낼 조건이 있는가?
3. 반복하면서 변수의 값이 변하는가?
4. 그 변화가 조건을 거짓으로 만드는 방향인가?

예시:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

`count`가 계속 증가하므로 언젠가 `5`를 초과하고 반복이 끝난다.

---

# 4. 무한루프

조건이 계속 참이면 반복문이 끝나지 않는다.

## 증감 코드가 없는 경우

```python
# count = 1

# while count <= 3:
#     print(count)
```

`count`가 계속 `1`이므로 조건이 영원히 참이다.

## 잘못된 방향으로 값이 변하는 경우

```python
# count = 1

# while count >= 1:
#     print(count)
#     count += 1
```

`count`가 계속 커지기 때문에 `count >= 1`은 계속 참이다.

## 반복문 안에서 계속 초기화하는 경우

```python
# count = 1

# while count <= 3:
#     count = 0
#     print(count)
#     count += 1
```

반복할 때마다 `count`가 다시 `0`이 되어 종료되지 않는다.

## 강제 종료

터미널에서 무한루프가 실행되면 일반적으로 다음 키를 사용한다.

```text
Ctrl + C
```

---

# 5. `while True`와 `break`

`while True`는 조건 자체가 항상 참이기 때문에 무한 반복한다.

대신 반복문 안에서 `break`를 사용해 종료한다.

```python
while True:
    text = input("입력하세요. 종료는 q: ")

    if text == "q":
        break

    print("입력값:", text)

print("입력을 종료합니다.")
```

## 동작 흐름

1. 사용자 입력을 받는다.
2. 입력값이 `q`인지 확인한다.
3. `q`이면 `break`로 반복문을 종료한다.
4. `q`가 아니면 입력값을 출력하고 다시 반복한다.

---

# 6. 사용자 입력 반복

```python
while True:
    value = input("입력: ")

    if value == "q":
        break

    print(f"입력받은 값: {value}")
```

입력값을 계속 보관할 필요가 없다면 반복할 때마다 같은 변수에 재할당해도 된다.

```python
value = input(...)
```

다음 반복에서 이전 값은 새로운 입력값으로 바뀐다.

## 대소문자와 공백 처리

```python
while True:
    value = input("종료는 q: ").strip().lower()

    if value == "q":
        break
```

이렇게 작성하면 `" Q "`를 입력해도 종료할 수 있다.

---

# 7. 누적값 기준 반복 종료

사용자가 값을 계속 입력하고, 누적 합계가 15를 넘으면 종료하는 코드이다.

```python
input_sum = 0

while True:
    user_input = int(input("값을 입력하세요: "))
    input_sum += user_input

    if input_sum > 15:
        print(f"누적 합계: {input_sum}")
        break

print("입력을 종료합니다.")
```

## 실행 예시

```text
값을 입력하세요: 5
값을 입력하세요: 6
값을 입력하세요: 7
누적 합계: 18
입력을 종료합니다.
```

## 핵심 구조

```python
누적 변수 생성

while True:
    값 입력
    누적

    if 종료 조건:
        break
```

---

# 8. `for`문과 `while`문 차이

| 구분      | `for`문      | `while`문    |
| ------- | ----------- | ----------- |
| 반복 기준   | 범위 또는 데이터   | 조건          |
| 횟수      | 주로 미리 알고 있음 | 주로 미리 모름    |
| 대표 예시   | 10번 반복      | `q` 입력까지 반복 |
| 종료 방식   | 범위가 끝나면 종료  | 조건이 거짓이면 종료 |
| 무한루프 위험 | 비교적 낮음      | 비교적 높음      |

## `for`문이 적합한 경우

```python
for i in range(5):
    print(i)
```

5번 반복한다는 사실을 알고 있다.

## `while`문이 적합한 경우

```python
while True:
    command = input("명령어: ")

    if command == "종료":
        break
```

사용자가 언제 종료할지 미리 알 수 없다.

---

# 9. 자주 하는 실수

## 9.1 증감 코드를 빼먹는 경우

```python
# count = 1

# while count <= 3:
#     print(count)
```

조건이 계속 참이므로 무한루프가 발생한다.

---

## 9.2 변수가 거짓 방향으로 변하지 않는 경우

```python
# count = 1

# while count <= 3:
#     count -= 1
```

`count`는 점점 작아지고 계속 `3 이하`이므로 종료되지 않는다.

올바른 방향:

```python
count += 1
```

---

## 9.3 `break` 위치가 잘못된 경우

```python
while True:
    value = input("입력: ")
    break

    if value == "q":
        print("종료")
```

입력 후 바로 `break`가 실행되어 조건을 검사하지 않는다.

올바른 코드:

```python
while True:
    value = input("입력: ")

    if value == "q":
        break
```

---

## 9.4 종료 조건을 너무 늦게 검사하는 경우

```python
while True:
    value = input("입력: ")

    print("입력값:", value)

    if value == "q":
        break
```

`q`도 입력값으로 출력된다.

종료값을 출력하고 싶지 않다면 먼저 검사한다.

```python
while True:
    value = input("입력: ")

    if value == "q":
        break

    print("입력값:", value)
```

---

# 10. 이해도 점검

## 퀴즈

다음 코드의 출력 결과를 예상해보자.

```python
count = 3

while count > 0:
    print(count)
    count -= 1

print("종료")
```

## 실습

사용자에게 정수를 계속 입력받다가 `0`을 입력하면 종료하는 프로그램을 작성해보자.

조건:

* 입력한 숫자의 합계를 누적한다.
* `0`은 합계에 포함하지 않는다.
* 종료 후 최종 합계를 출력한다.

실행 예시:

```text
숫자 입력: 5
숫자 입력: 3
숫자 입력: 2
숫자 입력: 0
최종 합계: 10
```

---

[⬅️ 이전: for 반복문](./02_for.md)
[🏠 전체 목차로 돌아가기](../README.md)
[⬆️ 맨 위로 이동](#03-while-반복문)
[➡️ 다음: break와 continue](./04_break_continue.md)
