# 🐼 Pandas DataFrame 완전 정리

> **목표:** `DataFrame`이 무엇인지 정확히 이해하고,  
> 데이터를 **불러오기 → 확인 → 선택 → 필터링 → 정렬 → 그룹화 → 집계 → 해석**하는 흐름까지 자연스럽게 사용할 수 있도록 정리한다.

---

# 0. 한눈에 보는 DataFrame

```text
DataFrame
│
├─ 2차원 표 형태의 데이터
│   ├─ 행(row)
│   └─ 열(column)
│
├─ 데이터 확인
│   ├─ head()
│   ├─ tail()
│   ├─ info()
│   ├─ describe()
│   ├─ shape
│   ├─ columns
│   └─ dtypes
│
├─ 데이터 선택
│   ├─ df["컬럼"]
│   ├─ df[["컬럼1", "컬럼2"]]
│   ├─ loc[]
│   └─ iloc[]
│
├─ 필터링
│   ├─ 조건식
│   ├─ &
│   ├─ |
│   ├─ ~
│   ├─ isin()
│   └─ between()
│
├─ 정렬
│   └─ sort_values()
│
├─ 데이터 변경
│   ├─ 새 컬럼 추가
│   ├─ drop()
│   ├─ rename()
│   └─ astype()
│
├─ 결측치
│   ├─ isna()
│   ├─ dropna()
│   └─ fillna()
│
└─ 그룹 분석
    ├─ groupby()
    ├─ agg()
    ├─ size()
    ├─ count()
    └─ value_counts()
```

---

# 1. DataFrame이란?

## 💡 핵심 개념

`DataFrame`은 **행과 열로 이루어진 2차원 표 형태의 데이터 구조**이다.

쉽게 말하면:

> **엑셀 표처럼 생긴 Pandas의 핵심 데이터 구조**

예:

```python
import pandas as pd

df = pd.DataFrame({
    "설비": ["모터", "펌프", "팬"],
    "온도": [78, 92, 85],
    "진동": [2.1, 4.8, 2.9]
})

print(df)
```

결과:

```text
   설비  온도   진동
0  모터  78  2.1
1  펌프  92  4.8
2   팬  85  2.9
```

구조를 그림으로 보면:

```text
          column
       ↓    ↓    ↓
index  설비   온도   진동
  0    모터   78    2.1
  1    펌프   92    4.8
  2    팬    85    2.9
```

---

# 2. DataFrame의 핵심 구조

DataFrame에는 크게 세 가지가 있다.

```text
DataFrame
├─ index   : 행의 이름/번호
├─ columns : 열의 이름
└─ values  : 실제 데이터
```

예:

```python
print(df.index)
print(df.columns)
print(df.values)
```

---

# 3. DataFrame과 Series 차이 ⭐⭐⭐

| 구분 | Series | DataFrame |
|---|---|---|
| 차원 | 1차원 | 2차원 |
| 모양 | 한 줄 | 표 |
| 예 | 온도 한 열 | 전체 센서 데이터 |
| 컬럼 수 | 보통 1개 | 여러 개 |
| 대표 선택 | `df["온도"]` | `df[["온도", "진동"]]` |

예:

```python
df["온도"]
```

→ `Series`

```python
df[["온도"]]
```

→ `DataFrame`

### ⭐ 암기

```text
[ ]      → 한 열 → Series
[[ ]]    → 여러 열 형태 → DataFrame
```

---

# 4. DataFrame 생성하기

## 4-1. 딕셔너리로 만들기

```python
df = pd.DataFrame({
    "이름": ["철수", "영희", "민수"],
    "점수": [80, 95, 70]
})
```

결과:

```text
   이름  점수
0  철수  80
1  영희  95
2  민수  70
```

---

## 4-2. 리스트로 만들기

```python
data = [
    ["모터", 78],
    ["펌프", 92],
    ["팬", 85]
]

df = pd.DataFrame(data, columns=["설비", "온도"])
```

---

# 5. CSV 파일 불러오기 ⭐⭐⭐

실전에서는 직접 DataFrame을 만드는 것보다 파일에서 불러오는 경우가 많다.

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

예:

```python
df = pd.read_csv("data/14_hydraulic.csv")
```

### 핵심

```text
CSV 파일
   ↓
pd.read_csv()
   ↓
DataFrame
```

---

# 6. 데이터 분석 기본 흐름 ⭐⭐⭐

DataFrame 분석은 이 순서로 생각하면 좋다.

```text
① 데이터 불러오기
      ↓
② 구조 확인
      ↓
③ 필요한 열 선택
      ↓
④ 조건 필터링
      ↓
⑤ 정렬
      ↓
⑥ 그룹화 / 집계
      ↓
⑦ 결과 해석
```

예:

```python
import pandas as pd

df = pd.read_csv("sensor.csv")

print(df.head())
print(df.info())

result = df[df["온도"] > 90]

result = result.sort_values("온도", ascending=False)

print(result)
```

---

# 7. `head()` ⭐⭐⭐

앞부분 데이터를 확인한다.

```python
df.head()
```

기본적으로 5개 행을 보여준다.

```python
df.head(10)
```

→ 앞에서 10개 행.

### 활용

파일을 불러온 뒤 가장 먼저 데이터 형태를 빠르게 확인할 때 사용한다.

---

# 8. `tail()`

마지막 데이터를 확인한다.

```python
df.tail()
```

```python
df.tail(3)
```

---

# 9. `info()` ⭐⭐⭐

DataFrame의 구조를 종합적으로 확인한다.

```python
df.info()
```

확인 가능한 것:

```text
행 개수
컬럼 이름
결측치 여부
데이터 타입
메모리 사용량
```

예:

```text
온도      120 non-null  float64
상태      120 non-null  object
```

### 특히 중요

```text
non-null 개수
dtype
```

를 확인한다.

---

# 10. `shape` ⭐⭐⭐

DataFrame의 크기를 확인한다.

```python
df.shape
```

결과 예:

```text
(100, 7)
```

뜻:

```text
100행 × 7열
```

### ⚠️ 주의

`shape`은 메서드가 아니라 속성이다.

```python
df.shape      # O
df.shape()    # X
```

---

# 11. `columns`

컬럼 이름 확인.

```python
df.columns
```

예:

```text
Index(['샷', '실린더압력', '주조압력', '사이클타임'], dtype='object')
```

---

# 12. `dtypes`

각 컬럼의 데이터 타입 확인.

```python
df.dtypes
```

예:

```text
온도      float64
진동      float64
상태      object
```

---

# 13. `describe()` ⭐⭐

수치형 데이터의 기초 통계를 한 번에 확인한다.

```python
df.describe()
```

대표 결과:

```text
count
mean
std
min
25%
50%
75%
max
```

### 활용

데이터의:

```text
평균
표준편차
최소/최대
분포
```

를 빠르게 확인할 수 있다.

---

# 14. 한 컬럼 선택하기 ⭐⭐⭐

```python
df["온도"]
```

결과:

```text
Series
```

예:

```python
temp = df["온도"]
```

이제:

```python
temp.mean()
temp.max()
temp.std()
```

처럼 Series 기능을 사용할 수 있다.

---

# 15. 여러 컬럼 선택하기 ⭐⭐⭐

```python
df[["온도", "진동"]]
```

결과:

```text
DataFrame
```

### 핵심

```python
df["온도"]             # Series
df[["온도", "진동"]]    # DataFrame
```

---

# 16. `loc` ⭐⭐⭐

`loc`는 **행/열의 이름(label)을 기준으로 선택**한다.

기본 형태:

```python
df.loc[행, 열]
```

---

## 특정 행 선택

```python
df.loc[0]
```

---

## 특정 행, 특정 열

```python
df.loc[0, "온도"]
```

---

## 여러 열 선택

```python
df.loc[:, ["온도", "진동"]]
```

여기서:

```text
:
```

는 모든 행을 의미한다.

---

# 17. `iloc` ⭐⭐⭐

`iloc`는 **위치 번호를 기준으로 선택**한다.

```python
df.iloc[0]
```

→ 첫 번째 행

```python
df.iloc[0, 1]
```

→ 첫 번째 행, 두 번째 열

---

## 여러 행과 열

```python
df.iloc[0:3, 1:4]
```

뜻:

```text
0~2번 행
1~3번 열
```

### 핵심

```text
loc  → 이름 기준
iloc → 위치 기준
```

---

# 18. 행 슬라이싱

```python
df.iloc[0:5]
```

→ 0~4번 행

```python
df.loc[0:5]
```

→ index 0~5

### 차이

```text
iloc → 끝 위치 제외
loc  → 끝 라벨 포함
```

---

# 19. 조건 만들기 ⭐⭐⭐

예:

```python
df["온도"] > 90
```

결과는:

```text
Boolean Series
```

예:

```text
0    False
1     True
2    False
```

즉:

```text
DataFrame의 한 열
     ↓
Series
     ↓
조건 비교
     ↓
Boolean Series
```

---

# 20. 불리언 인덱싱 ⭐⭐⭐

조건에 맞는 행만 선택한다.

```python
df[df["온도"] > 90]
```

구조:

```text
df[조건]
```

예:

```python
condition = df["온도"] > 90

result = df[condition]
```

---

# 21. AND 조건 `&` ⭐⭐⭐

예:

```python
df[(df["온도"] >= 70) & (df["온도"] <= 90)]
```

뜻:

```text
온도가 70 이상이고
90 이하
```

---

# 22. OR 조건 `|` ⭐⭐⭐

```python
df[(df["온도"] > 90) | (df["진동"] > 4)]
```

뜻:

```text
온도가 90 초과
또는
진동이 4 초과
```

---

# 23. NOT 조건 `~` ⭐⭐⭐

```python
df[~(df["상태"] == "정상")]
```

→ 상태가 정상이 아닌 행.

보통 `isin()`과 함께 많이 사용한다.

```python
df[~df["상태"].isin(["정상", "점검"])]
```

---

# 24. 조건식에서는 괄호가 중요 ⭐⭐⭐

잘못된 예:

```python
df[df["온도"] > 70 & df["온도"] < 90]
```

권장:

```python
df[(df["온도"] > 70) & (df["온도"] < 90)]
```

### 암기

```text
조건 하나마다 괄호
```

---

# 25. `isin()` ⭐⭐⭐

여러 값 중 하나와 일치하는 행을 선택한다.

```python
df[df["상태"].isin(["고장", "경고"])]
```

뜻:

```text
상태가 "고장" 또는 "경고"
```

다음과 비슷하다.

```python
df[(df["상태"] == "고장") | (df["상태"] == "경고")]
```

값이 많아질수록 `isin()`이 훨씬 편하다.

---

# 26. `between()` ⭐⭐

범위 조건을 간단하게 표현한다.

```python
df[df["온도"].between(70, 90)]
```

뜻:

```text
70 <= 온도 <= 90
```

다음과 비슷하다.

```python
df[(df["온도"] >= 70) & (df["온도"] <= 90)]
```

---

# 27. 문자열 조건

문자열 컬럼에는 `.str` 기능을 사용할 수 있다.

예:

```python
df[df["설비"].str.contains("모터")]
```

뜻:

```text
설비 이름에 "모터"가 포함된 행
```

---

# 28. 데이터 정렬 `sort_values()` ⭐⭐⭐

## 한 컬럼 기준 정렬

```python
df.sort_values("온도")
```

기본은 오름차순.

```text
작은 값 → 큰 값
```

---

## 내림차순

```python
df.sort_values("온도", ascending=False)
```

```text
큰 값 → 작은 값
```

---

# 29. 여러 컬럼 기준 정렬

```python
df.sort_values(
    ["상태", "온도"],
    ascending=[True, False]
)
```

뜻:

```text
상태 → 오름차순
온도 → 내림차순
```

---

# 30. 원본 수정 여부 ⭐⭐⭐

대부분의 Pandas 메서드는 기본적으로:

> 원본을 바로 바꾸지 않고 새로운 결과를 반환한다.

예:

```python
df.sort_values("온도")
```

만 실행해도 원본 `df`가 자동으로 바뀌는 것은 아니다.

저장하려면:

```python
df = df.sort_values("온도")
```

또는 복사본 사용:

```python
df_sorted = df.sort_values("온도")
```

---

# 31. 새 컬럼 추가 ⭐⭐⭐

예:

```python
df["위험여부"] = df["온도"] > 90
```

결과 개념:

```text
설비   온도   위험여부
모터   78     False
펌프   92     True
```

---

# 32. 계산 결과를 새 컬럼으로 만들기

예:

```python
df["평균센서값"] = (df["온도"] + df["진동"]) / 2
```

실전에서는 의미가 맞는 컬럼끼리 계산해야 한다.

---

# 33. 컬럼 삭제 `drop()` ⭐⭐⭐

```python
df.drop(columns=["온도"])
```

여러 컬럼:

```python
df.drop(columns=["온도", "진동"])
```

---

# 34. 행 삭제

```python
df.drop(index=[0])
```

여러 행:

```python
df.drop(index=[0, 2])
```

---

# 35. `inplace=True` 주의

다음처럼 사용할 수도 있다.

```python
df.drop(columns=["온도"], inplace=True)
```

그러면 원본이 직접 수정된다.

하지만 초보 단계에서는:

```python
df = df.drop(columns=["온도"])
```

처럼 명시적으로 다시 저장하는 방식이 흐름을 이해하기 쉽다.

---

# 36. 컬럼 이름 변경 `rename()`

```python
df = df.rename(columns={
    "온도": "temperature",
    "진동": "vibration"
})
```

---

# 37. 데이터 타입 변경 `astype()`

예:

```python
df["온도"] = df["온도"].astype(float)
```

문자열로 변경:

```python
df["설비"] = df["설비"].astype(str)
```

---

# 38. 결측치란?

데이터가 비어 있는 값을 흔히:

```text
NaN
```

이라고 한다.

예:

```text
설비   온도
모터   78
펌프   NaN
팬     85
```

---

# 39. 결측치 확인 `isna()` ⭐⭐⭐

```python
df.isna()
```

각 값이 결측치인지 True/False로 확인한다.

---

## 컬럼별 결측치 개수

```python
df.isna().sum()
```

매우 자주 사용한다.

결과 예:

```text
온도    2
진동    1
상태    0
```

---

# 40. 결측치 제거 `dropna()`

```python
df.dropna()
```

결측치가 있는 행을 제거한다.

---

## 특정 컬럼 기준

```python
df.dropna(subset=["온도"])
```

→ 온도가 비어 있는 행만 제거.

---

# 41. 결측치 채우기 `fillna()`

```python
df["온도"] = df["온도"].fillna(0)
```

평균값으로 채우기:

```python
df["온도"] = df["온도"].fillna(df["온도"].mean())
```

### ⚠️ 주의

무조건 0이나 평균으로 채우면 안 된다.

결측치 처리 방법은:

```text
데이터 의미
분석 목적
결측치 발생 원인
```

에 따라 달라진다.

---

# 42. 중복 데이터 확인

```python
df.duplicated()
```

중복 행 개수:

```python
df.duplicated().sum()
```

---

# 43. 중복 제거

```python
df.drop_duplicates()
```

---

# 44. `value_counts()` ⭐⭐⭐

특정 컬럼의 값별 개수를 확인한다.

```python
df["상태"].value_counts()
```

예:

```text
정상    80
고장    25
점검    15
```

범주형 데이터 분석에서 매우 중요하다.

---

# 45. 그룹화 `groupby()` ⭐⭐⭐

`groupby()`는 같은 범주의 데이터를 묶어서 분석할 때 사용한다.

예:

```python
df.groupby("상태")
```

이것만으로는 보통 최종 결과가 나오지 않는다.

뒤에 계산을 붙인다.

```python
df.groupby("상태")["온도"].mean()
```

뜻:

```text
상태별로 묶고
↓
온도를 선택해서
↓
평균 계산
```

---

# 46. `groupby()` 흐름 ⭐⭐⭐

```text
전체 데이터
   ↓
기준 컬럼으로 그룹 나누기
   ↓
분석할 컬럼 선택
   ↓
집계 함수 적용
```

예:

```python
df.groupby("냉각기상태")["온도"].mean()
```

```text
냉각기상태
   ↓
정상 그룹 / 이상 그룹
   ↓
각 그룹의 온도 평균
```

---

# 47. 여러 기준으로 그룹화

```python
df.groupby(["학년", "반"]).size()
```

뜻:

```text
학년별
  ↓
그 안에서 반별
  ↓
학생 수 계산
```

---

# 48. `size()` vs `count()` ⭐⭐⭐

## `size()`

그룹의 **전체 행 수**.

```python
df.groupby("학년").size()
```

---

## `count()`

결측치를 제외한 값의 개수.

```python
df.groupby("학년")["국어"].count()
```

### 차이

```text
size()  → 행 개수
count() → NaN 제외 개수
```

---

# 49. `agg()` ⭐⭐⭐

여러 통계를 한 번에 계산할 때 사용한다.

예:

```python
df.groupby("상태")["온도"].agg([
    "mean",
    "std",
    "min",
    "max"
])
```

결과:

```text
       mean   std   min   max
상태
정상    ...
고장    ...
```

---

# 50. 여러 컬럼을 한 번에 집계

```python
result = df.groupby("냉각기상태").agg({
    "온도": ["mean", "std"],
    "진동": ["mean"],
    "압력": ["min", "max"]
})
```

### 의미

```text
냉각기상태별
│
├─ 온도 평균
├─ 온도 표준편차
├─ 진동 평균
├─ 압력 최소
└─ 압력 최대
```

---

# 51. `round()`로 소수점 정리

```python
result = result.round(2)
```

→ 소수 둘째 자리까지.

예:

```python
df.groupby("상태")["온도"].mean().round(2)
```

---

# 52. `mean()`, `std()`, `var()` 활용

예:

```python
df["온도"].mean()
df["온도"].std()
df["온도"].var()
```

뜻:

```text
mean → 평균
std  → 표준편차
var  → 분산
```

---

# 53. `min()`, `max()`

```python
df["온도"].min()
df["온도"].max()
```

최솟값과 최댓값 확인.

---

# 54. 조건 + 그룹 분석

예:

온도가 80 이상인 데이터만 선택 후 상태별 평균:

```python
filtered = df[df["온도"] >= 80]

result = filtered.groupby("상태")["진동"].mean()
```

분석 흐름:

```text
전체 데이터
   ↓
조건 필터링
   ↓
필요 데이터만 남김
   ↓
그룹화
   ↓
평균 계산
```

---

# 55. 실전 예제 ① 센서 위험값 필터링

데이터:

```text
설비   회전수   토크
A     1500     50
B     2300     25
C     1800     40
```

위험 조건:

```text
회전수 > 2000
또는
토크 < 30
```

코드:

```python
danger = (df["회전수"] > 2000) | (df["토크"] < 30)

result = df[danger]
```

---

# 56. 실전 예제 ② 정상 범위 필터링

```python
normal = df["온도"].between(70, 90)

result = df[normal]
```

정상 범위를 벗어난 값:

```python
result = df[~normal]
```

---

# 57. 실전 예제 ③ 특정 상태만 선택

```python
result = df[df["result"].isin(["고장", "주의"])]
```

---

# 58. 실전 예제 ④ 상태별 평균

```python
result = df.groupby("result")["온도"].mean()
```

---

# 59. 실전 예제 ⑤ 여러 통계 집계

```python
result = df.groupby("냉각기상태").agg({
    "온도": ["mean", "std"],
    "진동": ["mean"],
    "냉각효율": ["mean"]
})

result = result.round(2)

print(result)
```

---

# 60. 실전 예제 ⑥ 학년/반별 분석

학생 데이터가 있다고 하자.

```text
학년   반   국어
1     1    80
1     1    90
1     2    70
2     1    95
```

## 전체 학생 수

```python
len(df)
```

또는:

```python
df.shape[0]
```

---

## 학년별 학생 수

```python
df.groupby("학년").size()
```

---

## 학년-반별 학생 수

```python
df.groupby(["학년", "반"]).size()
```

---

## 학년-반별 국어 평균

```python
df.groupby(["학년", "반"])["국어"].mean().round(2)
```

---

# 61. `copy()` ⭐⭐⭐

원본 데이터를 보존하면서 수정하고 싶다면:

```python
df_copy = df.copy()
```

이후:

```python
df_copy["온도"] = df_copy["온도"].fillna(0)
```

### 활용 흐름

```text
원본 df
   ↓
copy()
   ↓
전처리용 df_copy
   ↓
수정 / 분석
```

---

# 62. `reset_index()`

필터링이나 그룹화 후 인덱스를 다시 정리할 때 사용한다.

```python
result = result.reset_index()
```

예:

```text
기존 index
2
5
8
```

를:

```text
0
1
2
```

처럼 다시 정리할 수 있다.

---

# 63. `set_index()`

특정 컬럼을 인덱스로 지정한다.

```python
df = df.set_index("설비")
```

이후:

```python
df.loc["모터"]
```

처럼 이름 기반으로 접근하기 쉬워진다.

---

# 64. `drop=True` 주의

```python
df.reset_index(drop=True)
```

`drop=True`를 사용하면 기존 인덱스를 새 컬럼으로 만들지 않고 버린다.

---

# 65. 행/열 개수 확인 방법

## 전체 행 수

```python
len(df)
```

또는:

```python
df.shape[0]
```

---

## 전체 열 수

```python
df.shape[1]
```

---

## 전체 원소 수

```python
df.size
```

예:

```text
100행 × 7열
```

이면:

```text
700
```

---

# 66. `size`와 `shape` 차이 ⭐⭐⭐

예:

```text
100행 × 7열
```

```python
df.shape
```

→

```text
(100, 7)
```

```python
df.size
```

→

```text
700
```

### 암기

```text
shape → 행, 열 구조
size  → 전체 칸 수
```

---

# 67. 자주 하는 실수 ① `shape()`

잘못:

```python
df.shape()
```

올바른 코드:

```python
df.shape
```

---

# 68. 자주 하는 실수 ② `columns()`

잘못:

```python
df.columns()
```

올바른 코드:

```python
df.columns
```

`columns`도 속성이다.

---

# 69. 자주 하는 실수 ③ 한 열과 여러 열 혼동

```python
df["온도"]
```

→ Series

```python
df[["온도"]]
```

→ DataFrame

이 차이를 이해하지 못하면 이후 함수 사용에서 헷갈릴 수 있다.

---

# 70. 자주 하는 실수 ④ `groupby[]`

잘못:

```python
df.groupby["학년"]
```

올바른 코드:

```python
df.groupby("학년")
```

### 이유

`groupby`는 메서드이므로 `()`를 사용한다.

---

# 71. 자주 하는 실수 ⑤ 여러 그룹 컬럼 지정

잘못:

```python
df.groupby["학년", "반"]
```

올바른 코드:

```python
df.groupby(["학년", "반"])
```

---

# 72. 자주 하는 실수 ⑥ `and`, `or`

잘못:

```python
df[(df["온도"] > 70) and (df["온도"] < 90)]
```

올바른 코드:

```python
df[(df["온도"] > 70) & (df["온도"] < 90)]
```

---

# 73. 자주 하는 실수 ⑦ 조건 괄호 생략

잘못:

```python
df[df["온도"] > 70 & df["온도"] < 90]
```

올바른 코드:

```python
df[(df["온도"] > 70) & (df["온도"] < 90)]
```

---

# 74. 자주 하는 실수 ⑧ `count()`와 전체 행 수 혼동

결측치가 있으면:

```python
df["온도"].count()
```

은 전체 행 수와 다를 수 있다.

전체 행 수:

```python
len(df)
```

또는:

```python
df.shape[0]
```

---

# 75. 자주 하는 실수 ⑨ 원본이 자동으로 바뀐다고 생각함

예:

```python
df.sort_values("온도")
```

이 결과를 보기만 하면 원본은 보통 그대로다.

저장:

```python
df = df.sort_values("온도")
```

---

# 76. 함수 / 메서드 / 속성 구분 ⭐⭐⭐

## 함수

```python
len(df)
```

형태:

```text
함수(자료)
```

---

## 메서드

```python
df.head()
df.info()
df.sort_values()
df.groupby()
```

형태:

```text
자료.메서드()
```

---

## 속성

```python
df.shape
df.columns
df.dtypes
df.index
df.values
df.size
```

형태:

```text
자료.속성
```

---

# 77. DataFrame에서 꼭 기억해야 할 메서드

## 불러오기

```python
pd.read_csv()
```

## 확인

```python
df.head()
df.tail()
df.info()
df.describe()
```

## 선택

```python
df.loc[]
df.iloc[]
```

## 정렬

```python
df.sort_values()
```

## 삭제 / 변경

```python
df.drop()
df.rename()
df.astype()
```

## 결측치

```python
df.isna()
df.dropna()
df.fillna()
```

## 그룹

```python
df.groupby()
df.agg()
```

## 기타

```python
df.copy()
df.reset_index()
df.set_index()
df.drop_duplicates()
```

---

# 78. DataFrame에서 꼭 기억해야 할 속성

```python
df.shape
df.columns
df.index
df.dtypes
df.values
df.size
df.ndim
```

---

# 79. 가장 중요한 선택 문법 모음 ⭐⭐⭐

| 목적 | 코드 |
|---|---|
| 한 열 | `df["온도"]` |
| 여러 열 | `df[["온도", "진동"]]` |
| 행/열 이름 기준 | `df.loc[...]` |
| 행/열 위치 기준 | `df.iloc[...]` |
| 조건 필터링 | `df[조건]` |
| 특정 값들 | `df[df["상태"].isin([...])]` |
| 범위 | `df[df["온도"].between(a, b)]` |

---

# 80. 가장 중요한 분석 문법 모음 ⭐⭐⭐

| 목적 | 코드 |
|---|---|
| 앞부분 확인 | `df.head()` |
| 구조 확인 | `df.info()` |
| 크기 | `df.shape` |
| 평균 | `df["온도"].mean()` |
| 표준편차 | `df["온도"].std()` |
| 값별 개수 | `df["상태"].value_counts()` |
| 정렬 | `df.sort_values("온도")` |
| 그룹 평균 | `df.groupby("상태")["온도"].mean()` |
| 다중 집계 | `df.groupby("상태").agg(...)` |
| 결측치 개수 | `df.isna().sum()` |

---

# 81. 초보자가 가장 먼저 익힐 우선순위

## 1순위 ⭐⭐⭐

```python
pd.read_csv()
df.head()
df.info()
df.shape
df.columns
```

---

## 2순위 ⭐⭐⭐

```python
df["컬럼"]
df[["컬럼1", "컬럼2"]]
df.loc[]
df.iloc[]
```

---

## 3순위 ⭐⭐⭐

```python
df[조건]
&
|
~
isin()
between()
```

---

## 4순위 ⭐⭐⭐

```python
sort_values()
value_counts()
groupby()
mean()
size()
agg()
```

---

## 5순위 ⭐⭐

```python
isna()
fillna()
dropna()
copy()
reset_index()
```

---

# 82. 추천 학습 흐름

처음부터 모든 메서드를 외우려고 하지 말고:

```text
불러오기
↓
확인
↓
선택
↓
필터링
↓
정렬
↓
그룹 분석
```

이 순서를 먼저 익힌다.

실전에서 대부분의 분석은 이 흐름 안에서 이루어진다.

---

# 83. Series와 DataFrame 연결 구조 ⭐⭐⭐

```text
DataFrame
   │
   ├─ df["온도"]
   │       ↓
   │     Series
   │       ↓
   │    조건 생성
   │       ↓
   │ Boolean Series
   │       ↓
   └──→ df[조건]
           ↓
      필터링된 DataFrame
```

예:

```python
temp = df["온도"]

condition = temp > 90

result = df[condition]
```

---

# 84. 최종 개념 지도

```text
                    Pandas DataFrame
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
     구조 확인            데이터 선택          데이터 분석
       │                   │                   │
 head / info           column / row       filter / group
 shape / dtype          loc / iloc             │
       │                   │                   │
       │                   ↓             ┌─────┼─────┐
       │                Series            │     │     │
       │                   │            sort group  agg
       │                   ↓
       │             Boolean Series
       │                   │
       └───────────────────┴───────────────┐
                                           ↓
                                  필요한 데이터 추출
                                           ↓
                               평균 / 개수 / 표준편차
                                           ↓
                                      결과 해석
```

---

# 85. 실전 분석 전체 예제 ⭐⭐⭐

```python
import pandas as pd

# 1. 데이터 불러오기
df = pd.read_csv("data/14_hydraulic.csv")

# 2. 데이터 확인
print(df.head())
print(df.info())
print(df.shape)

# 3. 필요한 열 선택
sensor = df[["냉각기상태", "온도", "진동"]]

# 4. 조건 필터링
filtered = sensor[
    (sensor["온도"] > 80) | (sensor["진동"] > 4)
]

# 5. 정렬
filtered = filtered.sort_values(
    "온도",
    ascending=False
)

# 6. 그룹 분석
result = filtered.groupby("냉각기상태").agg({
    "온도": ["mean", "std"],
    "진동": ["mean", "count"]
})

# 7. 소수점 정리
result = result.round(2)

# 8. 결과 출력
print(result)
```

분석 흐름:

```text
CSV
 ↓
DataFrame
 ↓
구조 확인
 ↓
필요 컬럼 선택
 ↓
조건 필터링
 ↓
정렬
 ↓
groupby
 ↓
agg
 ↓
결과 해석
```

---

# 86. 마지막 한 문장 정리

> **DataFrame은 행과 열로 이루어진 2차원 표 형태의 데이터이며, Pandas 데이터 분석의 중심이 되는 구조이다.**

가장 중요한 흐름은:

```text
불러오기
  ↓
확인
  ↓
선택
  ↓
필터링
  ↓
정렬
  ↓
그룹화
  ↓
집계
  ↓
해석
```

이다.

이 흐름을 자연스럽게 사용할 수 있으면 DataFrame의 핵심을 제대로 이해한 것이다.
