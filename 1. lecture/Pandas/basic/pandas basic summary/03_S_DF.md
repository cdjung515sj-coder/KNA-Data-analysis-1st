아래 내용 그대로 `.md` 파일에 붙여넣으면 돼.

````md
# Pandas Series와 DataFrame 차이 및 주의사항

## 1. Series란?

`Series`는 Pandas의 **1차원 자료구조**이다.

쉽게 말하면:

> 하나의 열처럼 생긴 데이터

```python
import pandas as pd

s = pd.Series([70, 80, 90])

print(s)
````

결과:

```text
0    70
1    80
2    90
dtype: int64
```

구조:

```text
index    value
0        70
1        80
2        90
```

즉, Series는

```text
index + value
```

로 이루어져 있다.

---

## 2. DataFrame이란?

`DataFrame`은 Pandas의 **2차원 자료구조**이다.

쉽게 말하면:

> 행과 열로 이루어진 엑셀 같은 표

```python
df = pd.DataFrame({
    "설비": ["A", "B", "C"],
    "온도": [70, 80, 90],
    "압력": [10, 15, 20]
})

print(df)
```

결과:

```text
   설비  온도  압력
0   A  70  10
1   B  80  15
2   C  90  20
```

구조:

```text
          columns
       설비  온도  압력
index
0       A   70   10
1       B   80   15
2       C   90   20
```

즉, DataFrame은

```text
index + columns + values
```

로 이루어져 있다.

---

# 3. Series와 DataFrame 차이

| 구분   | Series        | DataFrame        |
| ---- | ------------- | ---------------- |
| 차원   | 1차원           | 2차원              |
| 모양   | 한 줄의 데이터      | 표 형태             |
| 행    | 있음            | 있음               |
| 열    | 하나의 데이터 묶음    | 여러 열             |
| 대표 예 | 온도 열 하나       | 전체 데이터           |
| 생성   | `pd.Series()` | `pd.DataFrame()` |

쉽게 기억하면:

```text
Series
→ 열 하나

DataFrame
→ 여러 열이 모인 표
```

---

# 4. DataFrame의 한 열을 선택하면 Series

DataFrame:

```python
df
```

```text
   설비  온도  압력
0   A  70  10
1   B  80  15
2   C  90  20
```

여기에서:

```python
df["온도"]
```

결과:

```text
0    70
1    80
2    90
Name: 온도
dtype: int64
```

결과 자료형은 `Series`이다.

```text
DataFrame
    ↓
열 하나 선택
    ↓
Series
```

---

# 5. 가장 중요한 차이

## 열 하나 선택

```python
df["온도"]
```

결과:

```text
Series
```

---

## 열 하나를 리스트 형태로 선택

```python
df[["온도"]]
```

결과:

```text
DataFrame
```

즉:

| 코드                 | 결과        |
| ------------------ | --------- |
| `df["온도"]`         | Series    |
| `df[["온도"]]`       | DataFrame |
| `df[["온도", "압력"]]` | DataFrame |

### 중요

```python
df["온도"]
```

와

```python
df[["온도"]]
```

는 모양이 비슷하지만 **자료형이 다르다.**

---

# 6. Series 속성

```python
s.index
```

→ 인덱스 확인

```python
s.values
```

→ 실제 값 확인

```python
s.dtype
```

→ 데이터 타입 확인

```python
s.size
```

→ 원소 개수

```python
s.shape
```

→ Series의 크기

---

# 7. DataFrame 속성

```python
df.index
```

→ 행 index 확인

```python
df.columns
```

→ 열 이름 확인

```python
df.values
```

→ 실제 값 확인

```python
df.shape
```

→ `(행 개수, 열 개수)`

```python
df.size
```

→ 전체 원소 개수

```python
df.dtypes
```

→ 각 열의 자료형 확인

---

# 8. 주의사항 ① 속성과 메서드 구분

속성은 객체가 가지고 있는 **정보**이다.

```python
df.shape
df.columns
s.size
s.dtype
```

메서드는 객체가 수행하는 **기능**이다.

```python
df.head()
df.info()
df.sort_values()
s.mean()
s.sum()
```

쉽게 구분하면:

```text
속성
→ 객체.속성
→ () 없음

메서드
→ 객체.메서드()
→ () 있음
```

예:

```python
df.shape      # O
df.shape()    # X
```

```python
s.size        # O
s.size()      # X
```

---

# 9. 주의사항 ② `column`과 `columns`

DataFrame의 열 이름 전체를 확인할 때는:

```python
df.columns
```

을 사용한다.

```python
df.column
```

이라는 기본 속성은 없다.

따라서:

```python
df.columns     # O
df.columns()   # X
df.column      # X
```

---

# 10. 주의사항 ③ `loc`과 `iloc`

## `loc`

index 이름과 column 이름을 사용한다.

```python
df.loc[0, "온도"]
```

또는 조건을 사용할 수 있다.

```python
df.loc[df["온도"] >= 80, ["설비", "온도"]]
```

---

## `iloc`

위치 번호를 사용한다.

```python
df.iloc[0, 1]
```

뜻:

```text
0번째 행
1번째 열
```

쉽게 기억:

```text
loc
→ 이름 / 조건

iloc
→ 위치 번호
```

---

# 11. 주의사항 ④ Series에 조건을 걸면 Boolean Series

```python
df["온도"] >= 80
```

먼저:

```python
df["온도"]
```

는 Series이다.

여기에 조건을 적용하면:

```text
0    False
1     True
2     True
```

처럼 `True / False`로 이루어진 Series가 만들어진다.

이것을 **Boolean Series**라고 한다.

전체 흐름:

```text
df["온도"]
    ↓
Series
    ↓
>= 80
    ↓
Boolean Series
```

---

# 12. Boolean Series로 DataFrame 필터링

```python
df[df["온도"] >= 80]
```

뜻:

> 온도가 80 이상인 행만 가져와라.

구조:

```text
df["온도"]
    ↓
Series

df["온도"] >= 80
    ↓
Boolean Series

df[Boolean Series]
    ↓
True인 행만 선택
```

---

# 13. 주의사항 ⑤ Pandas 다중 조건

일반 Python에서는:

```python
and
or
not
```

을 사용하지만,

Pandas Series 조건에서는 주로:

```text
&  → AND
|  → OR
~  → NOT
```

을 사용한다.

예:

```python
df[
    (df["온도"] >= 80) &
    (df["압력"] >= 15)
]
```

### 중요

각 조건에 괄호를 붙인다.

```python
(df["온도"] >= 80)
```

```python
(df["압력"] >= 15)
```

잘못된 형태:

```python
df["온도"] >= 80 & df["압력"] >= 15
```

권장 형태:

```python
(df["온도"] >= 80) & (df["압력"] >= 15)
```

---

# 14. 주의사항 ⑥ `shape`와 `size`

DataFrame이 다음과 같다고 하자.

```text
3행 × 2열
```

`shape`:

```python
df.shape
```

결과:

```text
(3, 2)
```

즉:

```text
(행 개수, 열 개수)
```

`size`:

```python
df.size
```

결과:

```text
6
```

왜냐하면:

```text
3행 × 2열 = 6개
```

이기 때문이다.

따라서:

```text
shape
→ 행과 열의 개수

size
→ 전체 원소의 개수
```

---

# 15. Series와 DataFrame 관계

Series와 DataFrame은 서로 완전히 별개의 개념이라기보다 연결되어 있다.

```text
DataFrame
│
├─ 설비 Series
├─ 온도 Series
└─ 압력 Series
```

즉:

> DataFrame은 여러 Series가 모여 있는 2차원 표라고 이해하면 쉽다.

---

# 16. 최종 핵심 정리

```text
Series
→ 1차원
→ index + value
→ 열 하나

DataFrame
→ 2차원
→ index + columns + values
→ 여러 행과 여러 열을 가진 표
```

가장 중요한 코드:

```python
df["온도"]
# Series
```

```python
df[["온도"]]
# DataFrame
```

```python
df[["온도", "압력"]]
# DataFrame
```

```python
df["온도"] >= 80
# Boolean Series
```

```python
df[df["온도"] >= 80]
# 조건을 만족하는 DataFrame
```

---

# 17. 한눈에 보는 흐름

```text
DataFrame
    ↓
열 하나 선택
    ↓
Series
    ↓
조건 적용
    ↓
Boolean Series
    ↓
DataFrame에 적용
    ↓
조건에 맞는 행 필터링
```

## 한 문장 암기

> **Series는 한 열을 다루는 1차원 자료구조이고, DataFrame은 여러 Series가 모인 2차원 표 형태의 자료구조이다.**

```
```
