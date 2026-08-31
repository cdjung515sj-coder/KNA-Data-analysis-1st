# 🐼 Pandas Series 완전 정리

> **목표:** `Series`가 무엇인지 정확히 이해하고,  
> 데이터를 **선택 → 필터링 → 계산 → 집계**하는 흐름까지 자연스럽게 사용할 수 있도록 정리한다.

---

# 0. 한눈에 보는 Series

```text
Series
│
├─ 1차원 데이터
├─ 값(value)마다 인덱스(index)가 붙어 있음
├─ 한 종류의 열(column)을 다룰 때 자주 사용
│
├─ 값 선택
│  ├─ s[0]
│  ├─ s.loc[]
│  └─ s.iloc[]
│
├─ 조건 필터링
│  ├─ s > 80
│  ├─ s[s > 80]
│  ├─ s.isin([...])
│  ├─ s.between(a, b)
│  └─ ~조건
│
├─ 통계
│  ├─ mean()
│  ├─ sum()
│  ├─ min(), max()
│  ├─ var(), std()
│  └─ count()
│
└─ 값 분석
   ├─ value_counts()
   ├─ unique()
   └─ nunique()
```

---

# 1. Series란?

## 💡 핵심 개념

`Series`는 **인덱스가 붙어 있는 1차원 데이터 구조**이다.

쉽게 말하면:

> **"한 줄짜리 데이터 + 각 값의 이름표(index)"**

```python
import pandas as pd

s = pd.Series([10, 20, 30])
print(s)
```

결과:

```text
0    10
1    20
2    30
dtype: int64
```

구조를 그림으로 보면:

```text
index     value
  0   →    10
  1   →    20
  2   →    30
```

즉 Series에는 크게 두 가지가 있다.

```text
Series
 ├─ index : 값의 위치/이름
 └─ value : 실제 데이터
```

---

# 2. Series와 List의 차이

Python의 `list`와 비슷해 보이지만 목적이 다르다.

| 구분 | Python List | Pandas Series |
|---|---|---|
| 형태 | `[10, 20, 30]` | index + value |
| 차원 | 1차원 | 1차원 |
| 인덱스 | 위치 번호 | 위치 또는 사용자 지정 인덱스 |
| 조건 필터링 | 직접 반복문 필요 | 매우 편리 |
| 통계 계산 | 제한적 | 매우 편리 |
| 결측치 처리 | 직접 처리 | 기능 제공 |
| 데이터 분석 | 불편 | 매우 적합 |

예를 들어 리스트에서는:

```python
data = [60, 90, 75, 100]

result = []

for x in data:
    if x >= 80:
        result.append(x)

print(result)
```

Series에서는:

```python
s = pd.Series([60, 90, 75, 100])

print(s[s >= 80])
```

결과:

```text
1     90
3    100
dtype: int64
```

### ⭐ Series를 쓰는 가장 큰 이유

```text
여러 데이터를
조건으로 찾고
계산하고
통계 내는 작업이 편하다.
```

---

# 3. Series와 DataFrame의 차이 ⭐⭐⭐

Pandas에서 가장 중요하게 구분해야 한다.

| 구분 | Series | DataFrame |
|---|---|---|
| 차원 | 1차원 | 2차원 |
| 느낌 | 열 1개 | 표 전체 |
| 모양 | 세로 한 줄 | 행 × 열 |
| 예 | 온도 열 | 전체 센서 데이터 |

예:

```python
df["온도"]
```

컬럼 하나를 선택하면 보통:

```text
Series
```

이다.

반면:

```python
df[["온도"]]
```

처럼 대괄호를 한 번 더 사용하면:

```text
DataFrame
```

이다.

### ⭐ 매우 중요

```python
df["온도"]      # Series
df[["온도"]]    # DataFrame
```

모양으로 기억하면:

```text
[ ]       → 한 열 → Series

[[ ]]     → 열 목록 → DataFrame
```

---

# 4. Series 생성하기

## 4-1. 리스트로 만들기

```python
import pandas as pd

s = pd.Series([10, 20, 30])
```

결과:

```text
0    10
1    20
2    30
```

인덱스를 지정하지 않으면 자동으로:

```text
0, 1, 2, 3 ...
```

이 생성된다.

---

## 4-2. 인덱스 직접 지정

```python
s = pd.Series(
    [78, 92, 85],
    index=["모터", "펌프", "팬"]
)

print(s)
```

결과:

```text
모터    78
펌프    92
팬     85
dtype: int64
```

구조:

```text
모터 → 78
펌프 → 92
팬   → 85
```

이제 위치 번호 대신 이름으로 값을 찾을 수 있다.

```python
print(s["모터"])
```

결과:

```text
78
```

---

# 5. Series의 주요 속성 ⭐⭐⭐

예제:

```python
s = pd.Series([10, 20, 30], name="온도")
```

---

## `s.index`

인덱스를 확인한다.

```python
print(s.index)
```

---

## `s.values`

실제 값들을 확인한다.

```python
print(s.values)
```

예:

```text
[10 20 30]
```

---

## `s.dtype`

데이터 타입을 확인한다.

```python
print(s.dtype)
```

예:

```text
int64
float64
object
bool
```

---

## `s.shape`

Series의 크기를 **튜플 형태**로 반환한다.

```python
print(s.shape)
```

결과:

```text
(3,)
```

Series는 1차원이기 때문에:

```text
(행 개수,)
```

형태이다.

---

## `s.size`

전체 원소 개수.

```python
print(s.size)
```

결과:

```text
3
```

### ⚠️ 주의

`size`는 **메서드가 아니라 속성**이다.

```python
s.size      # O
s.size()    # X
```

---

## `s.ndim`

차원 수를 확인한다.

```python
print(s.ndim)
```

Series이므로:

```text
1
```

---

## `s.name`

Series의 이름.

```python
print(s.name)
```

---

# 6. Series 값 선택하기

예제:

```python
s = pd.Series(
    [78, 92, 85],
    index=["모터", "펌프", "팬"]
)
```

---

# 7. `loc`와 `iloc` ⭐⭐⭐

Series 데이터 선택에서 매우 중요하다.

## `loc`

> **인덱스 이름(label)으로 선택**

```python
s.loc["모터"]
```

결과:

```text
78
```

---

## `iloc`

> **실제 위치 번호로 선택**

```python
s.iloc[0]
```

결과:

```text
78
```

비교하면:

```text
loc  → 이름 기준
iloc → 위치 기준
```

예:

```python
s.loc["펌프"]
```

```text
92
```

```python
s.iloc[1]
```

```text
92
```

---

# 8. 슬라이싱

## `iloc` 슬라이싱

```python
s.iloc[0:2]
```

0번부터 2번 **직전까지** 선택한다.

```text
0, 1
```

즉:

```text
모터    78
펌프    92
```

---

## `loc` 슬라이싱

```python
s.loc["모터":"펌프"]
```

`loc`는 끝값까지 포함한다.

### ⭐ 차이

```text
iloc[0:2]
→ 0, 1
→ 끝 위치 제외

loc["모터":"펌프"]
→ 모터, 펌프
→ 끝 라벨 포함
```

---

# 9. 조건 비교

Series는 값 전체에 한 번에 조건을 적용할 수 있다.

```python
s = pd.Series([70, 85, 90, 65])
```

```python
s >= 80
```

결과:

```text
0    False
1     True
2     True
3    False
dtype: bool
```

이 결과도 Series이다.

정확히는:

> **Boolean Series**

---

# 10. 불리언 인덱싱 ⭐⭐⭐

조건에 맞는 실제 값만 가져오려면:

```python
s[s >= 80]
```

결과:

```text
1    85
2    90
dtype: int64
```

흐름을 분리하면 이해하기 쉽다.

```python
condition = s >= 80
result = s[condition]
```

구조:

```text
원본 데이터
   ↓
조건 만들기
   ↓
True / False
   ↓
True인 값만 선택
```

---

# 11. 여러 조건 사용하기

Pandas에서는 Python의 `and`, `or` 대신:

```text
&  → AND
|  → OR
~  → NOT
```

를 사용한다.

---

## AND 조건

```python
s[(s >= 70) & (s <= 90)]
```

뜻:

```text
70 이상이고
90 이하인 값
```

---

## OR 조건

```python
s[(s < 70) | (s > 90)]
```

뜻:

```text
70 미만 또는
90 초과
```

---

## ⚠️ 매우 중요: 괄호

잘못된 예:

```python
s[s >= 70 & s <= 90]
```

권장:

```python
s[(s >= 70) & (s <= 90)]
```

각 조건을 반드시 괄호로 묶는 습관을 들인다.

---

# 12. `between()` ⭐⭐

특정 범위 안에 있는 값을 찾을 때 편리하다.

```python
s.between(70, 90)
```

뜻:

```text
70 <= 값 <= 90
```

실제 값 필터링:

```python
s[s.between(70, 90)]
```

다음과 비슷하다.

```python
s[(s >= 70) & (s <= 90)]
```

### 활용

온도가 정상 범위에 있는지 검사:

```python
normal = temp.between(20, 80)
```

---

# 13. `isin()` ⭐⭐⭐

여러 후보 중 하나에 해당하는 값인지 검사한다.

```python
status = pd.Series(["정상", "고장", "점검", "정상"])
```

```python
status.isin(["고장", "점검"])
```

결과:

```text
False
True
True
False
```

필터링:

```python
status[status.isin(["고장", "점검"])]
```

### 의미

```text
"고장"이거나 "점검"인가?
```

즉 다음과 비슷하다.

```python
(status == "고장") | (status == "점검")
```

하지만 값이 많아질수록 `isin()`이 훨씬 편하다.

---

# 14. `~` 부정 연산자 ⭐⭐⭐

`~`는 Boolean Series의 True/False를 반대로 바꾼다.

```python
condition = status.isin(["고장", "점검"])
```

```python
~condition
```

결과:

```text
True
False
False
True
```

따라서:

```python
status[~status.isin(["고장", "점검"])]
```

은:

> 고장과 점검이 **아닌 값**

을 가져온다.

### 암기

```text
~ = 조건 뒤집기
```

---

# 15. 산술 연산

Series는 전체 값에 한 번에 연산할 수 있다.

```python
s = pd.Series([10, 20, 30])
```

```python
s + 10
```

결과:

```text
0    20
1    30
2    40
```

---

```python
s * 2
```

결과:

```text
0    20
1    40
2    60
```

이것을 **벡터화 연산(vectorized operation)**이라고 생각하면 된다.

### 장점

반복문 없이 전체 데이터 계산 가능.

---

# 16. Series끼리 연산할 때의 핵심 ⭐⭐⭐

Series끼리 계산할 때는 단순히 위치만 보는 것이 아니라:

> **index를 기준으로 맞춰서 계산한다.**

예:

```python
a = pd.Series([10, 20], index=["A", "B"])
b = pd.Series([1, 2], index=["B", "A"])

print(a + b)
```

계산:

```text
A → 10 + 2
B → 20 + 1
```

결과:

```text
A    12
B    21
```

### ⚠️ 주의

Series의 인덱스가 다르면 예상하지 못한 `NaN`이 생길 수 있다.

```python
a = pd.Series([10, 20], index=["A", "B"])
b = pd.Series([1, 2], index=["B", "C"])

a + b
```

결과 개념:

```text
A    NaN
B    21
C    NaN
```

따라서 Series 연산에서는:

```text
인덱스 정렬
```

이 매우 중요하다.

---

# 17. 기본 통계 메서드 ⭐⭐⭐

예:

```python
s = pd.Series([10, 20, 30, 40])
```

| 기능 | 코드 |
|---|---|
| 합계 | `s.sum()` |
| 평균 | `s.mean()` |
| 최소 | `s.min()` |
| 최대 | `s.max()` |
| 중앙값 | `s.median()` |
| 분산 | `s.var()` |
| 표준편차 | `s.std()` |
| 개수 | `s.count()` |

---

# 18. `size`, `count()`, `len()` 차이 ⭐⭐⭐

특히 결측치가 있을 때 차이가 난다.

```python
s = pd.Series([10, 20, None, 40])
```

## `s.size`

전체 칸 수.

```python
s.size
```

결과:

```text
4
```

---

## `len(s)`

전체 원소 개수.

```python
len(s)
```

결과:

```text
4
```

---

## `s.count()`

`NaN`을 제외한 실제 데이터 개수.

```python
s.count()
```

결과:

```text
3
```

### 한눈에 보기

```text
데이터
10
20
NaN
40
```

```text
size      → 4
len(s)    → 4
count()   → 3
```

### ⭐ 암기

```text
전체 칸 수       → size / len
결측치 제외 개수 → count()
```

---

# 19. `value_counts()` ⭐⭐⭐

각 값이 몇 번 등장했는지 센다.

```python
s = pd.Series(["정상", "고장", "정상", "정상", "고장"])
```

```python
s.value_counts()
```

결과:

```text
정상    3
고장    2
```

### 활용

범주형 데이터 분석에서 매우 많이 사용한다.

예:

```python
df["품질등급"].value_counts()
df["result"].value_counts()
df["설비상태"].value_counts()
```

---

# 20. 비율 계산하기

```python
s.value_counts(normalize=True)
```

각 값의 비율을 반환한다.

예:

```text
정상    0.6
고장    0.4
```

퍼센트로 보고 싶다면:

```python
s.value_counts(normalize=True) * 100
```

---

# 21. `unique()`와 `nunique()`

## `unique()`

어떤 값들이 존재하는지 확인.

```python
s.unique()
```

예:

```text
['정상' '고장' '점검']
```

---

## `nunique()`

고유한 값의 개수를 확인.

```python
s.nunique()
```

예:

```text
3
```

### 차이

```text
unique()  → 값 종류 자체
nunique() → 값 종류 개수
```

---

# 22. 정렬

## 값 기준 정렬

```python
s.sort_values()
```

오름차순:

```text
작은 값 → 큰 값
```

내림차순:

```python
s.sort_values(ascending=False)
```

---

## 인덱스 기준 정렬

```python
s.sort_index()
```

---

# 23. 결측치 `NaN`

데이터가 비어 있는 경우 Pandas에서는 흔히:

```text
NaN
```

으로 표현된다.

예:

```python
s = pd.Series([10, None, 30])
```

---

# 24. 결측치 확인

## `isna()`

```python
s.isna()
```

결과:

```text
False
True
False
```

---

## `notna()`

결측치가 아닌 값 확인.

```python
s.notna()
```

---

# 25. 결측치 제거

```python
s.dropna()
```

결측치가 있는 값을 제거한다.

---

# 26. 결측치 채우기

```python
s.fillna(0)
```

NaN을 0으로 채운다.

평균으로 채우는 것도 가능하다.

```python
s.fillna(s.mean())
```

### ⚠️ 주의

결측치를 무조건 0이나 평균으로 채우는 것이 항상 좋은 것은 아니다.

데이터 의미와 분석 목적을 보고 결정해야 한다.

---

# 27. 값 변경

## `replace()`

특정 값을 다른 값으로 바꾼다.

```python
s = pd.Series(["정상", "불량", "정상"])

s.replace("불량", "고장")
```

---

# 28. `map()` ⭐⭐

각 값에 규칙을 적용할 때 사용할 수 있다.

```python
s = pd.Series(["정상", "고장"])
```

```python
s.map({
    "정상": 0,
    "고장": 1
})
```

결과:

```text
0    0
1    1
dtype: int64
```

범주형 값을 숫자로 바꾸는 데 자주 사용한다.

---

# 29. 문자열 Series

문자열 Series에서는 `.str`을 사용한다.

```python
s = pd.Series(["motor", "pump", "fan"])
```

대문자로 변환:

```python
s.str.upper()
```

문자 포함 여부:

```python
s.str.contains("m")
```

문자 길이:

```python
s.str.len()
```

### 핵심

```text
문자열 기능
Series.str.문자열메서드()
```

---

# 30. DataFrame에서 Series 가져오기 ⭐⭐⭐

실전에서는 직접 Series를 만드는 것보다 DataFrame의 한 컬럼을 선택해서 Series를 얻는 경우가 많다.

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

```python
temp = df["온도"]
```

이때:

```python
type(temp)
```

은:

```text
pandas.core.series.Series
```

이다.

---

# 31. DataFrame 분석에서 Series의 역할

예를 들어 설비 데이터가 있다고 하자.

```text
설비     온도    진동    상태
모터     78     2.1    정상
펌프     92     4.8    고장
팬       85     2.9    정상
```

온도 한 열:

```python
df["온도"]
```

→ Series

온도 평균:

```python
df["온도"].mean()
```

고온 설비 조건:

```python
df["온도"] >= 90
```

→ Boolean Series

고온 행만 선택:

```python
df[df["온도"] >= 90]
```

### 흐름

```text
DataFrame
   ↓
한 컬럼 선택
   ↓
Series
   ↓
조건 생성
   ↓
Boolean Series
   ↓
DataFrame 필터링
```

이 흐름을 이해하는 것이 매우 중요하다.

---

# 32. 실전 예제 ① 온도 이상치 탐색

```python
temp = pd.Series([72, 85, 95, 68, 101])
```

90도 초과:

```python
condition = temp > 90
```

```python
temp[condition]
```

결과:

```text
2     95
4    101
```

---

# 33. 실전 예제 ② 정상 범위 찾기

```python
temp = pd.Series([20, 50, 75, 95])
```

정상 범위가 30~80이라면:

```python
normal = temp.between(30, 80)
```

정상값:

```python
temp[normal]
```

비정상값:

```python
temp[~normal]
```

---

# 34. 실전 예제 ③ 여러 상태 선택

```python
status = pd.Series([
    "정상",
    "고장",
    "점검",
    "정상",
    "경고"
])
```

고장 또는 경고만:

```python
condition = status.isin(["고장", "경고"])

status[condition]
```

---

# 35. 실전 예제 ④ 위험 조건 만들기

회전수:

```python
rpm = pd.Series([1000, 1500, 2200, 1800])
```

토크:

```python
torque = pd.Series([50, 45, 20, 55])
```

위험 조건:

```text
회전수가 2000 초과
또는
토크가 30 미만
```

코드:

```python
danger = (rpm > 2000) | (torque < 30)
```

위험한 위치:

```python
rpm[danger]
```

또는 DataFrame이라면:

```python
df[danger]
```

---

# 36. 인덱스 찾기

조건을 만족하는 위치의 인덱스를 확인할 수 있다.

```python
condition = s > 80

print(s[condition].index)
```

예:

```text
Index([1, 2], dtype='int64')
```

인덱스를 리스트로 바꾸려면:

```python
s[condition].index.tolist()
```

---

# 37. 함수와 메서드 구분

Series 학습에서도 중요하다.

## 함수

자료를 괄호 안에 넣는다.

```python
len(s)
sum(s)
max(s)
min(s)
```

형태:

```text
함수(자료)
```

---

## Series 메서드

Series 뒤에 `.`을 사용한다.

```python
s.mean()
s.sum()
s.value_counts()
s.sort_values()
```

형태:

```text
자료.메서드()
```

---

# 38. 속성과 메서드 구분 ⭐⭐⭐

## 속성

괄호 없음.

```python
s.size
s.shape
s.dtype
s.index
s.values
s.ndim
```

## 메서드

괄호 있음.

```python
s.mean()
s.count()
s.value_counts()
s.sort_values()
```

### 암기

```text
속성   → 정보 → ()
없음

메서드 → 동작 → ()
있음
```

물론 모든 경우가 이 문장 하나로 설명되는 것은 아니지만, 초반 구분에는 매우 유용하다.

---

# 39. 자주 하는 실수 ① `size()`

잘못:

```python
s.size()
```

올바른 코드:

```python
s.size
```

`size`는 속성이다.

---

# 40. 자주 하는 실수 ② `and`, `or`

잘못:

```python
s[(s > 70) and (s < 90)]
```

Series에서는:

```python
s[(s > 70) & (s < 90)]
```

또는:

```python
s[(s < 70) | (s > 90)]
```

---

# 41. 자주 하는 실수 ③ 조건 괄호 생략

권장하지 않음:

```python
s[s > 70 & s < 90]
```

올바른 습관:

```python
s[(s > 70) & (s < 90)]
```

---

# 42. 자주 하는 실수 ④ Series와 DataFrame 혼동

```python
df["온도"]
```

→ Series

```python
df[["온도"]]
```

→ DataFrame

두 결과의 형태가 다르기 때문에 이후 코드에도 영향을 준다.

---

# 43. 자주 하는 실수 ⑤ `count()`를 전체 행 수라고 생각함

결측치가 있으면:

```python
s.count()
```

은 전체 칸 수가 아니다.

```text
전체 칸 → size / len
실제 값 → count
```

---

# 44. 자주 하는 실수 ⑥ 인덱스와 위치 혼동

인덱스가 다음과 같다고 하자.

```python
s = pd.Series(
    [100, 200, 300],
    index=[10, 20, 30]
)
```

```text
위치       index       value
0           10          100
1           20          200
2           30          300
```

```python
s.loc[10]
```

→ index가 10인 값

```text
100
```

```python
s.iloc[0]
```

→ 첫 번째 위치의 값

```text
100
```

### 핵심

```text
index 번호와 위치 번호는 같은 개념이 아니다.
```

---

# 45. `copy()`를 사용하는 이유

Series를 별도로 수정하고 싶다면:

```python
new_s = s.copy()
```

를 사용할 수 있다.

이후:

```python
new_s.iloc[0] = 999
```

처럼 수정해도 원본 `s`와 분리해서 관리하기 쉽다.

### 활용

```text
원본 데이터는 보존
↓
복사본에서 전처리
↓
분석
```

---

# 46. Series의 대표적인 활용 분야

## 1) 센서 데이터 분석

```python
df["온도"]
df["압력"]
df["진동"]
```

특정 센서 값을 분석할 때 사용.

---

## 2) 이상값 탐지

```python
df["온도"] > 90
```

```python
df["진동"] > df["진동"].mean() + 3 * df["진동"].std()
```

---

## 3) 범주형 데이터 분석

```python
df["result"].value_counts()
```

---

## 4) 조건 필터링

```python
df["품질등급"].isin(["불량", "주의"])
```

---

## 5) 통계 계산

```python
df["온도"].mean()
df["온도"].std()
df["온도"].var()
```

---

# 47. 분석 흐름으로 이해하기 ⭐⭐⭐

Series는 단독으로 외우기보다 데이터 분석 흐름 속에서 이해하는 것이 좋다.

```text
① 데이터 불러오기
      ↓
② DataFrame 구조 확인
      ↓
③ 필요한 열 선택
      ↓
④ Series 생성
      ↓
⑤ 조건 만들기
      ↓
⑥ 필터링
      ↓
⑦ 계산 / 통계
      ↓
⑧ 결과 해석
```

예:

```python
import pandas as pd

df = pd.read_csv("sensor.csv")

temp = df["온도"]

condition = temp > 90

result = df[condition]

print(result)
```

---

# 48. Series에서 꼭 기억해야 할 핵심 메서드

## 데이터 확인

```python
s.head()
s.tail()
```

## 통계

```python
s.sum()
s.mean()
s.min()
s.max()
s.median()
s.var()
s.std()
s.count()
```

## 값 종류 분석

```python
s.value_counts()
s.unique()
s.nunique()
```

## 정렬

```python
s.sort_values()
s.sort_index()
```

## 조건

```python
s.isin([...])
s.between(a, b)
s.isna()
s.notna()
```

## 결측치

```python
s.dropna()
s.fillna(...)
```

## 변경

```python
s.replace(...)
s.map(...)
```

---

# 49. Series에서 꼭 기억해야 할 속성

```python
s.index
s.values
s.dtype
s.shape
s.size
s.ndim
s.name
```

---

# 50. 최종 핵심 비교표 ⭐⭐⭐

| 목적 | 코드 |
|---|---|
| 한 열 선택 | `df["온도"]` |
| 여러 열 선택 | `df[["온도", "진동"]]` |
| 인덱스 이름으로 선택 | `s.loc[...]` |
| 위치 번호로 선택 | `s.iloc[...]` |
| 조건 만들기 | `s > 80` |
| 조건 필터링 | `s[s > 80]` |
| AND | `(조건1) & (조건2)` |
| OR | `(조건1) \| (조건2)` |
| NOT | `~조건` |
| 여러 값 포함 | `s.isin([...])` |
| 범위 확인 | `s.between(a, b)` |
| 평균 | `s.mean()` |
| 표준편차 | `s.std()` |
| 분산 | `s.var()` |
| 전체 원소 수 | `s.size` |
| 결측치 제외 개수 | `s.count()` |
| 값별 빈도 | `s.value_counts()` |
| 고유값 | `s.unique()` |
| 고유값 개수 | `s.nunique()` |
| 결측치 확인 | `s.isna()` |
| 결측치 제거 | `s.dropna()` |
| 결측치 채우기 | `s.fillna(...)` |
| 값 정렬 | `s.sort_values()` |

---

# 51. 초보자가 가장 먼저 익혀야 할 우선순위

모든 기능을 한꺼번에 외울 필요는 없다.

## 1순위 ⭐⭐⭐

```python
df["컬럼"]
s.loc[]
s.iloc[]
s > 값
s[조건]
```

---

## 2순위 ⭐⭐⭐

```python
&
|
~
isin()
between()
```

---

## 3순위 ⭐⭐⭐

```python
mean()
sum()
min()
max()
count()
size
value_counts()
```

---

## 4순위 ⭐⭐

```python
isna()
fillna()
dropna()
sort_values()
unique()
nunique()
```

---

# 52. 최종 개념 지도

```text
                 Pandas Series
                      │
          ┌───────────┴───────────┐
          │                       │
       구조 이해                데이터 처리
          │                       │
   index / value            선택 / 조건 / 계산
          │                       │
  ┌───────┼───────┐       ┌──────┼────────┐
  │       │       │       │      │        │
dtype   shape    size     loc   iloc   Boolean
                                      Indexing
                                         │
                              ┌──────────┼──────────┐
                              │          │          │
                              &          |          ~
                              │          │          │
                           isin()    between()    NOT
                                         │
                                         ↓
                                  원하는 데이터 추출
                                         │
                                         ↓
                            평균 / 합계 / 표준편차 / 빈도
```

---

# 53. 마지막 한 문장 정리

> **Series는 "인덱스가 붙어 있는 1차원 데이터"이며, DataFrame의 한 열을 선택하고 조건을 만들고 통계를 계산하는 Pandas 분석의 핵심 구조이다.**

특히 아래 흐름을 자연스럽게 사용할 수 있으면 Series의 핵심을 이해한 것이다.

```python
temp = df["온도"]

condition = (temp >= 70) & (temp <= 90)

result = df[condition]

print(temp.mean())
print(result)
```

```text
열 선택
  ↓
Series
  ↓
조건 생성
  ↓
Boolean Series
  ↓
필터링
  ↓
통계 및 분석
```
