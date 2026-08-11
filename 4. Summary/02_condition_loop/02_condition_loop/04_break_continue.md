# 04. `break`와 `continue`

[⬅️ 이전: while 반복문](./03_while.md)
[🏠 전체 목차로 돌아가기](../README.md)

---

## 💡 한 줄 요약

`break`는 반복문 전체를 종료하고, `continue`는 현재 반복만 건너뛰고 다음 반복으로 이동한다.

---

## ✅ 핵심 요약

| 문법                   | 동작                         | 사용하는 상황        |
| -------------------- | -------------------------- | -------------- |
| `break`              | 반복문 즉시 종료                  | 이상값 발견 시 검사 중단 |
| `continue`           | 현재 반복만 건너뜀                 | 필요 없는 값 제외     |
| `while True + break` | 종료 조건을 내부에서 결정             | 사용자 입력 반복      |
| `for-else`           | `break` 없이 끝났을 때 `else` 실행 | 검색 성공 여부 판단    |

---

## 📍 언제 사용하는가?

* 설비 이상값을 발견하면 검사를 즉시 중단할 때
* 짝수나 결측값처럼 필요 없는 값을 건너뛸 때
* 사용자가 `q`를 입력하면 반복을 종료할 때
* 특정 값을 찾았는지 확인할 때
* 반복문 전체를 끝낼지, 한 번만 넘길지 결정할 때

---

## 📌 목차

* [1. break](#1-break)
* [2. continue](#2-continue)
* [3. break와 continue 차이](#3-break와-continue-차이)
* [4. while문에서 break](#4-while문에서-break)
* [5. for문에서 break](#5-for문에서-break)
* [6. continue 활용](#6-continue-활용)
* [7. 반복문 else](#7-반복문-else)
* [8. 중첩 반복문에서 break](#8-중첩-반복문에서-break)
* [9. 자주 하는 실수](#9-자주-하는-실수)
* [10. 이해도 점검](#10-이해도-점검)

---

# 1. `break`

현재 실행 중인 반복문을 즉시 종료한다.

```python
for i in range(1, 6):
    if i == 3:
        break

    print(i)
```

```text
1
2
```

`i`가 `3`이 되는 순간 반복문이 끝난다.

`3`, `4`, `5`는 출력되지 않는다.

## 동작 흐름

```text
i = 1 → 출력
i = 2 → 출력
i = 3 → break 실행
반복 종료
```

---

# 2. `continue`

현재 반복에서 아래 코드를 건너뛰고 다음 반복으로 이동한다.

```python
for i in range(1, 7):
    if i % 2 == 0:
        continue

    print(i)
```

```text
1
3
5
```

짝수일 때 `continue`가 실행되어 `print(i)`를 건너뛴다.

반복문 자체는 종료되지 않는다.

---

# 3. `break`와 `continue` 차이

```python
for i in range(1, 6):
    if i == 3:
        break

    print(i)
```

```text
1
2
```

`break`는 반복 전체를 끝낸다.

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

```text
1
2
4
5
```

`continue`는 `3`인 회차만 건너뛴다.

## 비교표

| 구분     | `break` | `continue` |
| ------ | ------- | ---------- |
| 현재 반복  | 종료      | 건너뜀        |
| 다음 반복  | 실행하지 않음 | 실행함        |
| 반복문 전체 | 종료      | 유지         |
| 대표 상황  | 이상값 발견  | 제외할 값 발견   |

---

# 4. `while`문에서 `break`

`while True`와 함께 자주 사용한다.

```python
while True:
    value = input("입력하세요. 종료는 q: ")

    if value == "q":
        break

    print(f"입력값: {value}")

print("입력을 종료합니다.")
```

`q`를 입력하기 전까지 계속 반복한다.

## 누적 합계 기준 종료

```python
total = 0

while True:
    value = int(input("값 입력: "))
    total += value

    if total > 15:
        print(f"누적 합계: {total}")
        break
```

누적 합계가 15를 넘는 순간 반복문이 종료된다.

---

# 5. `for`문에서 `break`

설비 측정값을 검사하다가 이상값이 발생하면 즉시 중단할 수 있다.

```python
values = [50, 70, 85, 95, 60]

for value in values:
    if value > 80:
        print("이상 발생:", value)
        break

    print("정상:", value)
```

```text
정상: 50
정상: 70
이상 발생: 85
```

`85`에서 반복이 종료되기 때문에 뒤의 `95`, `60`은 검사하지 않는다.

## 사용자 입력 반복 중 이상값 발견

```python
count = int(input("측정 횟수: "))

for i in range(count):
    value = int(input("측정값: "))

    if value > 80:
        print("이상 발생")
        print("이상 발생 회차:", i + 1)
        break

    print("정상 상태")
```

> 전체 가동 횟수가 아니라 실제 이상 발생 회차를 출력하려면 `i + 1`을 사용한다.

---

# 6. `continue` 활용

## 짝수 제외

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue

    print(i)
```

## 음수 제외하고 합계 구하기

```python
numbers = [10, -3, 5, -1, 8]

total = 0

for number in numbers:
    if number < 0:
        continue

    total += number

print(total)
```

```text
23
```

음수는 건너뛰고 양수만 더한다.

## 빈 문자열 제외

```python
names = ["펌프", "", "모터", "", "압축기"]

for name in names:
    if name == "":
        continue

    print(name)
```

```text
펌프
모터
압축기
```

---

# 7. 반복문 `else`

파이썬에서는 반복문에도 `else`를 붙일 수 있다.

`break`가 실행되지 않고 반복이 정상적으로 끝나면 `else`가 실행된다.

```python
numbers = [10, 20, 30]
target = 20

for number in numbers:
    if number == target:
        print("값을 찾았습니다.")
        break
else:
    print("값이 없습니다.")
```

```text
값을 찾았습니다.
```

## 값이 없는 경우

```python
target = 99

for number in numbers:
    if number == target:
        print("값을 찾았습니다.")
        break
else:
    print("값이 없습니다.")
```

```text
값이 없습니다.
```

## 구조 이해하기

* 값을 찾으면 `break`
* `break`가 실행되면 `else`는 실행되지 않음
* 끝까지 찾지 못하면 `else` 실행

검색 기능을 만들 때 사용할 수 있다.

---

# 8. 중첩 반복문에서 `break`

`break`는 자신이 들어 있는 가장 가까운 반복문 하나만 종료한다.

```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break

        print(i, j)
```

```text
1 1
2 1
3 1
```

안쪽 반복문만 종료된다.

바깥쪽 반복문은 계속 실행된다.

## 바깥 반복문까지 종료하기

플래그 변수를 사용할 수 있다.

```python
found = False

for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            found = True
            break

    if found:
        break

print("반복 종료")
```

다만 초급 단계에서는 중첩 반복문을 지나치게 복잡하게 만들지 않는 것이 좋다.

---

# 9. 자주 하는 실수

## 9.1 `continue` 아래 코드는 실행되지 않음

```python
for i in range(5):
    if i == 2:
        continue
        print("실행되지 않음")
```

`continue`가 실행되는 순간 다음 반복으로 넘어간다.

---

## 9.2 `break` 뒤에 중요한 코드를 작성하는 경우

```python
while True:
    value = input("입력: ")

    if value == "q":
        break
        print("종료합니다.")
```

`break` 뒤의 출력문은 실행되지 않는다.

수정:

```python
while True:
    value = input("입력: ")

    if value == "q":
        print("종료합니다.")
        break
```

---

## 9.3 `break`가 조건문만 끝낸다고 생각하는 경우

`break`는 `if`문을 끝내는 명령어가 아니다.

반복문을 끝낸다.

```python
for i in range(5):
    if i == 2:
        break
```

`for`문 전체가 종료된다.

---

## 9.4 `continue`를 불필요하게 사용하는 경우

```python
for temp in temps:
    if temp >= 80:
        print(temp)
```

이 정도 조건은 `continue` 없이 작성하는 편이 더 간단하다.

`continue`가 코드를 더 읽기 쉽게 만들 때 사용한다.

---

# 10. 이해도 점검

## 퀴즈

다음 코드의 출력 결과를 예상해보자.

```python
for i in range(1, 7):
    if i == 2:
        continue

    if i == 5:
        break

    print(i)
```

## 실습

다음 설비 온도를 순서대로 검사하는 프로그램을 작성해보자.

```python
temps = [70, 75, -1, 82, 95, 60]
```

조건:

* `-1`은 잘못된 측정값이므로 `continue`로 건너뛴다.
* 90 이상을 발견하면 `"위험 온도 발견"`을 출력한다.
* 위험 온도를 발견하면 `break`로 검사를 종료한다.
* 정상적으로 검사한 값은 `"검사 완료: 값"` 형식으로 출력한다.

예상 출력:

```text
검사 완료: 70
검사 완료: 75
검사 완료: 82
위험 온도 발견: 95
```

---

[⬅️ 이전: while 반복문](./03_while.md)
[🏠 전체 목차로 돌아가기](../README.md)
[⬆️ 맨 위로 이동](#04-break와-continue)
