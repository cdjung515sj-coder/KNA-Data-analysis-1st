# Pandas DataFrame 통계 정리

Pandas에서 통계는 다음 흐름으로 보면 이해하기 쉽습니다.

```text
개수 확인
   ↓
중심값
   ↓
퍼짐 정도
   ↓
범위 / 분위수
   ↓
전체 요약
   ↓
결측치 확인
```

---

# 1. 개수 관련 통계

## `count()`

```python
df.count()
```

각 컬럼에서 **NaN을 제외한 실제 값의 개수**를 셉니다.

```python
df["온도"].count()
```

> `count()` = NaN 제외하고 값이 몇 개 있는가?

---

## `size`

```python
df.size
```

**NaN을 포함한 전체 원소 개수**입니다.

DataFrame에서는:

```text
행 개수 × 열 개수
```

입니다.

```text
count() → NaN 제외
size    → NaN 포함
```

---

## `value_counts()`

```python
df["상태"].value_counts()
```

각 값이 **몇 번 등장했는지 값별로** 셉니다.

예:

```text
정상    10
주의     5
고장     2
```

```text
count()        → 총 몇 개?
value_counts() → 각각 몇 개씩?
```

---

# 2. 중심값

## `mean()`

```python
df["온도"].mean()
```

평균입니다.

> 모든 값을 더한 뒤 값의 개수로 나눈 값

NaN은 기본적으로 제외됩니다.

---

## `median()`

```python
df["온도"].median()
```

중앙값입니다.

> 데이터를 크기순으로 정렬했을 때 가운데 위치의 값

평균보다 이상치의 영향을 덜 받습니다.

---

## `mode()`

```python
df["상태"].mode()
```

최빈값입니다.

> 가장 많이 등장한 값

문자열이나 범주형 데이터에서도 자주 사용합니다.

---

# 3. 퍼짐 정도

## `std()`

```python
df["온도"].std()
```

표준편차입니다.

> 데이터가 평균을 중심으로 얼마나 퍼져 있는지 나타냅니다.

```text
표준편차 작음 → 값들이 평균 근처에 모여 있음
표준편차 큼   → 값들이 넓게 퍼져 있음
```

---

## `var()`

```python
df["온도"].var()
```

분산입니다.

```text
분산
 ↓ 제곱근
표준편차
```

둘 다 데이터의 퍼짐 정도를 나타냅니다.

---

# 4. 범위와 분위수

## `min()` / `max()`

```python
df["온도"].min()
df["온도"].max()
```

각각 최솟값과 최댓값을 확인합니다.

---

## `quantile()`

```python
df["온도"].quantile(0.25)
df["온도"].quantile(0.50)
df["온도"].quantile(0.75)
```

```text
0.25 → Q1
0.50 → Q2 = 중앙값
0.75 → Q3
```

IQR 계산에서도 사용합니다.

```python
Q1 = df["온도"].quantile(0.25)
Q3 = df["온도"].quantile(0.75)
IQR = Q3 - Q1
```

---

# 5. `describe()`

```python
df.describe()
```

숫자형 컬럼의 주요 통계를 한 번에 보여줍니다.

| 항목 | 의미 |
|---|---|
| `count` | NaN 제외 개수 |
| `mean` | 평균 |
| `std` | 표준편차 |
| `min` | 최솟값 |
| `25%` | Q1 |
| `50%` | 중앙값 |
| `75%` | Q3 |
| `max` | 최댓값 |

숫자형 전체를 명시하려면:

```python
df.describe(include="number")
```

모든 자료형을 포함하려면:

```python
df.describe(include="all")
```

문자열 컬럼에서는 다음과 같은 값이 나올 수 있습니다.

```text
count  → 값 개수
unique → 서로 다른 값 개수
top    → 가장 많이 등장한 값
freq   → top 값의 등장 횟수
```

---

# 6. 결측치 통계

## `isna().sum()`

```python
df.isna().sum()
```

각 컬럼별 NaN 개수를 확인합니다.

## `notna().sum()`

```python
df.notna().sum()
```

각 컬럼별 실제 값이 있는 개수를 확인합니다.

---

# 7. 실제 분석에서 자주 쓰는 순서

```python
df.head()
df.info()
df.isna().sum()
df.describe(include="number")
df["상태"].value_counts()
```

```text
데이터 확인
   ↓
구조 확인
   ↓
결측치 확인
   ↓
숫자 통계 확인
   ↓
범주형 분포 확인
```

---

# 8. 주의사항 / 많이 헷갈리는 부분

## 1) `count()` vs `size`

```text
count() → NaN 제외
size    → NaN 포함
```

예:

```text
70
80
NaN
90
```

```text
count() = 3
size    = 4
```

---

## 2) `count()` vs `value_counts()`

```text
count()        → 값이 총 몇 개 있는지
value_counts() → 각 값이 몇 번 나왔는지
```

예:

```text
정상
정상
고장
주의
```

`count()`:

```text
4
```

`value_counts()`:

```text
정상 2
고장 1
주의 1
```

---

## 3) `mean()` vs `median()`

```text
mean()   → 평균, 이상치 영향을 많이 받을 수 있음
median() → 중앙값, 이상치 영향을 덜 받음
```

이상치가 큰 데이터에서는 중앙값이 더 적절할 수 있습니다.

---

## 4) `std()` vs `var()`

```text
std() → 표준편차
var() → 분산
```

둘 다 퍼짐 정도를 나타냅니다.

---

## 5) `describe()`는 이상치를 직접 찾아주지 않는다

`describe()`는 `min`, `max`, `25%`, `50%`, `75%` 등을 보여줄 뿐입니다.

실제 이상치 판단에는 다음과 같은 기준이 필요합니다.

```text
IQR
Z-score
3시그마
```

---

## 6) `include="number"` 의미

```text
number → int + float 등 숫자형 전체
int    → 정수형
float  → 실수형
all    → 모든 자료형
```

---

## 7) NaN은 대부분의 통계 계산에서 기본적으로 제외된다

다음 메서드들은 보통 NaN을 제외하고 계산합니다.

```python
mean()
median()
std()
var()
min()
max()
```

NaN 개수 자체를 확인하려면:

```python
df.isna().sum()
```

---

## 8) Series와 DataFrame 결과가 다를 수 있다

```python
df["온도"].mean()
```

→ 숫자 하나

```python
df[["온도", "압력"]].mean()
```

→ 컬럼별 평균이 담긴 Series

---

## 9) 문자열 컬럼에는 평균을 낼 수 없다

`설비`, `상태`, `이름` 같은 문자열 데이터는 평균이나 표준편차 계산이 의미가 없습니다.

대신 다음을 많이 사용합니다.

```python
value_counts()
mode()
describe(include="all")
```

---

## 10) 메서드와 속성을 구분해야 한다

메서드:

```python
df.count()
df.mean()
df.describe()
```

→ `()` 필요

속성:

```python
df.size
df.shape
df.ndim
df.dtypes
```

→ `()` 없음

---

# 9. 한눈에 정리

| 코드 | 의미 |
|---|---|
| `count()` | NaN 제외 값 개수 |
| `size` | NaN 포함 전체 원소 수 |
| `value_counts()` | 값별 등장 횟수 |
| `sum()` | 합계 |
| `mean()` | 평균 |
| `median()` | 중앙값 |
| `mode()` | 최빈값 |
| `std()` | 표준편차 |
| `var()` | 분산 |
| `min()` | 최솟값 |
| `max()` | 최댓값 |
| `quantile()` | 분위수 |
| `describe()` | 통계 요약 |
| `isna().sum()` | 결측치 개수 |
| `notna().sum()` | 값이 있는 개수 |

---

# 10. 핵심 요약

```text
개수
count / size / value_counts

중심
mean / median / mode

퍼짐
std / var

범위
min / max / quantile

요약
describe

결측치
isna / notna
```

특히 초반에는 아래 네 가지 구분을 확실히 잡는 것이 중요합니다.

```text
count() vs size
count() vs value_counts()
mean() vs median()
std() vs var()
```
