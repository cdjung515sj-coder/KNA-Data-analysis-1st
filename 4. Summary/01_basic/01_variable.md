# 01. 변수와 기본 자료형

[🏠 전체 목차로 돌아가기](../README.md)
[➡️ 다음: 문자열](./02_string.md)

---

## 📌 목차

* [1. 변수란?](#1-변수란)
* [2. 변수 만들기](#2-변수-만들기)
* [3. 기본 자료형](#3-기본-자료형)
* [4. type 함수](#4-type-함수)
* [5. 재할당](#5-재할당)
* [6. 복합 할당 연산자](#6-복합-할당-연산자)
* [7. 변수 이름 규칙](#7-변수-이름-규칙)
* [8. 주의할 점](#8-주의할-점)
* [9. 핵심 요약](#9-핵심-요약)
* [10. 이해도 점검](#10-이해도-점검)

---

# summary

| 개념       | 설명             | 예시                  |
| -------- | -------------- | ------------------- |
| 변수       | 값을 저장해 사용하는 이름 | `temp = 80`         |
| `int`    | 정수             | `count = 5`         |
| `float`  | 실수             | `temp = 36.5`       |
| `str`    | 문자열            | `name = "펌프"`       |
| `bool`   | 참·거짓           | `is_running = True` |
| `None`   | 값이 없음          | `result = None`     |
| `type()` | 자료형 확인         | `type(temp)`        |
| 재할당      | 변수의 값을 변경      | `temp = 90`         |
| `+=`     | 더한 결과를 재할당     | `count += 1`        |


---
# 1. 변수란?

변수는 값을 저장해두는 이름표이다.

예를 들어 설비의 온도 `85`를 여러 번 사용해야 한다면 매번 숫자를 직접 작성하는 대신 변수에 저장할 수 있다.

```python
temp = 85

print(temp)
print(temp + 10)
```

```text
85
95
```

> 변수는 데이터를 담는 상자라기보다, 저장된 값을 가리키는 이름표라고 이해하면 좋다.

---

# 2. 변수 만들기

## 기본 문법

```python
변수명 = 값
```

예시:

```python
machine = "펌프"
temp = 78
pressure = 3.5
is_running = True
```

`=`은 수학에서 말하는 “같다”가 아니라 오른쪽의 값을 왼쪽 변수에 저장하는 **할당 연산자**이다.

```python
temp = 78
```

위 코드는 다음 의미이다.

> 숫자 `78`을 `temp`라는 변수에 저장한다.

---

# 3. 기본 자료형

파이썬에서는 값의 종류를 자료형이라고 한다.

## 3.1 정수 `int`

소수점이 없는 숫자이다.

```python
temp = 78
count = 5
year = 2026
```

```python
print(type(temp))
```

```text
<class 'int'>
```

### 사용하는 상황

* 설비 개수
* 사람 수
* 반복 횟수
* 정수 형태의 온도
* 점수

---

## 3.2 실수 `float`

소수점이 있는 숫자이다.

```python
temperature = 36.5
pressure = 2.8
vibration = 0.23
```

```python
print(type(temperature))
```

```text
<class 'float'>
```

### 사용하는 상황

* 체온
* 진동값
* 압력값
* 평균
* 비율

---

## 3.3 문자열 `str`

글자나 문장을 저장하는 자료형이다.

문자열은 작은따옴표 또는 큰따옴표로 감싼다.

```python
machine = "펌프"
status = "정상"
code = "EQP-001"
```

```python
print(type(machine))
```

```text
<class 'str'>
```

숫자처럼 보이더라도 따옴표로 감싸면 문자열이다.

```python
a = 123
b = "123"

print(type(a))
print(type(b))
```

```text
<class 'int'>
<class 'str'>
```

---

## 3.4 불리언 `bool`

참과 거짓을 나타내는 자료형이다.

```python
is_running = True
has_error = False
```

불리언은 조건문의 판단 결과로 자주 사용된다.

```python
temp = 85

print(temp > 80)
```

```text
True
```

> `True`와 `False`의 첫 글자는 반드시 대문자로 작성한다.

---

## 3.5 값이 없음을 나타내는 `None`

아직 값이 없거나 반환할 값이 없다는 뜻이다.

```python
result = None

print(result)
print(type(result))
```

```text
None
<class 'NoneType'>
```

리스트의 `append()`, `sort()`처럼 원본을 수정하지만 별도의 결과를 반환하지 않는 메서드를 출력하면 `None`이 나타날 수 있다.

```python
numbers = [3, 1, 2]

print(numbers.sort())
```

```text
None
```

---

# 4. `type()` 함수

`type()`은 값이나 변수의 자료형을 확인하는 내장함수이다.

```python
name = "PUMP_A"
temp = 78
pressure = 3.4
is_running = True

print(type(name))
print(type(temp))
print(type(pressure))
print(type(is_running))
```

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

## 언제 사용하는가?

* 변수에 어떤 자료형이 저장되어 있는지 확인할 때
* 연산 오류의 원인을 찾을 때
* 사용자 입력값이 문자열인지 확인할 때
* 리스트 요소의 자료형을 확인할 때

---

# 5. 재할당

이미 만들어진 변수에 새로운 값을 다시 저장하는 것을 재할당이라고 한다.

```python
temp = 70
print(temp)

temp = 90
print(temp)
```

```text
70
90
```

기존의 `70` 대신 새로운 값 `90`을 가리키게 된다.

## 자기 자신의 값을 사용한 재할당

```python
num = 1
num = num + 1

print(num)
```

```text
2
```

동작 순서:

1. 오른쪽의 기존 `num` 값을 가져온다.
2. 기존 값 `1`에 `1`을 더한다.
3. 결과 `2`를 다시 `num`에 저장한다.

---

# 6. 복합 할당 연산자

자기 자신의 값에 연산한 결과를 다시 저장할 때 짧게 작성할 수 있다.

```python
num = 10

num += 3
print(num)
```

```text
13
```

다음 두 코드는 같은 의미이다.

```python
num = num + 3
```

```python
num += 3
```

## 주요 복합 할당 연산자

| 연산자  | 의미       | 같은 표현       |
| ---- | -------- | ----------- |
| `+=` | 더한 후 재할당 | `a = a + 값` |
| `-=` | 뺀 후 재할당  | `a = a - 값` |
| `*=` | 곱한 후 재할당 | `a = a * 값` |
| `/=` | 나눈 후 재할당 | `a = a / 값` |
| `%=` | 나머지를 재할당 | `a = a % 값` |

예시:

```python
total = 0
total += 10
total += 20

print(total)
```

```text
30
```

---

# 7. 변수 이름 규칙

## 반드시 지켜야 하는 규칙

### 숫자로 시작할 수 없다

```python
# 잘못된 예
# 1temp = 80
```

```python
# 올바른 예
temp1 = 80
```

### 띄어쓰기를 사용할 수 없다

```python
# 잘못된 예
# machine temp = 80
```

```python
# 올바른 예
machine_temp = 80
```

### 특수문자는 대부분 사용할 수 없다

언더바 `_`는 사용할 수 있다.

```python
machine_name = "펌프"
```

### 파이썬 예약어를 사용할 수 없다

다음과 같은 단어는 파이썬 문법에서 이미 사용 중이다.

```text
if, else, for, while, True, False, def
```

---

## 추천하는 변수 이름

변수가 무엇을 저장하는지 알 수 있게 작성한다.

```python
a = 85
```

보다 다음 코드가 좋다.

```python
machine_temp = 85
```

### 추천 예시

```python
machine_name = "모터"
machine_temp = 92
warning_count = 3
is_running = True
```

---

# 8. 주의할 점

## 8.1 변수 이름에는 따옴표를 사용하지 않는다

```python
eqp = "EQP"
```

`eqp`는 변수 이름이고 `"EQP"`는 문자열 값이다.

```python
print("EQP-001".startswith(eqp))
```

올바른 코드이다.

```python
print("EQP-001".startswith("eqp"))
```

이 코드는 변수 `eqp`가 아니라 실제 문자열 `"eqp"`를 검사한다.

---

## 8.2 대문자와 소문자는 서로 다른 변수이다

```python
temp = 80
Temp = 90

print(temp)
print(Temp)
```

```text
80
90
```

`temp`와 `Temp`는 서로 다른 변수이다.

변수 이름은 가능하면 소문자로 통일한다.

---

## 8.3 내장함수 이름을 변수명으로 사용하지 않는다

다음 이름은 사용을 피한다.

```python
list = [1, 2, 3]
str = "hello"
sorted = [1, 2, 3]
```

이렇게 작성하면 파이썬이 기본으로 제공하는 `list()`, `str()`, `sorted()` 기능을 가릴 수 있다.

수정:

```python
numbers = [1, 2, 3]
text = "hello"
sorted_numbers = [1, 2, 3]
```

---

## 8.4 변수를 만들기 전에 사용할 수 없다

```python
# print(temp)
# temp = 80
```

위 코드는 `temp`가 만들어지기 전에 사용했기 때문에 오류가 발생한다.

```text
NameError
```

변수를 먼저 만든 후 사용해야 한다.

```python
temp = 80
print(temp)
```

---

# 9. 핵심 요약

| 개념       | 설명             | 예시                  |
| -------- | -------------- | ------------------- |
| 변수       | 값을 저장해 사용하는 이름 | `temp = 80`         |
| `int`    | 정수             | `count = 5`         |
| `float`  | 실수             | `temp = 36.5`       |
| `str`    | 문자열            | `name = "펌프"`       |
| `bool`   | 참·거짓           | `is_running = True` |
| `None`   | 값이 없음          | `result = None`     |
| `type()` | 자료형 확인         | `type(temp)`        |
| 재할당      | 변수의 값을 변경      | `temp = 90`         |
| `+=`     | 더한 결과를 재할당     | `count += 1`        |

---

# 10. 이해도 점검

## 퀴즈

다음 코드의 출력 결과와 각 변수의 자료형을 예상해보자.

```python
machine = "모터"
temp = 80
temp += 5
is_warning = temp >= 85

print(machine)
print(temp)
print(is_warning)
```

## 실습

다음 정보를 각각 알맞은 변수에 저장하고 출력해보자.

* 설비 이름: `압축기`
* 온도: `87.5`
* 가동 여부: `True`

예상 출력:

```text
설비 이름: 압축기
온도: 87.5
가동 여부: True
```

---

[🏠 전체 목차로 돌아가기](../README.md)
[⬆️ 맨 위로 이동](#01-변수와-기본-자료형)
[➡️ 다음: 문자열](./02_string.md)
