# 02. 문자열

[⬅️ 이전: 변수와 기본 자료형](./01_variable.md)
[🏠 전체 목차로 돌아가기](../README.md)
[➡️ 다음: 입력과 출력](./03_input_output.md)

---

## 📌 목차

* [1. 문자열이란?](#1-문자열이란)
* [2. 문자열 인덱싱](#2-문자열-인덱싱)
* [3. 문자열 슬라이싱](#3-문자열-슬라이싱)
* [4. 문자열 길이](#4-문자열-길이)
* [5. 포함 여부 확인](#5-포함-여부-확인)
* [6. 문자열 위치와 개수 찾기](#6-문자열-위치와-개수-찾기)
* [7. 시작과 끝 검사](#7-시작과-끝-검사)
* [8. 대소문자 처리](#8-대소문자-처리)
* [9. 공백과 문자 제거](#9-공백과-문자-제거)
* [10. 문자열 교체](#10-문자열-교체)
* [11. split과 join](#11-split과-join)
* [12. 메서드 체이닝](#12-메서드-체이닝)
* [13. 자주 하는 실수](#13-자주-하는-실수)
* [14. 핵심 요약](#14-핵심-요약)
* [15. 이해도 점검](#15-이해도-점검)

---

# summary

| 기능    | 사용법                      | 의미           |
| ----- | ------------------------ | ------------ |
| 인덱싱   | `text[0]`                | 글자 하나 가져오기   |
| 슬라이싱  | `text[1:4]`              | 문자열 일부 가져오기  |
| 뒤집기   | `text[::-1]`             | 문자열 역순       |
| 길이    | `len(text)`              | 글자 수         |
| 포함 여부 | `"고장" in text`           | 포함 여부 확인     |
| 개수    | `text.count("a")`        | 등장 횟수        |
| 위치    | `text.find("@")`         | 첫 등장 위치      |
| 시작 검사 | `text.startswith("EQP")` | 시작 문자열 확인    |
| 끝 검사  | `text.endswith(".csv")`  | 끝 문자열 확인     |
| 대문자   | `text.upper()`           | 대문자 변환       |
| 소문자   | `text.lower()`           | 소문자 변환       |
| 공백 제거 | `text.strip()`           | 양쪽 공백 제거     |
| 교체    | `text.replace("-", "")`  | 문자열 교체 또는 제거 |
| 분리    | `text.split(",")`        | 문자열을 리스트로 분리 |
| 연결    | `",".join(items)`        | 리스트를 문자열로 연결 |

---

# 1. 문자열이란?

문자열은 글자나 문장을 저장하는 `str` 자료형이다.

```python
machine = "펌프"
status = "정상"
message = "설비가 정상적으로 가동 중입니다."
```

문자열은 작은따옴표 또는 큰따옴표로 감싼다.

```python
a = "Python"
b = 'Python'
```

두 방식 모두 문자열이다.

```python
print(type(a))
```

```text
<class 'str'>
```

---

# 2. 문자열 인덱싱

문자열의 각 글자에는 왼쪽부터 인덱스 번호가 붙는다.

```python
word = "PYTHON"
```

| 글자     |  P |  Y |  T |  H |  O |  N |
| ------ | -: | -: | -: | -: | -: | -: |
| 양수 인덱스 |  0 |  1 |  2 |  3 |  4 |  5 |
| 음수 인덱스 | -6 | -5 | -4 | -3 | -2 | -1 |

## 특정 글자 가져오기

```python
print(word[0])
print(word[2])
print(word[-1])
```

```text
P
T
N
```

## 주의점

존재하지 않는 인덱스를 사용하면 오류가 발생한다.

```python
# print(word[10])
```

```text
IndexError: string index out of range
```

---

# 3. 문자열 슬라이싱

문자열의 일정한 구간을 잘라낼 때 사용한다.

```python
문자열[시작:끝:간격]
```

* 시작 인덱스는 포함한다.
* 끝 인덱스는 포함하지 않는다.
* 시작, 끝, 간격은 생략할 수 있다.

## 기본 슬라이싱

```python
word = "PYTHON"

print(word[1:4])
```

```text
YTH
```

인덱스 `1`, `2`, `3`의 글자를 가져온다.

## 시작 생략

```python
print(word[:4])
```

```text
PYTH
```

처음부터 4번 인덱스 직전까지 가져온다.

## 끝 생략

```python
print(word[2:])
```

```text
THON
```

2번 인덱스부터 마지막까지 가져온다.

## 전체 가져오기

```python
print(word[:])
```

```text
PYTHON
```

## 음수 인덱스 사용

```python
print(word[-3:])
```

```text
HON
```

음수 인덱스를 사용한다고 자동으로 역순이 되는 것은 아니다.

```python
print(word[:-1])
```

```text
PYTHO
```

마지막 글자를 제외한 전체 문자열이다.

## 간격 사용

```python
print(word[::2])
```

```text
PTO
```

0번부터 두 칸 간격으로 글자를 가져온다.

## 문자열 뒤집기

```python
print(word[::-1])
```

```text
NOHTYP
```

## 범위를 벗어난 슬라이싱

```python
print(word[0:999])
```

```text
PYTHON
```

슬라이싱은 가능한 범위까지만 가져오기 때문에 범위를 크게 지정해도 오류가 발생하지 않는다.

---

# 4. 문자열 길이

`len()`은 문자열의 글자 수를 반환하는 내장함수이다.

```python
print(len("Hello"))
```

```text
5
```

공백도 한 글자로 센다.

```python
print(len("Hello World"))
```

```text
11
```

빈 문자열의 길이는 `0`이다.

```python
print(len(""))
```

```text
0
```

마지막 인덱스 번호는 전체 길이보다 1 작다.

```python
word = "PYTHON"

print(len(word))
print(len(word) - 1)
print(word[len(word) - 1])
```

```text
6
5
N
```

하지만 마지막 값은 보통 `word[-1]`로 더 간단히 가져온다.

---

# 5. 포함 여부 확인

## `in`

특정 문자열이 포함되어 있는지 검사한다.

```python
message = "설비 고장 발생"

print("고장" in message)
print("정상" in message)
```

```text
True
False
```

## `not in`

특정 문자열이 포함되어 있지 않은지 검사한다.

```python
print("고장" not in message)
print("정상" not in message)
```

```text
False
True
```

결과는 항상 `True` 또는 `False`이다.

## 조건문과 함께 사용

```python
message = "모터 고장 발생"

if "고장" in message:
    print("관리자에게 알림을 전송합니다.")
```

---

# 6. 문자열 위치와 개수 찾기

## 6.1 `count()`

특정 문자열이 몇 번 등장하는지 반환한다.

```python
print("banana".count("a"))
```

```text
3
```

```python
phone = "010-1234-1234"

print(phone.count("-"))
```

```text
2
```

찾는 문자열과 정확히 일치해야 한다.

```python
text = "a, b, c, d"

print(text.count(","))
print(text.count(", "))
```

```text
3
3
```

---

## 6.2 `find()`

찾는 문자열이 처음 등장하는 위치를 반환한다.

```python
email = "hong@company.com"

at_index = email.find("@")

print(at_index)
```

```text
4
```

찾는 문자열이 없으면 `-1`을 반환한다.

```python
print("정상".find("고장"))
```

```text
-1
```

### `find()`와 슬라이싱 활용

```python
email = "hong@company.com"
at_index = email.find("@")

user_id = email[:at_index]

print(user_id)
```

```text
hong
```

---

## 6.3 `index()`

`find()`처럼 특정 문자열의 위치를 반환한다.

```python
email = "layla@spreatics.com"

at_index = email.index("@")

print(at_index)
```

하지만 찾는 문자열이 없으면 오류가 발생한다.

```python
# email.index("/")
```

```text
ValueError
```

## `find()`와 `index()` 비교

| 메서드       | 문자열이 있을 때 | 문자열이 없을 때       |
| --------- | --------- | --------------- |
| `find()`  | 위치 반환     | `-1` 반환         |
| `index()` | 위치 반환     | `ValueError` 발생 |

문자열이 없을 가능성이 있다면 `find()`가 안전하다.

---

# 7. 시작과 끝 검사

## `startswith()`

특정 문자열로 시작하는지 검사한다.

```python
code = "EQP-001"

print(code.startswith("EQP"))
```

```text
True
```

## `endswith()`

특정 문자열로 끝나는지 검사한다.

```python
file_name = "sensor_log.csv"

print(file_name.endswith(".csv"))
```

```text
True
```

## 함께 사용하기

```python
file_name = "sensor_log.csv"

if file_name.startswith("sensor") and file_name.endswith(".csv"):
    print("센서 CSV 파일입니다.")
```

### 사용하는 상황

* 파일 확장자 검사
* 설비 코드 형식 검사
* URL 형식 검사
* 특정 접두어나 접미어 확인

---

# 8. 대소문자 처리

## `upper()`

문자열을 대문자로 변환한다.

```python
text = "normal"

print(text.upper())
```

```text
NORMAL
```

## `lower()`

문자열을 소문자로 변환한다.

```python
text = "WARNING"

print(text.lower())
```

```text
warning
```

문자열 메서드는 원본 문자열을 직접 수정하지 않는다.

```python
text = "normal"

text.upper()

print(text)
```

```text
normal
```

변환 결과를 계속 사용하려면 재할당한다.

```python
text = text.upper()

print(text)
```

```text
NORMAL
```

## 대소문자를 통일해서 비교하기

```python
a = "Fault"
b = "FAULT"

print(a == b)
print(a.lower() == b.lower())
```

```text
False
True
```

---

## `capitalize()`

문자열의 첫 글자만 대문자로 바꾼다.

```python
name = "jeong su jin"

print(name.capitalize())
```

```text
Jeong su jin
```

## `title()`

띄어쓰기로 구분된 각 단어의 첫 글자를 대문자로 바꾼다.

```python
print(name.title())
```

```text
Jeong Su Jin
```

## `isupper()`와 `islower()`

문자열이 모두 대문자 또는 소문자로 구성되어 있는지 확인한다.

```python
print("ABC".isupper())
print("abc".islower())
print("Abc".isupper())
```

```text
True
True
False
```

---

# 9. 공백과 문자 제거

## `strip()`

문자열 양쪽의 공백을 제거한다.

```python
text = "   정상   "

print("[" + text.strip() + "]")
```

```text
[정상]
```

문자열 중간의 공백은 제거하지 않는다.

```python
text = "   정   상   "

print(text.strip())
```

```text
정   상
```

## `lstrip()`

왼쪽 공백만 제거한다.

```python
print("[" + text.lstrip() + "]")
```

## `rstrip()`

오른쪽 공백만 제거한다.

```python
print("[" + text.rstrip() + "]")
```

---

## 특정 문자 제거

```python
status = "===정상==="

print(status.strip("="))
```

```text
정상
```

`strip("abcd")`는 `"abcd"`라는 단어 전체를 제거하는 것이 아니다.

전달한 문자 각각을 양쪽 끝에서 반복해서 제거한다.

```python
text = "aaab 오잉 cd"

print(text.strip("abcd"))
```

결과의 양쪽 끝에서 `a`, `b`, `c`, `d`에 해당하는 문자를 제거한다.

중간에 있는 문자는 제거하지 않는다.

> 문자열 중간까지 특정 문자를 제거하려면 `replace()`를 사용한다.

---

# 10. 문자열 교체

`replace()`는 특정 문자열을 다른 문자열로 교체한다.

```python
문자열.replace("기존 문자열", "새 문자열")
```

## 문자열 교체

```python
status = "설비 정상 가동"

print(status.replace("정상", "점검"))
```

```text
설비 점검 가동
```

## 문자열 제거

새 문자열 자리에 빈 문자열 `""`을 넣으면 제거할 수 있다.

```python
phone = "010-1234-1234"

print(phone.replace("-", ""))
```

```text
01012341234
```

## 모든 공백 제거

```python
text = "정 상 작 동"

print(text.replace(" ", ""))
```

```text
정상작동
```

`strip()`은 양쪽 공백만 제거하지만 `replace()`는 문자열 전체에서 일치하는 값을 바꾼다.

---

# 11. `split()`과 `join()`

## `split()`

문자열을 일정한 기준으로 나누어 리스트로 반환한다.

```python
drinks = "에스프레소 아메리카노 카페라떼"

print(drinks.split())
```

```text
['에스프레소', '아메리카노', '카페라떼']
```

구분자를 지정할 수도 있다.

```python
fruits = "딸기,망고,수박"

fruits_list = fruits.split(",")

print(fruits_list)
```

```text
['딸기', '망고', '수박']
```

## 분리 횟수 제한

```python
phone = "010-1234-5678"

print(phone.split("-", 1))
```

```text
['010', '1234-5678']
```

---

## `join()`

여러 문자열을 하나의 문자열로 연결한다.

```python
"구분자".join(문자열이 들어 있는 리스트)
```

예시:

```python
fruits = ["딸기", "망고", "수박"]

print(",".join(fruits))
```

```text
딸기,망고,수박
```

## `split()`과 `join()` 함께 사용하기

```python
today = "2026/08/03"

parts = today.split("/")
result = "-".join(parts)

print(result)
```

```text
2026-08-03
```

한 줄로도 작성할 수 있다.

```python
print("-".join(today.split("/")))
```

---

# 12. 메서드 체이닝

메서드의 결과에 또 다른 메서드를 이어서 사용하는 것을 체이닝이라고 한다.

```python
raw = "  WARNING  "

clean = raw.strip().lower()

print(clean)
```

```text
warning
```

실행 순서:

1. `strip()`으로 양쪽 공백 제거
2. `lower()`로 소문자 변환
3. 결과를 `clean`에 저장

## 실제 데이터 정리 예시

```python
product = "1, NORMAL ,25.3"

parts = product.split(",")
status = parts[1].strip().lower()

print(status)
```

```text
normal
```

데이터 분석에서는 다음과 같은 순서가 자주 사용된다.

```text
공백 제거
→ 대소문자 통일
→ 불필요한 문자 교체
→ 데이터 분리
→ 필요한 값 추출
```

---

# 13. 자주 하는 실수

## 13.1 메서드 괄호를 빼먹는 경우

```python
text = "hello"

print(text.upper)
```

메서드 실행 결과가 아니라 메서드 자체가 출력된다.

올바른 코드:

```python
print(text.upper())
```

---

## 13.2 문자열 메서드가 원본을 바꾼다고 생각하는 경우

```python
text = "hello"
text.upper()

print(text)
```

```text
hello
```

변경 결과를 사용하려면 재할당한다.

```python
text = text.upper()
```

---

## 13.3 `split()` 결과가 문자열이라고 생각하는 경우

```python
result = "a,b,c".split(",")

print(type(result))
```

```text
<class 'list'>
```

`split()`의 결과는 리스트이다.

---

## 13.4 `join()`의 방향을 반대로 작성하는 경우

잘못된 형태:

```python
# fruits.join(",")
```

올바른 형태:

```python
",".join(fruits)
```

구분자 문자열이 앞에 온다.

---

## 13.5 문자열 인덱스 위치를 잘못 계산하는 경우

```python
word = "python"
```

| 글자  |  p |  y |  t |  h |  o |  n |
| --- | -: | -: | -: | -: | -: | -: |
| 인덱스 |  0 |  1 |  2 |  3 |  4 |  5 |

`pyThon`을 만들려면 2번 인덱스를 대문자로 바꿔야 한다.

```python
result = word[:2] + word[2].upper() + word[3:]

print(result)
```

```text
pyThon
```

---

# 14. 핵심 요약

| 기능    | 사용법                      | 의미           |
| ----- | ------------------------ | ------------ |
| 인덱싱   | `text[0]`                | 글자 하나 가져오기   |
| 슬라이싱  | `text[1:4]`              | 문자열 일부 가져오기  |
| 뒤집기   | `text[::-1]`             | 문자열 역순       |
| 길이    | `len(text)`              | 글자 수         |
| 포함 여부 | `"고장" in text`           | 포함 여부 확인     |
| 개수    | `text.count("a")`        | 등장 횟수        |
| 위치    | `text.find("@")`         | 첫 등장 위치      |
| 시작 검사 | `text.startswith("EQP")` | 시작 문자열 확인    |
| 끝 검사  | `text.endswith(".csv")`  | 끝 문자열 확인     |
| 대문자   | `text.upper()`           | 대문자 변환       |
| 소문자   | `text.lower()`           | 소문자 변환       |
| 공백 제거 | `text.strip()`           | 양쪽 공백 제거     |
| 교체    | `text.replace("-", "")`  | 문자열 교체 또는 제거 |
| 분리    | `text.split(",")`        | 문자열을 리스트로 분리 |
| 연결    | `",".join(items)`        | 리스트를 문자열로 연결 |

---

# 15. 이해도 점검

## 퀴즈

다음 코드의 출력 결과를 예상해보자.

```python
data = "  SENSOR-01, WARNING  "

clean = data.strip().lower()
parts = clean.split(",")

code = parts[0]
status = parts[1].strip()

print(code)
print(status)
```

## 실습

다음 문자열을 이용하여 전화번호의 하이픈과 공백을 모두 제거해보자.

```python
phone = "  010-1234-5678  "
```

예상 결과:

```text
01012345678
```

---

[⬅️ 이전: 변수와 기본 자료형](./01_variable.md)
[🏠 전체 목차로 돌아가기](../README.md)
[⬆️ 맨 위로 이동](#02-문자열)
[➡️ 다음: 입력과 출력](./03_input_output.md)
