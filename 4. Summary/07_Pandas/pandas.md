# 🐼 Pandas 기초 → 데이터 분석 전체 정리

## 0. 📌 먼저 보는 전체 요약

Pandas를 처음 배울 때는 아래 흐름만 먼저 머릿속에 넣으면 된다.

```text
CSV / Excel 같은 표 데이터
          ↓
      Pandas로 불러오기
          ↓
       DataFrame
          ↓
┌─────────┼─────────┐
구조 확인   데이터 선택   데이터 정리
          ↓
       통계 분석
          ↓
       결과 저장
```

### 핵심 기능 요약

| 하고 싶은 일     | 사용하는 코드               | 쉽게 말하면          |
| ----------- | --------------------- | --------------- |
| Pandas 불러오기 | `import pandas as pd` | Pandas 사용 준비    |
| CSV 읽기      | `pd.read_csv()`       | 파일 → 표          |
| 앞부분 보기      | `df.head()`           | 앞 5줄 확인         |
| 크기 확인       | `df.shape`            | 몇 행 몇 열?        |
| 열 확인        | `df.columns`          | 어떤 데이터가 있지?     |
| 자료형 확인      | `df.dtypes`           | 숫자인가 문자인가?      |
| 전체 구조       | `df.info()`           | 데이터 건강검진        |
| 통계 확인       | `df.describe()`       | 평균·최대·최소 등      |
| 열 하나 선택     | `df["온도"]`            | 온도만 가져오기        |
| 조건 선택       | `df[df["온도"] >= 90]`  | 90도 이상만         |
| 결측치 확인      | `df.isna().sum()`     | 빈 값이 몇 개?       |
| 정렬          | `df.sort_values()`    | 큰 값부터 보기        |
| 종류별 개수      | `value_counts()`      | 정상 몇 개? 경고 몇 개? |
| 그룹별 분석      | `groupby()`           | 설비별 평균          |
| CSV 저장      | `to_csv()`            | 분석 결과 저장        |

---

# 1. Pandas는 무엇인가?

## 💡 개념

Pandas는 **행과 열로 된 데이터를 다루기 위한 Python 라이브러리**다.

예를 들어:

```text
측정시각    설비    온도    전류
09:00      M01     72      20
09:01      M01     75      21
09:02      M02     95      35
```

이런 데이터를 Python에서 편하게 처리한다.

PDF에서는 설비 센서가 1초마다 기록되면 하루에도 매우 많은 행이 만들어지므로, 엑셀 손작업보다 코드 처리가 **대량 처리·재사용·정확성** 면에서 유리하다고 설명한다. 

### 언제 사용하는가?

* 센서 로그 분석
* 판매 데이터 분석
* 고객 데이터 분석
* 품질 데이터 분석
* 머신러닝 전처리
* CSV/Excel 자동 처리

---

# 2. Series와 DataFrame

이걸 먼저 알아야 뒤가 쉬워진다.

## DataFrame

**표 전체**

```python
import pandas as pd

df = pd.DataFrame({
    "설비": ["M01", "M02", "M03"],
    "온도": [70, 85, 95],
    "전류": [20, 25, 40]
})

print(df)
```

```text
    설비  온도  전류
0  M01  70   20
1  M02  85   25
2  M03  95   40
```

## Series

**DataFrame의 열 하나**

```python
temperature = df["온도"]

print(temperature)
```

```text
0    70
1    85
2    95
```

### 🚨 차이

| 코드           | 결과        |
| ------------ | --------- |
| `df["온도"]`   | Series    |
| `df[["온도"]]` | DataFrame |

즉:

```text
Series = 열 하나
DataFrame = 표 전체
```

PDF에서도 여러 Series가 모여 DataFrame을 구성한다고 설명한다. 

---

# 3. 행 · 열 · 인덱스

```text
index    설비    온도
0        M01     70
1        M02     85
2        M03     95
```

| 개념          | 의미              |
| ----------- | --------------- |
| 행 `row`     | 가로 한 줄, 데이터 한 건 |
| 열 `column`  | 같은 종류의 데이터      |
| 인덱스 `index` | 각 행의 이름표        |

설비 데이터라면 보통:

```text
한 행
→ 한 시점의 측정 결과

한 열
→ 온도 전체 / 전류 전체 등

index
→ 각 측정 기록의 행 번호
```

라고 이해하면 된다. PDF에서도 이 구조를 Pandas 표의 기본 개념으로 설명한다. 

---

# 4. Pandas 설치와 import

## 설치

터미널:

```bash
python -m pip install pandas
```

환경에 따라:

```bash
python3 -m pip install pandas
```

## Python에서 사용

```python
import pandas as pd
```

여기서:

```text
pandas = 라이브러리 이름
pd     = 별명
```

### 🚨 오류

```text
ModuleNotFoundError: No module named 'pandas'
```

가 나오면 **현재 실행 중인 Python 환경에 Pandas가 설치됐는지** 확인해야 한다.

---

# 5. CSV 불러오기 `read_csv()`

## 💡 개념

CSV 파일을 Pandas의 DataFrame으로 만드는 함수다.

```python
df = pd.read_csv("data/sensor.csv")
```

흐름:

```text
sensor.csv
    ↓
pd.read_csv()
    ↓
DataFrame
    ↓
df
```

PDF에서도 `read_csv()` 결과가 DataFrame으로 반환되고, 분석에 계속 사용하려면 변수에 담는 형태를 기본으로 설명한다. 

---

# 6. `read_csv()` 주요 옵션

## `sep`

**데이터를 나누는 구분자**

보통 CSV:

```text
온도,전류,압력
70,20,8.5
```

은:

```python
pd.read_csv("data.csv")
```

세미콜론이면:

```text
온도;전류;압력
70;20;8.5
```

```python
pd.read_csv("data.csv", sep=";")
```

### 🚨 언제 의심?

원래:

```text
200행 7열
```

이어야 하는데:

```python
print(df.shape)
```

결과가:

```text
(200, 1)
```

이라면 **구분자가 틀렸을 가능성**이 높다. PDF에서도 값을 한 열에 몰아 읽는 현상을 대표적인 `sep` 문제로 설명한다. 

---

## `encoding`

문자를 해석하는 방식이다.

```python
pd.read_csv(
    "data.csv",
    encoding="utf-8-sig"
)
```

한글 관련 문제가 생기면 파일에 맞춰 `utf-8`, `utf-8-sig`, `cp949` 등을 확인한다.

### 비교

```text
sep 문제
→ 열이 한 칸에 뭉침

encoding 문제
→ 문자가 깨지거나 디코딩 오류
```

---

## `usecols`

필요한 열만 읽는다.

```python
df = pd.read_csv(
    "data.csv",
    usecols=["측정시각", "온도", "전류"]
)
```

### 언제?

100개 센서 중 3개만 필요할 때.

### 장점

* 메모리 절약
* 처리량 감소
* 분석할 데이터가 명확

---

## `nrows`

처음 일부 행만 읽는다.

```python
df = pd.read_csv(
    "big_data.csv",
    nrows=100
)
```

### `nrows` vs `head()`

|              | `nrows=100`  | `head(100)` |
| ------------ | ------------ | ----------- |
| 언제?          | 파일 읽을 때      | 읽은 뒤        |
| 실제 메모리에 읽는 양 | 100행         | 전체 데이터      |
| 용도           | 대용량 파일 사전 점검 | 화면 확인       |

이 차이는 중요하다.

---

# 7. 데이터를 불러온 직후 해야 하는 일

PDF에서 가장 중요한 흐름 중 하나다. 

```python
df = pd.read_csv("data/sensor.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)

df.info()
```

## 왜 확인하는가?

분석 전에:

```text
파일이 제대로 읽혔나?
↓
행·열 개수가 맞나?
↓
필요한 열이 있나?
↓
숫자가 진짜 숫자로 읽혔나?
↓
비어 있는 값이 있나?
```

를 확인해야 한다.

---

# 8. `head()` · `tail()` · `sample()`

## `head()`

```python
df.head()
```

앞 5행.

파일을 불러온 직후 가장 먼저 사용한다.

## `tail()`

```python
df.tail()
```

마지막 5행.

시간순 로그의 마지막 기록을 볼 때 유용하다.

## `sample()`

```python
df.sample(5)
```

임의의 5행.

### 비교

| 메서드        | 보여주는 위치 |
| ---------- | ------- |
| `head()`   | 앞       |
| `tail()`   | 뒤       |
| `sample()` | 랜덤      |

### 🚨 주의

`head()`만 보면 **데이터 앞부분만 정상이고 뒷부분이 이상한 상황**을 놓칠 수도 있다.

---

# 9. `shape` · `columns` · `dtypes` · `info()`

## `shape`

```python
df.shape
```

```text
(200, 7)
```

뜻:

```text
200행
7열
```

### 🚨 속성

```python
df.shape
```

✅

```python
df.shape()
```

❌

---

## `columns`

```python
df.columns
```

열 이름을 확인한다.

특히:

```text
Usecols do not match columns
```

오류가 발생하면 실제 열 이름부터 확인한다.

---

## `dtypes`

```python
df.dtypes
```

열별 자료형.

예:

```text
측정시각     object
온도        float64
전류        float64
```

### 🚨 주의

겉보기에는 숫자여도:

```text
object
```

라면 문자열이 섞였을 수 있다.

---

## `info()`

```python
df.info()
```

한 번에:

* 행 수
* 열 수
* 열 이름
* Non-Null 개수
* 자료형
* 메모리 정보

등을 보여준다.

### `dtypes` vs `info()`

|        | `dtypes` | `info()` |
| ------ | -------- | -------- |
| 자료형    | O        | O        |
| 결측 여부  | X        | O        |
| 데이터 크기 | X        | O        |
| 메모리    | X        | O        |

`dtypes` = 자료형만 빠르게
`info()` = 전체 건강검진

---

# 10. ⭐ 통계는 무엇을 보는 것인가?

여기부터 더 중요하게 이해하면 돼.

통계는 어렵게 생각할 필요 없다.

> **많은 데이터를 숫자 몇 개로 요약해서 전체적인 특징을 알아보는 것**

이다.

센서 온도가 100만 개 있으면 전부 눈으로 볼 수 없다.

그래서:

```text
평균은?
가운데 값은?
가장 작은 값은?
가장 큰 값은?
얼마나 흔들리는가?
대부분 값이 어디에 있는가?
```

를 확인한다.

---

# 11. 평균 `mean()` ⭐⭐⭐⭐⭐

예:

```text
온도 = 70, 80, 90
```

평균:

```text
(70 + 80 + 90) ÷ 3
= 80
```

Pandas:

```python
df["온도"].mean()
```

## 의미

전체 데이터를 **공평하게 나눴을 때의 대표값**이라고 생각하면 쉽다.

예:

```text
설비 온도 평균 = 78도
```

→ “대체로 78도 근처에서 작동하는구나.”

genui{"descriptive_statistics_sampling_learning_block":{"type_id":"ARITHMETIC_MEAN"}}

### 🚨 평균의 문제점

데이터:

```text
50, 51, 52, 53, 300
```

300이라는 아주 큰 값 하나 때문에 평균이 크게 올라간다.

즉 평균은 **이상치에 영향을 많이 받는다.**

---

# 12. 중앙값 `median()` ⭐⭐⭐⭐⭐

숫자를 순서대로 세웠을 때 **정가운데 값**이다.

```text
50, 51, 52, 53, 300
```

중앙값:

```text
52
```

Pandas:

```python
df["온도"].median()
```

## 평균 vs 중앙값

|        | 평균        | 중앙값     |
| ------ | --------- | ------- |
| 계산     | 모두 더해서 나눔 | 가운데 값   |
| 이상치 영향 | 큼         | 작음      |
| 일반 데이터 | 좋음        | 좋음      |
| 극단값 존재 | 왜곡 가능     | 비교적 안정적 |

genui{"descriptive_statistics_sampling_learning_block":{"type_id":"MEAN_VS_MEDIAN"}}

### 실무 예

```text
평균 온도 = 82도
중앙값 = 70도
```

차이가 매우 크다면:

> 극단적으로 높은 온도가 몇 개 있는 것 아닌가?

라고 의심할 수 있다.

---

# 13. 최솟값과 최댓값 `min()`, `max()`

```python
df["온도"].min()
df["온도"].max()
```

예:

```text
평균 55도
최소 42도
최대 137도
```

이면:

> 최대 137도는 정상인가?

라는 질문이 생긴다.

통계는 이렇게 **이상한 부분을 발견하기 위한 출발점**으로 쓰인다.

---

# 14. 범위 Range

간단히:

```text
최댓값 - 최솟값
```

예:

```text
최소 50
최대 90

범위 = 40
```

Pandas에서는:

```python
temp_range = (
    df["온도"].max()
    - df["온도"].min()
)
```

### 한계

최솟값과 최댓값 단 두 개만 보기 때문에 이상치 하나에도 크게 영향을 받는다.

---

# 15. 분산과 표준편차 ⭐⭐⭐⭐⭐

여기서 많이 헷갈리는데 핵심은 하나다.

> **값들이 평균 주변에 얼마나 흩어져 있는가?**

## 예시 A

```text
온도:
78, 79, 80, 81, 82
```

평균 근처에 모여 있다.

→ 변동이 작음
→ 표준편차 작음

## 예시 B

```text
온도:
50, 65, 80, 95, 110
```

평균 주변에서 많이 떨어져 있다.

→ 변동이 큼
→ 표준편차 큼

Pandas:

```python
df["온도"].std()
```

genui{"descriptive_statistics_sampling_learning_block":{"type_id":"STANDARD_DEVIATION"}}

## 설비에서는 왜 중요한가?

평균 온도가 똑같아도:

```text
설비 A
79, 80, 80, 81, 80

설비 B
60, 70, 80, 90, 100
```

둘 다 평균은 약 80이다.

하지만 B는 훨씬 불안정하다.

따라서:

```text
평균
→ 중심이 어디인가?

표준편차
→ 얼마나 흔들리는가?
```

둘을 같이 봐야 한다.

---

# 16. 분산 `variance`는 무엇인가?

표준편차를 이해하기 위해 나온 개념이다.

쉽게:

```text
각 값이 평균에서 얼마나 떨어졌는지 계산
↓
그 차이를 제곱
↓
평균
↓
분산
```

Pandas:

```python
df["온도"].var()
```

## 분산 vs 표준편차

|       | 분산       | 표준편차  |
| ----- | -------- | ----- |
| 의미    | 퍼짐 정도    | 퍼짐 정도 |
| 단위    | 원래 단위²   | 원래 단위 |
| 해석    | 다소 어려움   | 쉬움    |
| 현업 설명 | 상대적으로 적음 | 많이 사용 |

예를 들어 온도가 `℃`이면:

```text
분산 → ℃²
표준편차 → ℃
```

이기 때문에 표준편차가 직관적이다.

---

# 17. 사분위수 `25%`, `50%`, `75%`

`describe()`를 보면:

```text
25%
50%
75%
```

가 나온다.

데이터를 작은 순서대로 정렬해서 네 덩어리로 나눈다고 생각하면 된다.

```text
최소
 │
25%   ← Q1
 │
50%   ← 중앙값 Q2
 │
75%   ← Q3
 │
최대
```

예:

```text
25% = 55
50% = 60
75% = 68
```

뜻:

```text
데이터의 25%가 55 이하
데이터의 절반이 60 이하
데이터의 75%가 68 이하
```

이다.

이 값들은 나중에 **IQR 이상치 탐지**와 직접 연결된다.

---

# 18. `describe()` 제대로 읽기 ⭐⭐⭐⭐⭐

```python
df.describe()
```

예:

```text
        온도
count   100
mean     70
std       5
min      55
25%      67
50%      70
75%      73
max     120
```

하나씩 읽으면:

```text
count = 100
→ 값이 100개 있음

mean = 70
→ 평균 70도

std = 5
→ 평균 주변으로 어느 정도 흔들림

min = 55
→ 최솟값

25% = 67
→ 25% 데이터가 67 이하

50% = 70
→ 중앙값

75% = 73
→ 75% 데이터가 73 이하

max = 120
→ 최대 120도
```

### 여기서 중요한 해석

대부분:

```text
67 ~ 73
```

근처인데 최대가:

```text
120
```

이면?

> 120도는 다른 값과 너무 떨어져 있는데?

라고 생각할 수 있다.

그 다음:

```python
df[df["온도"] >= 100]
```

처럼 실제 이상 시점을 확인한다.

즉:

```text
describe()
↓
이상한 숫자 발견
↓
조건 필터링
↓
실제 행 확인
```

이게 실무 흐름이다.

---

# 19. `count()` vs `size` vs `len()`

결측치가 있을 때 특히 중요하다.

데이터:

```text
70
80
NaN
90
```

## `count()`

```python
df["온도"].count()
```

→ `3`

**NaN 제외**

## `size`

```python
df["온도"].size
```

→ `4`

**NaN 포함**

## `len(df)`

```python
len(df)
```

→ DataFrame 행 개수

### 비교

| 코드        | 무엇을 세나?  |
| --------- | -------- |
| `count()` | 실제 값 개수  |
| `.size`   | 전체 요소 개수 |
| `len(df)` | 행 개수     |

---

# 20. NaN과 통계 ⭐⭐⭐⭐

```text
70
80
NaN
90
```

Pandas에서:

```python
df["온도"].mean()
```

은 기본적으로 NaN을 제외하고:

```text
(70 + 80 + 90) / 3
```

을 계산한다.

🚨 NaN을 `0`으로 보는 것이 아니다.

---

# 21. 결측치 확인

```python
df.isna().sum()
```

예:

```text
온도     15
전류      0
진동      2
```

뜻:

```text
온도 누락 15개
진동 누락 2개
```

## `isna()` vs `notna()`

```python
df["온도"].isna()
```

→ 없는 값이 `True`

```python
df["온도"].notna()
```

→ 있는 값이 `True`

---

# 22. `dropna()` vs `fillna()`

## 삭제

```python
df_clean = df.dropna(
    subset=["온도"]
)
```

## 채우기

```python
df["온도"] = df["온도"].fillna(
    df["온도"].mean()
)
```

### 🚨 매우 중요한 주의사항

결측치를 무조건:

```python
fillna(0)
```

하지 않는다.

```text
온도 = 0
```

은 실제 측정값일 수 있지만:

```text
온도 = NaN
```

은 측정값 자체가 없다는 뜻이다.

### 어떤 방법?

```text
결측치가 매우 적고 삭제해도 문제 없음
→ dropna 고려

결측치가 많고 삭제하면 데이터 손실이 큼
→ 적절한 대체 고려

0이 실제 의미를 가진 데이터
→ 무작정 fillna(0) 금지
```

---

# 23. 조건 필터링

90도 이상:

```python
danger = df[
    df["온도"] >= 90
]
```

다중 조건:

```python
danger = df[
    (df["온도"] >= 90)
    & (df["진동"] >= 1.5)
]
```

## Python 조건과 차이

일반 Python:

```python
and
or
not
```

Pandas Series 조건:

```text
&   AND
|   OR
~   NOT
```

### 🚨 괄호

```python
(df["온도"] >= 90) & (df["진동"] >= 1.5)
```

조건 하나씩 괄호로 감싸는 습관을 들인다.

---

# 24. `loc` vs `iloc`

## `loc`

이름 기준.

```python
df.loc[
    df["온도"] >= 90,
    ["설비", "온도"]
]
```

뜻:

> 온도가 90 이상인 행에서 설비와 온도 열만 가져와.

## `iloc`

위치 번호 기준.

```python
df.iloc[0, 2]
```

→ 첫 번째 행, 세 번째 열

### 차이

```text
loc
→ 이름

iloc
→ 위치
```

### 🚨 슬라이싱 차이

```python
df.loc[0:3]
```

→ 0,1,2,3

```python
df.iloc[0:3]
```

→ 0,1,2

`loc`는 끝 label 포함, `iloc`는 Python 슬라이싱처럼 끝 위치를 제외한다.

---

# 25. 정렬

```python
df.sort_values(
    "온도",
    ascending=False
)
```

→ 온도가 높은 순.

### `sort_values()` vs `sort_index()`

```text
sort_values()
→ 데이터 값 기준

sort_index()
→ 행 인덱스 기준
```

---

# 26. `value_counts()`

```python
df["가동상태"].value_counts()
```

예:

```text
가동    800
정지    200
```

## `count()`와 차이

```python
df["가동상태"].count()
```

→ 전체 값이 몇 개인지

```python
df["가동상태"].value_counts()
```

→ 종류별로 몇 개인지

---

# 27. `groupby()` ⭐⭐⭐⭐⭐

그룹별 통계를 낸다.

```python
df.groupby("설비")["온도"].mean()
```

예:

```text
M01    75
M02    92
M03    81
```

뜻:

> 설비별 평균 온도를 구해줘.

## `value_counts()` vs `groupby()`

```text
value_counts()
→ 종류별 개수

groupby()
→ 그룹별 계산
```

예:

```python
df["설비"].value_counts()
```

→ M01이 몇 번 등장?

```python
df.groupby("설비")["온도"].mean()
```

→ M01의 평균 온도는?

---

# 28. 현업에서 처음 데이터를 받으면

추천 순서다.

```python
import pandas as pd


# 1. 데이터 불러오기
df = pd.read_csv("data/sensor.csv")


# 2. 기본 구조 확인
print("데이터 크기:", df.shape)
print("컬럼:", df.columns)

df.info()


# 3. 실제 데이터 확인
print(df.head())
print(df.tail())


# 4. 결측치
print(df.isna().sum())


# 5. 중복
print("중복:", df.duplicated().sum())


# 6. 통계
print(df.describe())
```

그리고 분석:

```python
# 위험 온도
danger = df[
    df["온도"] >= 90
]

print(f"위험 데이터: {len(danger):,}건")
```

---

# ⭐ 마지막으로 통계 부분만 다시 압축

| 통계    | 질문              | Pandas          |
| ----- | --------------- | --------------- |
| 평균    | 대체로 얼마?         | `mean()`        |
| 중앙값   | 가운데 값은?         | `median()`      |
| 최솟값   | 가장 작은 값?        | `min()`         |
| 최댓값   | 가장 큰 값?         | `max()`         |
| 범위    | 얼마나 넓게 퍼짐?      | `max-min`       |
| 분산    | 평균에서 얼마나 퍼짐?    | `var()`         |
| 표준편차  | 실제 단위로 얼마나 흔들림? | `std()`         |
| 25%   | 아래쪽 1/4 경계      | `quantile(.25)` |
| 50%   | 중앙값             | `quantile(.50)` |
| 75%   | 위쪽 1/4 경계       | `quantile(.75)` |
| 전체 요약 | 위 통계를 한 번에      | `describe()`    |

특히 설비 데이터에서는 **평균 하나만 보면 부족하다.**

```text
평균
→ 평소 수준

중앙값
→ 이상치에 덜 흔들리는 대표값

최솟값·최댓값
→ 극단적인 상태

표준편차
→ 센서가 얼마나 불안정하게 흔들리는지

사분위수
→ 대부분 데이터가 어느 범위에 있는지
```

를 같이 보는 게 훨씬 중요하다.

그래서 `describe()`를 단순히 **“통계표 출력 함수”**라고 외우기보다는, **“이 데이터가 평소 어느 수준이고, 얼마나 흔들리며, 이상하게 튀는 값이 있는지 첫눈에 검사하는 건강검진”**이라고 이해하면 가장 쉽다.
