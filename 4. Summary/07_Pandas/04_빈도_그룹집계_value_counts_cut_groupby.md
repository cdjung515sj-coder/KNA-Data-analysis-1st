# 04. 빈도와 그룹 집계 - value_counts / pd.cut / groupby

> 원본 PDF: `14_01_빈도와_그룹_집계_47_260814_1(1).pdf`
> 
> 빠른 검색 키워드: **value_counts, normalize, sort=False, dropna=False, pd.cut, groupby, size, count**

---

## 📌 목차

1. 수치형과 범주형 구분
2. `value_counts()` 빈도 집계
3. `normalize=True` 비율
4. `pd.cut()`으로 수치형 구간화
5. `groupby()` 기본 구조
6. 다중 그룹
7. `size()`와 `count()` 차이

---

## 👀 한눈에 배운 코드 정리

```python
# 빈도
print(df['냉각기상태'].value_counts())

# 비율
print(df['result'].value_counts(normalize=True).round(3))

# 결측도 하나의 종류로 세기
print(df['result'].value_counts(dropna=False))

# 수치형을 구간으로 묶기
band = pd.cut(
    df['온도'],
    bins=[0, 40, 50, 200],
    labels=['낮음', '보통', '높음']
)
print(band.value_counts())

# 그룹 평균
print(df.groupby('냉각기상태')['온도'].mean().round(2))

# 다중 그룹
print(
    df.groupby(['냉각기상태', '운전부하'])['온도']
      .mean()
      .round(2)
)
```

---

# ==================== 개념 1. 빈도 집계 ====================

범주형 데이터는 각 종류가 **몇 번 나왔는지** 세는 것만으로도 전체 구성을 빠르게 알 수 있습니다.

```python
df['냉각기상태'].value_counts()
```

기본적으로 **개수가 많은 순서**로 정렬됩니다.

### 비율로 보기

```python
df['result'].value_counts(normalize=True).round(3)
```

예:

```text
정상 0.558
고장 0.442
```

→ 정상 약 55.8%, 고장 약 44.2%

### 옵션

```python
df['등급'].value_counts(sort=False)
df['등급'].value_counts(dropna=False)
```

- `sort=False` : 개수순 자동 정렬을 끔
- `dropna=False` : NaN도 하나의 종류로 셈

---

# ==================== 개념 2. 수치형을 pd.cut으로 구간화 ====================

온도 같은 연속 수치를 그대로 `value_counts()` 하면 값 종류가 너무 많아 해석하기 어렵습니다.

먼저 구간으로 묶습니다.

```python
band = pd.cut(
    df['온도'],
    bins=[0, 40, 50, 200],
    labels=['낮음', '보통', '높음']
)

band.value_counts()
```

### ⚠ Pitfall

```text
경계 4개 → 구간 3개
```

따라서 `labels` 개수는 `bins`보다 1개 적습니다.

---

# ==================== 개념 3. groupby의 핵심 - 분할 → 적용 → 결합 ====================

`groupby()`는 데이터를 그룹으로 나눈 뒤 각 그룹에 계산을 적용하고 결과를 다시 정리합니다.

```text
분할     → 적용       → 결합
groupby    mean()       그룹별 결과표
```

### 기본 문장 읽기

```python
df.groupby('냉각기상태')['온도'].mean()
```

→ `df`를 가지고
→ `냉각기상태`로 나눈 뒤
→ `온도` 열을 골라
→ 평균을 내라

```python
df.groupby('냉각기상태')['온도'].mean().round(2)
```

함수는 상황에 따라 바꿀 수 있습니다.

```python
.mean()
.sum()
.max()
.min()
.count()
```

---

# ==================== 개념 4. 다중 그룹 ====================

그룹 기준이 여러 개면 리스트로 묶습니다.

```python
df.groupby(['냉각기상태', '운전부하'])['온도'].mean().round(2)
```

→ 냉각기상태 안에서 다시 운전부하로 나눈 조합별 평균.

---

# ==================== 개념 5. 그룹 결과 정렬 ====================

그룹 결과에도 정렬을 이어 붙일 수 있습니다.

```python
result = df.groupby('냉각기상태')['온도'].mean()
print(result.sort_values(ascending=False))
```

어느 그룹이 가장 큰지 우선순위를 보기 좋습니다.

---

# ==================== 개념 6. size vs count ====================

둘 다 개수를 세지만 **결측 처리 방식**이 다릅니다.

| 구분 | `size()` | `count()` |
|---|---|---|
| 무엇을 셈 | 전체 행 수 | 결측이 아닌 값 수 |
| NaN 포함 여부 | 포함 | 제외 |
| 용도 | 그룹의 실제 행 개수 | 특정 열의 유효 측정 개수 |

### 핵심 해석

`size`와 `count` 차이가 크다면 그 그룹에 **빠진 값이 많다**는 단서가 됩니다.

```python
df.groupby('냉각기상태').size()
df.groupby('냉각기상태')['온도'].count()
```
