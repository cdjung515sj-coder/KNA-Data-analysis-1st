# 02. `for` 반복문

[⬅️ 이전: 조건문](./01_if.md)
[🏠 전체 목차로 돌아가기](../README.md)
[➡️ 다음: while 반복문](./03_while.md)

---

## 💡 한 줄 요약

`for`문은 정해진 범위나 여러 데이터의 값을 하나씩 꺼내 반복할 때 사용한다.

---

## ✅ 핵심 요약

| 문법                 | 의미            | 사용하는 상황     |
| ------------------ | ------------- | ----------- |
| `for 변수 in 자료:`    | 값을 하나씩 꺼내 반복  | 리스트 전체 검사   |
| `range(끝)`         | 0부터 끝 직전까지    | 정해진 횟수 반복   |
| `range(시작, 끝)`     | 시작부터 끝 직전까지   | 숫자 범위 반복    |
| `range(시작, 끝, 간격)` | 일정 간격으로 반복    | 짝수, 역순 출력   |
| `enumerate()`      | 인덱스와 값을 함께 반환 | 순번과 값 동시 사용 |
| 중첩 `for`           | 반복문 안에서 다시 반복 | 구구단, 행과 열   |
| 누적 변수              | 반복 결과를 계속 저장  | 합계, 개수 계산   |

---

## 📍 언제 사용하는가?

* 같은 코드를 정해진 횟수만큼 반복할 때
* 리스트에 들어 있는 값을 하나씩 확인할 때
* 1부터 10까지 숫자를 순서대로 사용할 때
* 설비 측정값을 전체 검사할 때
* 합계, 개수, 최댓값을 구할 때
* 구구단처럼 두 가지 값이 동시에 변할 때

---

## 📌 목차

* [1. for문이란?](#1-for문이란)
* [2. range 함수](#2-range-함수)
* [3. 시작·끝·간격](#3-시작끝간격)
* [4. 리스트 반복](#4-리스트-반복)
* [5. range와 len](#5-range와-len)
* [6. enumerate](#6-enumerate)
* [7. 누적 패턴](#7-누적-패턴)
* [8. 개수 세기](#8-개수-세기)
* [9. 조건과 반복문](#9-조건과-반복문)
* [10. 중첩 반복문](#10-중첩-반복문)
* [11. 자주 하는 실수](#11-자주-하는-실수)
* [12. 이해도 점검](#12-이해도-점검)

---

# 1. `for`문이란?

같은 작업을 여러 번 반복할 때 사용한다.

## 기본 문법

```python
for 변수 in 반복할_자료:
    반복할 코드
```

예시:

```python
for i in range(3):
    print("안녕하세요")
```

```text
안녕하세요
안녕하세요
안녕하세요
```

`i`는 반복할 때마다 `range()`가 전달하는 값을 하나씩 받는다.

---

# 2. `range()` 함수

`range()`는 일정한 숫자 범위를 만든다.

```python
for i in range(5):
    print(i)
```

```text
0
1
2
3
4
```

`range(5)`는 0부터 4까지 값을 만든다.

끝 값인 `5`는 포함하지 않는다.

---

# 3. 시작·끝·간격

## `range(끝)`

```python
for i in range(3):
    print(i)
```

```text
0
1
2
```

## `range(시작, 끝)`

```python
for i in range(1, 6):
    print(i)
```

```text
1
2
3
4
5
```

## `range(시작, 끝, 간격)`

```python
for i in range(0, 11, 2):
    print(i)
```

```text
0
2
4
6
8
10
```

## 홀수 출력

```python
for i in range(1, 11, 2):
    print(i)
```

```text
1
3
5
7
9
```

## 역순 출력

```python
for i in range(10, 0, -1):
    print(i)
```

```text
10
9
8
7
6
5
4
3
2
1
```

## 역순 짝수 출력

```python
for i in range(10, 0, -2):
    print(i)
```

```text
10
8
6
4
2
```

## 동작하지 않는 범위

```python
for i in range(0, 10, -2):
    print(i)
```

아무것도 출력되지 않는다.

* 시작값은 `0`
* 끝값은 `10`
* 간격은 음수

음수 간격은 숫자가 작아지는 방향이어야 하는데, 시작값보다 끝값이 더 크기 때문에 반복할 수 없다.

---

# 4. 리스트 반복

리스트의 값을 하나씩 직접 꺼낼 수 있다.

```python
temps = [33, 23, 45, 32, 28]

for temp in temps:
    print(temp)
```

```text
33
23
45
32
28
```

`temp`에는 반복할 때마다 리스트의 값이 하나씩 들어간다.

## 조건과 함께 사용

```python
temps = [70, 85, 90, 75]

for temp in temps:
    if temp >= 80:
        print("경고:", temp)
```

```text
경고: 85
경고: 90
```

---

# 5. `range()`와 `len()`

인덱스가 필요한 경우 리스트 길이를 이용할 수 있다.

```python
numbers = [4, 7, 6]

for i in range(len(numbers)):
    print(i, numbers[i])
```

```text
0 4
1 7
2 6
```

* `len(numbers)`는 `3`
* `range(3)`은 `0, 1, 2`
* 각 숫자를 인덱스로 사용한다.

## 값만 필요하다면

```python
for number in numbers:
    print(number)
```

이 방법이 더 간단하다.

## 인덱스도 필요하다면

`enumerate()`를 사용하는 편이 더 읽기 쉽다.

---

# 6. `enumerate()`

리스트의 인덱스와 값을 함께 가져온다.

```python
temps = [33, 23, 45, 32, 28]

for item in enumerate(temps):
    print(item)
```

```text
(0, 33)
(1, 23)
(2, 45)
(3, 32)
(4, 28)
```

`enumerate()`는 `(인덱스, 값)` 형태의 튜플을 반환한다.

## 언패킹하여 사용

```python
for idx, temp in enumerate(temps):
    print(f"인덱스: {idx}, 온도: {temp}")
```

```text
인덱스: 0, 온도: 33
인덱스: 1, 온도: 23
인덱스: 2, 온도: 45
인덱스: 3, 온도: 32
인덱스: 4, 온도: 28
```

## 순번을 1부터 출력

```python
for idx, temp in enumerate(temps):
    print(f"{idx + 1}번째 온도: {temp}")
```

또는 `start` 값을 지정할 수 있다.

```python
for idx, temp in enumerate(temps, start=1):
    print(f"{idx}번째 온도: {temp}")
```

---

# 7. 누적 패턴

반복하면서 값을 계속 더할 때 누적 변수를 사용한다.

```python
total = 0

for i in range(1, 6):
    total += i

print("합계:", total)
```

```text
합계: 15
```

## 동작 과정

| 반복 | `i` | `total` |
| -: | --: | ------: |
| 시작 |   - |       0 |
|  1 |   1 |       1 |
|  2 |   2 |       3 |
|  3 |   3 |       6 |
|  4 |   4 |      10 |
|  5 |   5 |      15 |

## 누적 변수는 반복문 밖에 만든다

잘못된 코드:

```python
for i in range(1, 6):
    total = 0
    total += i

print(total)
```

```text
5
```

반복할 때마다 `total`이 다시 `0`이 되기 때문에 누적되지 않는다.

올바른 코드:

```python
total = 0

for i in range(1, 6):
    total += i
```

---

# 8. 개수 세기

조건에 맞는 값의 개수를 셀 때는 `count` 변수를 사용한다.

```python
count = 0

for i in range(1, 11):
    if i > 5:
        count += 1

print(count)
```

```text
5
```

`6, 7, 8, 9, 10` 총 5개이다.

## 합계와 개수의 차이

```python
total += i
```

조건에 맞는 값 자체를 더한다.

```python
count += 1
```

조건에 맞을 때마다 개수만 1씩 증가한다.

---

# 9. 조건과 반복문

## 4의 배수만 누적

```python
total = 0

for i in range(1, 16):
    if i % 4 == 0:
        total += i

print(total)
```

```text
24
```

`4 + 8 + 12 = 24`

## 조건에 맞는 새 리스트 만들기

```python
temps = [1, 5, 2, 7, 4, 8, 10, 3]

low = []
high = []

for temp in temps:
    if temp < 5:
        low.append(temp)
    else:
        high.append(temp)

print("low:", low)
print("high:", high)
```

```text
low: [1, 2, 4, 3]
high: [5, 7, 8, 10]
```

## 모든 값 변환하기

```python
temps = [1, 5, 2, 7]
tripled = []

for temp in temps:
    tripled.append(temp * 3)

print(tripled)
```

```text
[3, 15, 6, 21]
```

---

# 10. 중첩 반복문

반복문 안에 또 다른 반복문을 작성하는 구조이다.

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

```text
1 1
1 2
2 1
2 2
3 1
3 2
```

바깥 반복 한 번마다 안쪽 반복이 처음부터 끝까지 실행된다.

## 구구단

```python
for dan in range(2, 10):
    print(f"=== {dan}단 ===")

    for su in range(1, 10):
        print(f"{dan} × {su} = {dan * su}")
```

* 바깥 반복문: 몇 단인지 결정
* 안쪽 반복문: 1부터 9까지 곱할 수 결정

## 짝수 단만 출력

방법 1: `range()` 간격 사용

```python
for dan in range(2, 10, 2):
    for su in range(1, 10):
        print(f"{dan} × {su} = {dan * su}")
```

방법 2: 조건문 사용

```python
for dan in range(2, 10):
    if dan % 2 == 0:
        for su in range(1, 10):
            print(f"{dan} × {su} = {dan * su}")
```

단순히 짝수 단만 필요하다면 첫 번째 방법이 더 간단하다.

---

# 11. 자주 하는 실수

## 11.1 끝 값을 포함한다고 생각하는 경우

```python
range(1, 5)
```

결과는 `1, 2, 3, 4`이다.

`5`는 포함하지 않는다.

---

## 11.2 누적 변수를 반복문 안에 만드는 경우

```python
for i in range(5):
    total = 0
    total += i
```

매번 초기화되어 누적되지 않는다.

---

## 11.3 리스트 값을 직접 사용할 수 있는데 인덱스를 복잡하게 쓰는 경우

복잡한 코드:

```python
for i in range(len(temps)):
    print(temps[i])
```

값만 필요하다면:

```python
for temp in temps:
    print(temp)
```

---

## 11.4 `i`가 특별한 기능을 가진다고 생각하는 경우

```python
for apple in range(3):
    print(apple)
```

정상적으로 실행된다.

`i`는 반복 변수로 자주 쓰는 관습적인 이름일 뿐이다.

가능하면 의미 있는 이름을 사용한다.

```python
for temp in temps:
    print(temp)
```

---

## 11.5 들여쓰기 위치가 잘못된 경우

```python
total = 0

for i in range(1, 6):
    total += i
    print(total)
```

반복할 때마다 중간 결과를 출력한다.

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

반복이 끝난 후 최종 결과만 출력한다.

---

# 12. 이해도 점검

## 퀴즈

다음 코드의 출력 결과를 예상해보자.

```python
total = 0

for i in range(2, 11, 2):
    total += i

print(total)
```

## 실습

다음 리스트에서 80 이상인 값만 새 리스트에 저장하고, 개수와 합계를 출력해보자.

```python
temps = [72, 85, 90, 68, 88, 77]
```

예상 출력:

```text
경고 온도: [85, 90, 88]
경고 개수: 3
경고 온도 합계: 263
```

조건:

* 빈 리스트를 만든다.
* `for`문과 `if`문을 사용한다.
* 개수를 저장할 변수를 만든다.
* 합계를 저장할 변수를 만든다.

---

[⬅️ 이전: 조건문](./01_if.md)
[🏠 전체 목차로 돌아가기](../README.md)
[⬆️ 맨 위로 이동](#02-for-반복문)
[➡️ 다음: while 반복문](./03_while.md)
