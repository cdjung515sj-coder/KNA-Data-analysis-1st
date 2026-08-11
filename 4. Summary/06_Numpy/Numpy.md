# NumPy 전체 정리

[🏠 전체 목차로 돌아가기](../README.md)

---

## 💡 한 줄 요약

NumPy는 많은 숫자 데이터를 빠르게 계산하고, 조건에 맞는 데이터를 쉽게 골라낼 수 있도록 만들어진 파이썬 라이브러리이다.

---

## ✅ 핵심 요약

| 개념         | 사용법                  | 의미            |
| ---------- | -------------------- | ------------- |
| NumPy 불러오기 | `import numpy as np` | NumPy 사용 준비   |
| 배열 생성      | `np.array()`         | NumPy 배열 만들기  |
| 범위 배열      | `np.arange()`        | 일정 범위 숫자 생성   |
| 배열 모양      | `.shape`             | 행과 열 확인       |
| 차원         | `.ndim`              | 배열 차원 확인      |
| 요소 개수      | `.size`              | 전체 데이터 개수     |
| 자료형        | `.dtype`             | 배열 데이터 타입 확인  |
| 인덱싱        | `arr[0]`             | 특정 값 가져오기     |
| 슬라이싱       | `arr[1:4]`           | 일정 범위 가져오기    |
| 배열 연산      | `arr * 2`            | 전체 요소에 연산     |
| 조건 생성      | `arr >= 80`          | Boolean 배열 생성 |
| 조건 필터링     | `arr[arr >= 80]`     | 조건에 맞는 값 추출   |
| 평균         | `np.mean(arr)`       | 평균 계산         |
| 최댓값        | `np.max(arr)`        | 최댓값 계산        |
| 형태 변경      | `arr.reshape()`      | 배열 모양 변경      |

---

# 📌 목차

### 시작하기

* [1. NumPy란?](#1-numpy란)
* [2. NumPy 설치](#2-numpy-설치)
* [3. NumPy 불러오기](#3-numpy-불러오기)

### 배열 기초

* [4. NumPy 배열 ndarray](#4-numpy-배열-ndarray)
* [5. Python 리스트와 NumPy 배열 차이](#5-python-리스트와-numpy-배열-차이)
* [6. 배열 생성 방법](#6-배열-생성-방법)
* [7. 배열 정보 확인](#7-배열-정보-확인)

### 데이터 선택

* [8. 인덱싱](#8-인덱싱)
* [9. 슬라이싱](#9-슬라이싱)
* [10. 2차원 배열 인덱싱](#10-2차원-배열-인덱싱)

### 배열 계산

* [11. 배열 전체 연산](#11-배열-전체-연산)
* [12. 배열끼리 연산](#12-배열끼리-연산)
* [13. 비교 연산](#13-비교-연산)

### ⭐ 조건 필터링

* [14. Boolean 배열](#14-boolean-배열)
* [15. Boolean Indexing](#15-boolean-indexing)
* [16. 다중 조건](#16-다중-조건)

### 데이터 분석

* [17. 통계 함수](#17-통계-함수)
* [18. 최댓값과 최솟값 위치](#18-최댓값과-최솟값-위치)

### 다차원 배열

* [19. 2차원 배열](#19-2차원-배열)
* [20. 행과 열 가져오기](#20-행과-열-가져오기)
* [21. reshape](#21-reshape)

### 실무 활용

* [22. 설비 데이터 필터링](#22-설비-데이터-필터링)
* [23. Python과 NumPy 비교](#23-python과-numpy-비교)
* [24. 자주 하는 실수](#24-자주-하는-실수)
* [25. 최종 정리](#25-최종-정리)

---

# 1. NumPy란?

NumPy는 **Numerical Python**의 줄임말이다.

숫자 데이터를 배열 형태로 저장하고 빠르게 계산하기 위해 사용하는 라이브러리이다.

예를 들어 Python 리스트에서는 각 값에 2를 곱하려면 반복문을 사용할 수 있다.

```python
nums = [10, 20, 30]

result = []

for num in nums:
    result.append(num * 2)

print(result)
```

NumPy에서는 배열 전체에 바로 연산할 수 있다.

```python
import numpy as np

nums = np.array([10, 20, 30])

print(nums * 2)
```

결과:

```text
[20 40 60]
```

[⬆️ 목차로 이동](#목차)

---

# 2. NumPy 설치

NumPy는 Python 기본 라이브러리가 아니므로 먼저 설치해야 한다.

터미널:

```bash
python -m pip install numpy
```

Mac에서 `python3`를 사용한다면:

```bash
python3 -m pip install numpy
```

설치 후 확인:

```python
import numpy as np

print(np.__version__)
```

버전 번호가 출력되면 정상적으로 설치된 것이다.

## 🚨 설치 오류

다음 오류가 발생한다면:

```text
ModuleNotFoundError: No module named 'numpy'
```

현재 Python 환경에 NumPy가 설치되어 있지 않은 것이다.

가상환경을 사용한다면 현재 터미널이 해당 환경인지 확인한다.

```text
(.venv)
```

가 표시된 상태에서 NumPy를 설치하는 것이 좋다.

[⬆️ 목차로 이동](#목차)

---

# 3. NumPy 불러오기

NumPy는 일반적으로 다음과 같이 불러온다.

```python
import numpy as np
```

의미:

```text
numpy를 불러오고
앞으로 np라는 이름으로 사용
```

그래서 다음처럼 사용한다.

```python
np.array()
np.mean()
np.max()
```

`np`는 NumPy에서 거의 표준처럼 사용하는 별칭이다.

[⬆️ 목차로 이동](#목차)

---

# 4. NumPy 배열 `ndarray`

NumPy의 핵심 자료형은 `ndarray`이다.

```python
import numpy as np

temps = np.array([10, 20, 30, 40])

print(temps)
print(type(temps))
```

결과:

```text
[10 20 30 40]
<class 'numpy.ndarray'>
```

쉽게 생각하면:

> `ndarray` = 숫자 계산에 특화된 NumPy 배열

이다.

[⬆️ 목차로 이동](#목차)

---

# 5. Python 리스트와 NumPy 배열 차이

## Python 리스트

```python
nums = [1, 2, 3]

print(nums * 2)
```

결과:

```text
[1, 2, 3, 1, 2, 3]
```

리스트가 두 번 반복된다.

## NumPy 배열

```python
nums = np.array([1, 2, 3])

print(nums * 2)
```

결과:

```text
[2 4 6]
```

각 요소에 `2`가 곱해진다.

### ⭐ 핵심

```text
Python 리스트 * 2
→ 리스트 반복

NumPy 배열 * 2
→ 모든 값에 2 곱하기
```

이처럼 배열 전체에 연산을 적용하는 것을 **벡터화 연산**이라고 한다.

[⬆️ 목차로 이동](#목차)

---

# 6. 배열 생성 방법

## `np.array()`

```python
temps = np.array([10, 20, 30])
```

가장 기본적인 배열 생성 방법이다.

---

## `np.arange()`

Python의 `range()`와 비슷하다.

```python
nums = np.arange(1, 10)

print(nums)
```

```text
[1 2 3 4 5 6 7 8 9]
```

간격 지정:

```python
nums = np.arange(0, 11, 2)

print(nums)
```

```text
[ 0  2  4  6  8 10]
```

---

## `np.zeros()`

모든 값이 0인 배열을 만든다.

```python
data = np.zeros(5)

print(data)
```

```text
[0. 0. 0. 0. 0.]
```

---

## `np.ones()`

모든 값이 1인 배열을 만든다.

```python
data = np.ones(5)

print(data)
```

```text
[1. 1. 1. 1. 1.]
```

[⬆️ 목차로 이동](#목차)

---

# 7. 배열 정보 확인

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

## `.shape`

배열의 형태를 확인한다.

```python
print(data.shape)
```

```text
(2, 3)
```

뜻:

```text
2행 3열
```

---

## `.ndim`

배열의 차원을 확인한다.

```python
print(data.ndim)
```

```text
2
```

---

## `.size`

전체 요소의 개수를 확인한다.

```python
print(data.size)
```

```text
6
```

---

## `.dtype`

배열에 저장된 데이터의 자료형을 확인한다.

```python
print(data.dtype)
```

예:

```text
int64
```

## 정리

| 속성       | 의미       |
| -------- | -------- |
| `.shape` | 배열의 모양   |
| `.ndim`  | 차원       |
| `.size`  | 전체 요소 개수 |
| `.dtype` | 데이터 자료형  |

[⬆️ 목차로 이동](#목차)

---

# 8. 인덱싱

리스트와 동일하게 인덱스로 특정 값에 접근할 수 있다.

```python
temps = np.array([10, 20, 30, 40])

print(temps[0])
print(temps[2])
print(temps[-1])
```

결과:

```text
10
30
40
```

[⬆️ 목차로 이동](#목차)

---

# 9. 슬라이싱

기본 형태:

```text
배열[시작:끝:간격]
```

예시:

```python
temps = np.array([10, 20, 30, 40, 50])

print(temps[1:4])
```

```text
[20 30 40]
```

간격 사용:

```python
print(temps[::2])
```

```text
[10 30 50]
```

[⬆️ 목차로 이동](#목차)

---

# 10. 2차원 배열 인덱싱

```python
data = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
```

특정 위치:

```python
print(data[0, 0])
```

```text
10
```

```python
print(data[1, 1])
```

```text
40
```

기본 형태:

```text
배열[행, 열]
```

[⬆️ 목차로 이동](#목차)

---

# 11. 배열 전체 연산

```python
temps = np.array([10, 20, 30, 40])
```

## 더하기

```python
print(temps + 10)
```

```text
[20 30 40 50]
```

## 빼기

```python
print(temps - 5)
```

## 곱하기

```python
print(temps * 2)
```

## 나누기

```python
print(temps / 2)
```

모든 요소에 연산이 적용된다.

[⬆️ 목차로 이동](#목차)

---

# 12. 배열끼리 연산

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
```

결과:

```text
[11 22 33]
```

같은 위치의 값끼리 계산된다.

```text
10 + 1
20 + 2
30 + 3
```

곱하기:

```python
print(a * b)
```

```text
[10 40 90]
```

> NumPy에서 `*`는 기본적으로 요소별 곱셈이다.

[⬆️ 목차로 이동](#목차)

---

# 13. 비교 연산

```python
temps = np.array([70, 85, 90, 75, 100])

print(temps >= 90)
```

결과:

```text
[False False  True False  True]
```

각 값마다 조건을 검사한다.

```text
70 >= 90 → False
85 >= 90 → False
90 >= 90 → True
75 >= 90 → False
100 >= 90 → True
```

[⬆️ 목차로 이동](#목차)

---

# 14. Boolean 배열

비교 연산의 결과로 만들어진 `True`, `False` 배열이다.

```python
temps = np.array([70, 85, 90, 100])

condition = temps >= 90

print(condition)
```

```text
[False False  True  True]
```

이 배열은 어떤 데이터가 조건을 만족하는지 표시하는 역할을 한다.

[⬆️ 목차로 이동](#목차)

---

# 15. Boolean Indexing

Boolean 배열을 이용하면 조건에 맞는 값만 추출할 수 있다.

```python
temps = np.array([70, 85, 90, 100])

condition = temps >= 90

print(temps[condition])
```

```text
[ 90 100]
```

한 줄로 작성:

```python
print(temps[temps >= 90])
```

### ⭐ 핵심 흐름

```text
temps >= 90

↓ 조건 검사

[False False True True]

↓ 배열에 적용

temps[condition]

↓

[90 100]
```

기존 Python에서는:

```python
warning = []

for temp in temps:
    if temp >= 90:
        warning.append(temp)
```

NumPy에서는:

```python
warning = temps[temps >= 90]
```

로 간단하게 처리할 수 있다.

[⬆️ 목차로 이동](#목차)

---

# 16. 다중 조건

## AND 조건 `&`

70 이상이고 90 이하:

```python
temps = np.array([60, 70, 75, 85, 95])

condition = (temps >= 70) & (temps <= 90)

print(temps[condition])
```

```text
[70 75 85]
```

---

## OR 조건 `|`

70 미만이거나 90 초과:

```python
condition = (temps < 70) | (temps > 90)

print(temps[condition])
```

```text
[60 95]
```

## 🚨 중요

NumPy 배열 조건에서는 일반적으로:

```text
and → &
or  → |
```

를 사용한다.

그리고 조건마다 괄호를 붙인다.

```python
(temps >= 70) & (temps <= 90)
```

[⬆️ 목차로 이동](#목차)

---

# 17. 통계 함수

```python
temps = np.array([70, 80, 90, 100])
```

## 합계

```python
print(np.sum(temps))
```

```text
340
```

## 평균

```python
print(np.mean(temps))
```

```text
85.0
```

## 최솟값

```python
print(np.min(temps))
```

```text
70
```

## 최댓값

```python
print(np.max(temps))
```

```text
100
```

## 표준편차

```python
print(np.std(temps))
```

데이터가 평균을 기준으로 얼마나 퍼져 있는지 확인할 때 사용한다.

## 핵심 정리

| 함수          | 의미   |
| ----------- | ---- |
| `np.sum()`  | 합계   |
| `np.mean()` | 평균   |
| `np.min()`  | 최솟값  |
| `np.max()`  | 최댓값  |
| `np.std()`  | 표준편차 |

[⬆️ 목차로 이동](#목차)

---

# 18. 최댓값과 최솟값 위치

## `argmax()`

최댓값의 인덱스를 반환한다.

```python
temps = np.array([70, 100, 85, 90])

print(np.argmax(temps))
```

```text
1
```

100이 `1번 인덱스`에 있기 때문이다.

## `argmin()`

최솟값의 인덱스를 반환한다.

```python
print(np.argmin(temps))
```

```text
0
```

## 차이

```text
np.max()     → 최댓값
np.argmax()  → 최댓값의 위치

np.min()     → 최솟값
np.argmin()  → 최솟값의 위치
```

[⬆️ 목차로 이동](#목차)

---

# 19. 2차원 배열

표처럼 행과 열을 가지는 배열이다.

```python
data = np.array([
    [70, 10],
    [80, 20],
    [90, 30]
])
```

형태:

```text
70  10
80  20
90  30
```

```python
print(data.shape)
```

```text
(3, 2)
```

3행 2열이다.

[⬆️ 목차로 이동](#목차)

---

# 20. 행과 열 가져오기

```python
data = np.array([
    [70, 10],
    [80, 20],
    [90, 30]
])
```

## 행 가져오기

```python
print(data[0])
```

```text
[70 10]
```

## 열 가져오기

```python
print(data[:, 0])
```

```text
[70 80 90]
```

`:`은 해당 위치의 전체 범위를 의미한다.

```python
data[:, 0]
```

뜻:

> 모든 행에서 0번 열을 가져온다.

두 번째 열:

```python
print(data[:, 1])
```

```text
[10 20 30]
```

[⬆️ 목차로 이동](#목차)

---

# 21. reshape

배열의 모양을 변경한다.

```python
data = np.array([1, 2, 3, 4, 5, 6])

new_data = data.reshape(2, 3)

print(new_data)
```

결과:

```text
[[1 2 3]
 [4 5 6]]
```

1차원 배열 6개를 `2행 3열`로 변경했다.

## 가능한 형태

```text
6개 데이터

1 × 6
2 × 3
3 × 2
6 × 1
```

모두 가능하다.

하지만:

```python
data.reshape(2, 4)
```

는 불가능하다.

```text
2 × 4 = 8
```

8개의 데이터가 필요하기 때문이다.

> `reshape()` 전과 후의 전체 요소 개수는 반드시 같아야 한다.

[⬆️ 목차로 이동](#목차)

---

# 22. 설비 데이터 필터링

회전수와 토크 데이터:

```python
rpm = np.array([1200, 1500, 1800, 2200, 2500])
torque = np.array([50, 45, 40, 30, 20])
```

## 회전수 2000 초과

```python
high_rpm = rpm[rpm > 2000]

print(high_rpm)
```

```text
[2200 2500]
```

---

## 위험 조건

조건:

* 회전수 2000 초과
* 또는 토크 25 미만

```python
danger = (rpm > 2000) | (torque < 25)

print(danger)
```

```text
[False False False  True  True]
```

위험 시점의 회전수:

```python
print(rpm[danger])
```

```text
[2200 2500]
```

같은 시점의 토크:

```python
print(torque[danger])
```

```text
[30 20]
```

### ⭐ 핵심

같은 길이의 센서 배열이라면 하나의 Boolean 조건을 여러 배열에 적용해 **같은 시점의 데이터**를 꺼낼 수 있다.

[⬆️ 목차로 이동](#목차)

---

# 23. Python과 NumPy 비교

## 조건에 맞는 값 추출

### Python

```python
temps = [70, 85, 90, 100]

warning = []

for temp in temps:
    if temp >= 90:
        warning.append(temp)

print(warning)
```

### NumPy

```python
temps = np.array([70, 85, 90, 100])

warning = temps[temps >= 90]

print(warning)
```

## 비교

| Python              | NumPy            |
| ------------------- | ---------------- |
| `list`              | `ndarray`        |
| `for` 반복 계산         | 배열 전체 연산         |
| `for + if`          | Boolean 배열       |
| `for + if + append` | Boolean Indexing |
| `sum()`             | `np.sum()`       |
| `min()`             | `np.min()`       |
| `max()`             | `np.max()`       |
| 직접 평균 계산            | `np.mean()`      |
| 중첩 리스트              | 2차원 배열           |

[⬆️ 목차로 이동](#목차)

---

# 24. 자주 하는 실수

## 24.1 NumPy 설치 환경이 다른 경우

```text
ModuleNotFoundError: No module named 'numpy'
```

코드를 실행하는 Python 환경과 NumPy를 설치한 환경이 같은지 확인한다.

---

## 24.2 import 누락

```python
# np.array([1, 2, 3])
```

`np`를 사용하기 전에:

```python
import numpy as np
```

가 필요하다.

---

## 24.3 배열 조건에서 `and` 사용

잘못된 형태:

```python
# (temps >= 70) and (temps <= 90)
```

NumPy에서는:

```python
(temps >= 70) & (temps <= 90)
```

---

## 24.4 배열 조건에서 `or` 사용

잘못된 형태:

```python
# (temps < 70) or (temps > 90)
```

NumPy:

```python
(temps < 70) | (temps > 90)
```

---

## 24.5 조건의 괄호 누락

추천:

```python
(temps >= 70) & (temps <= 90)
```

각 조건을 괄호로 묶는다.

---

## 24.6 `shape`를 함수처럼 사용하는 경우

잘못된 코드:

```python
# data.shape()
```

올바른 코드:

```python
data.shape
```

`shape`, `ndim`, `size`, `dtype`는 속성이므로 괄호를 붙이지 않는다.

---

## 24.7 `reshape()` 요소 개수 불일치

```python
data = np.array([1, 2, 3, 4, 5, 6])

# data.reshape(2, 4)
```

6개 데이터를 8칸으로 만들 수 없으므로 오류가 발생한다.

---

# 25. 최종 정리

NumPy의 가장 중요한 흐름은 다음과 같다.

```text
Python 리스트
        ↓
    np.array()
        ↓
   NumPy 배열
        ↓
 배열 전체 연산
        ↓
    비교 연산
        ↓
 Boolean 배열
        ↓
Boolean Indexing
        ↓
 조건 데이터 추출
        ↓
   통계 계산
```

## ⭐ 우선 암기할 것

```python
import numpy as np

np.array()

arr.shape
arr.ndim
arr.size
arr.dtype

arr[0]
arr[1:4]

arr + 10
arr * 2

arr >= 80
arr[arr >= 80]

(조건1) & (조건2)
(조건1) | (조건2)

np.sum()
np.mean()
np.min()
np.max()

arr.reshape()
```

---

## 🎯 이해도 점검

다음 코드의 결과를 예상해보자.

```python
import numpy as np

temps = np.array([65, 72, 88, 95, 81, 60])

condition = (temps >= 80) & (temps < 90)

result = temps[condition]

print(result)
```

---

## 🛠 실습

다음 데이터를 사용한다.

```python
rpm = np.array([1500, 1800, 2100, 2300, 1900, 2500])
torque = np.array([45, 38, 29, 35, 40, 20])
```

다음 조건을 만족하는 위치의 `rpm`과 `torque`를 각각 출력해보자.

```text
rpm이 2000 이상
그리고
torque가 30 미만
```

조건:

* Boolean 배열을 만든다.
* `&`를 사용한다.
* 각 조건에 괄호를 사용한다.
* 같은 Boolean 배열을 `rpm`, `torque`에 각각 적용한다.

---

[🏠 전체 목차로 돌아가기](../README.md)
[⬆️ 맨 위로 이동](#numpy-전체-정리)
