# 03. 입력과 출력

[⬅️ 이전: 문자열](./02_string.md)
[🏠 전체 목차로 돌아가기](../README.md)

---

## 📌 목차

* [1. print 함수](#1-print-함수)
* [2. 여러 값 출력하기](#2-여러-값-출력하기)
* [3. sep 속성](#3-sep-속성)
* [4. end 속성](#4-end-속성)
* [5. 문자열 연결](#5-문자열-연결)
* [6. f-string](#6-f-string)
* [7. input 함수](#7-input-함수)
* [8. 입력값 자료형 변환](#8-입력값-자료형-변환)
* [9. 입력값과 조건문 활용](#9-입력값과-조건문-활용)
* [10. 자주 하는 실수](#10-자주-하는-실수)
* [11. 핵심 요약](#11-핵심-요약)
* [12. 이해도 점검](#12-이해도-점검)

---

# summery

| 기능       | 사용법              | 의미            |
| -------- | ---------------- | ------------- |
| 기본 출력    | `print("안녕")`    | 화면에 값 출력      |
| 여러 값 출력  | `print(a, b)`    | 여러 값을 공백으로 구분 |
| 구분자 지정   | `sep="-"`        | 출력값 사이 문자 지정  |
| 끝 문자 지정  | `end=""`         | 출력 마지막 문자 지정  |
| 문자열 연결   | `"A" + "B"`      | 문자열끼리 연결      |
| f-string | `f"{name}"`      | 문자열 안에 변수 삽입  |
| 사용자 입력   | `input("안내문")`   | 사용자에게 값 입력받기  |
| 정수 입력    | `int(input())`   | 입력값을 정수로 변환   |
| 실수 입력    | `float(input())` | 입력값을 실수로 변환   |

---

# 1. `print()` 함수

`print()`는 값을 화면에 출력하는 내장함수이다.

```python
print("안녕하세요")
```

```text
안녕하세요
```

숫자나 변수도 출력할 수 있다.

```python
temp = 80

print(temp)
```

```text
80
```

---

# 2. 여러 값 출력하기

쉼표로 값을 구분하면 여러 값을 한 번에 출력할 수 있다.

```python
name = "PUMP_A"
temp = 85

print("설비", name, "온도", temp)
```

```text
설비 PUMP_A 온도 85
```

`print()`는 쉼표로 나눈 값 사이에 기본적으로 공백 한 칸을 넣는다.

```python
print("2026", "08", "03")
```

```text
2026 08 03
```

---

# 3. `sep` 속성

`sep`은 여러 출력값 사이에 넣을 구분자를 지정한다.

```python
print("2026", "08", "03", sep="-")
```

```text
2026-08-03
```

## 다양한 구분자

```python
print("A", "B", "C", sep="/")
```

```text
A/B/C
```

```python
print("펌프", "모터", "압축기", sep=" | ")
```

```text
펌프 | 모터 | 압축기
```

## 기본값

`sep`을 작성하지 않으면 공백 한 칸이 기본값이다.

```python
print("안녕", "파이썬")
```

다음 코드와 같은 의미이다.

```python
print("안녕", "파이썬", sep=" ")
```

---

# 4. `end` 속성

`end`는 출력 마지막에 넣을 문자열을 지정한다.

`print()`는 기본적으로 출력 후 줄바꿈을 한다.

```python
print("안녕")
print("파이썬")
```

```text
안녕
파이썬
```

기본 줄바꿈은 다음과 같다.

```python
end="\n"
```

## 줄바꿈하지 않기

```python
print("안녕", end=" ")
print("파이썬")
```

```text
안녕 파이썬
```

## 출력 끝에 문자 붙이기

```python
print("안녕", "하세", end="요\n")
```

```text
안녕 하세요
```

## `sep`과 `end` 함께 사용

```python
print("2026", "08", "03", sep="-", end=" 날짜\n")
```

```text
2026-08-03 날짜
```

---

# 5. 문자열 연결

## `+` 연산자

문자열끼리는 `+`로 연결할 수 있다.

```python
first = "안녕"
second = "하세요"

print(first + second)
```

```text
안녕하세요
```

문자열과 숫자를 바로 연결할 수는 없다.

```python
age = 25

# print("나이: " + age)
```

```text
TypeError
```

숫자를 문자열로 바꿔야 한다.

```python
print("나이: " + str(age))
```

```text
나이: 25
```

하지만 변수와 문자열을 함께 출력할 때는 f-string이 더 편리하다.

---

# 6. f-string

f-string은 문자열 안에 변수나 계산식을 쉽게 넣는 방법이다.

문자열 따옴표 앞에 `f`를 붙이고, 변수는 중괄호 `{}` 안에 작성한다.

```python
name = "홍길동"
age = 25

print(f"{name}님은 {age}살입니다.")
```

```text
홍길동님은 25살입니다.
```

## 기본 문법

```python
f"문자열 {변수}"
```

예시:

```python
machine = "PUMP_A"
temp = 85

print(f"설비 {machine}, 온도 {temp}도")
```

```text
설비 PUMP_A, 온도 85도
```

## 중괄호 안에서 계산하기

```python
hour = 8

print(f"{hour}시간은 {hour * 60}분입니다.")
```

```text
8시간은 480분입니다.
```

## 여러 변수 출력하기

```python
name = "모터"
temp = 92
status = "경고"

print(f"설비명: {name}, 온도: {temp}, 상태: {status}")
```

```text
설비명: 모터, 온도: 92, 상태: 경고
```

## f-string을 추천하는 이유

기존 방식:

```python
print("설비 " + name + ", 온도 " + str(temp) + "도")
```

f-string 방식:

```python
print(f"설비 {name}, 온도 {temp}도")
```

f-string은 다음 장점이 있다.

* 숫자를 `str()`로 직접 변환하지 않아도 된다.
* 변수의 위치를 바로 확인할 수 있다.
* 계산식을 넣을 수 있다.
* 코드가 짧고 읽기 쉽다.

---

# 7. `input()` 함수

`input()`은 사용자에게 값을 입력받는 내장함수이다.

```python
name = input("이름을 입력하세요: ")

print(name)
```

실행 예시:

```text
이름을 입력하세요: 홍길동
홍길동
```

괄호 안의 문자열은 사용자에게 보여주는 안내문이다.

```python
weather = input("오늘 날씨는 어떤가요? ")
```

---

# 8. 입력값 자료형 변환

`input()`으로 입력받은 값은 항상 문자열 `str`이다.

```python
age = input("나이를 입력하세요: ")

print(type(age))
```

사용자가 `25`를 입력해도 결과는 문자열이다.

```text
<class 'str'>
```

## 정수로 변환

```python
age = int(input("나이를 입력하세요: "))

print(type(age))
```

```text
<class 'int'>
```

## 실수로 변환

```python
temp = float(input("체온을 입력하세요: "))

print(type(temp))
```

```text
<class 'float'>
```

## 자료형 변환 함수

| 함수        | 변환 결과 | 예시              |
| --------- | ----- | --------------- |
| `int()`   | 정수    | `int("10")`     |
| `float()` | 실수    | `float("36.5")` |
| `str()`   | 문자열   | `str(100)`      |

---

## 숫자 입력값으로 계산하기

잘못된 예:

```python
num1 = input("첫 번째 숫자: ")
num2 = input("두 번째 숫자: ")

print(num1 + num2)
```

`10`과 `20`을 입력하면 문자열이 연결된다.

```text
1020
```

올바른 예:

```python
num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))

print(num1 + num2)
```

```text
30
```

---

# 9. 입력값과 조건문 활용

## 날씨 입력

```python
weather = input("오늘 날씨는 어떤가요? (비/눈/맑음): ")

if weather == "비":
    print("우산을 챙기세요.")
elif weather == "눈":
    print("따뜻한 장갑을 챙기세요.")
elif weather == "맑음":
    print("산책하기 좋은 날씨입니다.")
else:
    print("입력값을 다시 확인하세요.")
```

## 점수 입력

```python
score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A 학점")
elif score >= 80:
    print("B 학점")
elif score >= 70:
    print("C 학점")
else:
    print("F 학점")
```

## 설비 온도 입력

```python
machine = input("설비 이름: ")
temp = float(input("설비 온도: "))

if temp >= 90:
    status = "경고"
else:
    status = "정상"

print(f"설비: {machine}")
print(f"온도: {temp}")
print(f"상태: {status}")
```

---

# 10. 자주 하는 실수

## 10.1 `input()` 결과를 숫자로 생각하는 경우

```python
num = input("숫자 입력: ")

# print(num + 10)
```

`num`은 문자열이기 때문에 숫자와 바로 더할 수 없다.

수정:

```python
num = int(input("숫자 입력: "))

print(num + 10)
```

---

## 10.2 숫자가 아닌 값을 `int()`로 변환하는 경우

```python
# age = int(input("나이: "))
```

사용자가 `"스물다섯"`처럼 숫자가 아닌 문자를 입력하면 오류가 발생한다.

```text
ValueError
```

현재 단계에서는 숫자만 입력해야 한다.

예외 처리는 나중에 `try-except`에서 배운다.

---

## 10.3 f-string 앞의 `f`를 빼먹는 경우

```python
name = "홍길동"

print("{name}님 안녕하세요.")
```

```text
{name}님 안녕하세요.
```

올바른 코드:

```python
print(f"{name}님 안녕하세요.")
```

---

## 10.4 f-string 변수에 중괄호를 쓰지 않는 경우

잘못된 코드:

```python
# print(f"name님 안녕하세요.")
```

이 경우 변수 `name`이 아니라 글자 그대로 `name`이 출력된다.

올바른 코드:

```python
print(f"{name}님 안녕하세요.")
```

---

## 10.5 `sep`과 `end` 위치

`sep`과 `end`는 일반 출력값 뒤에 작성한다.

```python
print("A", "B", "C", sep="-", end="!\n")
```

```text
A-B-C!
```

---

# 11. 핵심 요약

| 기능       | 사용법              | 의미            |
| -------- | ---------------- | ------------- |
| 기본 출력    | `print("안녕")`    | 화면에 값 출력      |
| 여러 값 출력  | `print(a, b)`    | 여러 값을 공백으로 구분 |
| 구분자 지정   | `sep="-"`        | 출력값 사이 문자 지정  |
| 끝 문자 지정  | `end=""`         | 출력 마지막 문자 지정  |
| 문자열 연결   | `"A" + "B"`      | 문자열끼리 연결      |
| f-string | `f"{name}"`      | 문자열 안에 변수 삽입  |
| 사용자 입력   | `input("안내문")`   | 사용자에게 값 입력받기  |
| 정수 입력    | `int(input())`   | 입력값을 정수로 변환   |
| 실수 입력    | `float(input())` | 입력값을 실수로 변환   |

---

# 12. 이해도 점검

## 퀴즈

사용자가 `펌프`, `85.5`를 차례로 입력했다면 다음 코드의 출력 결과를 예상해보자.

```python
machine = input("설비 이름: ")
temp = float(input("온도: "))

print(f"설비 {machine}의 온도는 {temp}도입니다.")
```

## 실습

사용자에게 다음 값을 입력받아 출력해보자.

* 설비 이름
* 온도
* 진동값

출력 형식:

```text
설비: 모터 | 온도: 85.5도 | 진동: 0.3
```

조건:

* 온도와 진동값은 `float`로 변환한다.
* f-string을 사용한다.
* 한 줄로 출력한다.

---

[⬅️ 이전: 문자열](./02_string.md)
[🏠 전체 목차로 돌아가기](../README.md)
[⬆️ 맨 위로 이동](#03-입력과-출력)
