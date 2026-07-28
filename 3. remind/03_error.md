# 🐞 파이썬 디버깅(Debugging)과 에러 처리 완벽 정리

## 💡 목차

1. **[디버깅 4단계 원칙](https://www.google.com/search?q=%231-%EB%94%94%EB%B2%84%EA%B9%85-4%EB%8B%A8%EA%B3%84-%EC%9B%90%EC%B9%99)**
2. **[Traceback(오류 메시지) 읽는 방법](https://www.google.com/search?q=%232-traceback%EC%98%A4%EB%A5%98-%EB%A9%94%EC%8B%9C%EC%A7%80-%EC%9D%BD%EB%8A%94-%EB%B0%A9%EB%B2%95)**
3. **[자주 만나는 핵심 오류 종류](https://www.google.com/search?q=%233-%EC%9E%90%EC%A3%BC-%EB%A7%8C%EB%82%98%EB%8A%94-%ED%95%B5%EC%8B%AC-%EC%98%A4%EB%A5%98-%EC%A2%85%EB%A5%98)**
4. **[자료형 변환 (형변환 - `str()`)](https://www.google.com/search?q=%234-%EC%9E%90%EB%A3%8C%ED%98%95-%EB%B3%80%ED%99%98-%ED%98%95%EB%B3%80%ED%99%98---str)**
5. **[⚠️ 핵심 주의사항 요약](https://www.google.com/search?q=%235-%E2%9A%A0%EF%B8%8F-%ED%95%B5%EC%8B%AC-%EC%A3%BC%EC%9D%98%EC%82%AC%ED%95%AD-%EC%9A%94%EC%95%BD)**

---

## 1. 디버깅 4단계 원칙

> **디버깅(Debugging)**: 코드에 발생한 오류(버그)를 찾아내고 수정하는 과정

1. **1단계 (마인드 세팅)**: 당황하지 않고, 오류를 코드 작성의 자연스러운 과정으로 받아들이기
2. **2단계 (메시지 읽기)**: 에러의 종류(Name)와 **발생한 줄 번호(Line)** 확인하기
3. **3단계 (코드 점검)**: 에러가 발생한 줄로 이동해 괄호 짝, 따옴표 짝, 오타, 변수명 점검하기
4. **4단계 (검색 및 해결)**: 이해가 안 되는 오류 메시지는 구글에 그대로 검색해서 해결법 찾아 적용하기

---

## 2. Traceback(오류 메시지) 읽는 방법

파이썬은 에러가 발생하면 **Traceback**이라는 실행 이력을 출력합니다.

* **실행 순서**: 위에서 아래로 갈수록 시간 순서대로 실행된 흐름을 나타냅니다.
* **진짜 원인 위치**: **가장 아래쪽 줄**에 진짜 에러의 종류와 원인이 표기됩니다.
* **주요 신호**:
* `(' was never closed`: 괄호 `(` 가 닫히지 않음
* `unterminated string literal`: 따옴표 `"` 또는 `'` 가 닫히지 않음



```python
# 에러 예시 Traceback
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    print(온도)
NameError: name '온도' is not defined  <-- [가장 아래를 먼저 확인할 것!]

```

---

## 3. 자주 만나는 핵심 오류 종류

### 📌 `SyntaxError` (문법 오류)

* **원인**: 파이썬 문법 규칙을 어겼을 때 발생합니다. (괄호/따옴표 안 닫음, 콜론 `:` 오용 등)
* **특징**: 코드가 실행조차 되지 않고 즉시 멈춥니다.

```python
# ❌ SyntaxError 예시
print("온도)      # 따옴표 미복구
print("진동", 2.3  # 괄호 미복구
print("압력": 4.0) # 문법에 맞지 않는 콜론(:) 사용

# ⭕ 수정된 코드
print("온도")
print("진동", 2.3)
print("압력", 4.0)

```

---

### 📌 `NameError` (이름 오류)

* **원인**: 파이썬에 정의된 적 없는 변수나 함수 이름을 호출했을 때 발생합니다.
* **주요 실수**: 문자열 출력 시 **따옴표를 누락**하여 파이썬이 이를 변수로 착각하는 경우.

```python
# ❌ NameError 예시
print(온도, 75)   # '온도'라는 변수를 찾지 못해 발생!

# ⭕ 수정된 코드
print("온도", 75) # 따옴표로 감싸서 문자열로 만들기

```

---

### 📌 `TypeError` (타입 오류)

* **원인**: 서로 합쳐질 수 없는 자료형끼리 연산을 시도할 때 발생합니다. (예: 문자열 + 숫자)

```python
# ❌ TypeError 예시
print("온도: " + 82) # 문자열과 숫자는 '+' 연산 불가!

```

---

## 4. 자료형 변환 (형변환 - `str()`)

문자열끼리 연결할 때 쓰는 `+` 연산자는 **양쪽이 모두 문자열**이어야만 동작합니다.
숫자 변수를 `+` 연산자로 붙이고 싶다면 **`str()` 함수**로 변환해야 합니다.

```python
Temperature_1st = 82
Temperature_Anomaly = 95
Temperature_Change = abs(Temperature_1st - Temperature_Anomaly) # 13 (절댓값)

# 방법 1: 쉼표(,) 사용 (자동 띄어쓰기 1칸 포함)
print("온도:", Temperature_1st)

# 방법 2: str() 형변환 후 '+' 연산자 사용 (딱 붙여서 연결)
print("온도(℃):" + str(Temperature_1st))
print("온도 상승량:" + str(Temperature_Change))

# 방법 3: f-string 활용 (가장 깔끔하고 추천하는 방식)
print(f"온도(℃):{Temperature_1st}")

```

---

## 5. ⚠️ 핵심 주의사항 요약

| 구분 | 발생 원인 | 해결책 |
| --- | --- | --- |
| **코드의 중단** | 중간 줄에서 에러 발생 시 | 에러 발생 시점 이후의 코드는 **실행되지 않고 멈춤** ➔ 에러 줄을 먼저 수정 |
| **`+` 연산자 제약** | `"문자" + 숫자` | 숫자를 `str(숫자)`로 감싸서 문자열로 바꾼 뒤 연결 |
| **`abs()` 함수** | 변화량/차이 구할 때 | `abs(값1 - 값2)`를 쓰면 음수 없이 **양수(절댓값)**로 안전하게 계산 |