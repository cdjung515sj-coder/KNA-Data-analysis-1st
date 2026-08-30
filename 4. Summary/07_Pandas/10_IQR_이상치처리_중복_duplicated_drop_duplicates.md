# 10. IQR 이상치 처리와 중복 - IQR / clip / mask / duplicated

> 원본 PDF: `16_02_IQR_이상치_처리와_중복_데이터_55_260821_2.pdf`
> 
> 빠른 검색 키워드: **IQR, Q1, Q3, lower, upper, mask, clip, 이상치 제거, 중앙값 대체, duplicated, drop_duplicates, subset, keep, reset_index**

---

## 📌 목차

1. IQR 공식
2. 이상치 하한/상한 계산
3. Boolean mask로 이상치 추출
4. 이상치 개수와 비율
5. 이상치 처리 4가지 판단
6. `clip()` 경계값 보정
7. 이상치를 NaN으로 바꿔 중앙값 대체
8. `duplicated()` 중복 확인
9. `drop_duplicates()` 제거
10. `subset`, `keep`, `reset_index`

---

## 👀 한눈에 배운 코드 정리

```python
# 1. IQR 경계
Q1 = df['temperature'].quantile(0.25)
Q3 = df['temperature'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# 2. 이상치 마스크
mask = (
    (df['temperature'] < lower) |
    (df['temperature'] > upper)
)

print(mask.sum())
print(round(mask.mean() * 100, 1))

# 3. 이상치 제거
clean = df[~mask]

# 4. 경계값 보정
df['temp_clipped'] = df['temperature'].clip(
    lower=lower,
    upper=upper
)

# 5. 이상치를 NaN → 중앙값
masked = df['temperature'].mask(mask)
fixed = masked.fillna(masked.median())

# 6. 중복 확인/제거
print(df.duplicated().sum())
df_unique = df.drop_duplicates()
```

---

# ==================== 개념 1. IQR ====================

IQR(Inter-Quartile Range)은 가운데 50% 데이터가 차지하는 폭입니다.

```text
IQR = Q3 - Q1
```

극단적인 최솟값·최댓값을 직접 쓰지 않고 가운데 절반을 기준으로 하기 때문에 이상치에 덜 흔들리는 기준입니다.

---

# ==================== 개념 2. 이상치 경계 공식 ====================

```text
하한 lower = Q1 - 1.5 × IQR
상한 upper = Q3 + 1.5 × IQR
```

코드:

```python
Q1 = df['temperature'].quantile(0.25)
Q3 = df['temperature'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

교재의 예시에서는:

```text
Q1 = 74
Q3 = 81.5
IQR = 7.5
lower = 62.75
upper = 92.75
```

---

# ==================== 개념 3. Boolean mask로 이상치 찾기 ====================

```python
mask = (
    (df['temperature'] < lower) |
    (df['temperature'] > upper)
)
```

이상치만:

```python
df[mask]
```

정상 범위만:

```python
df[~mask]
```

### ⚠ Pitfall

```python
(df['x'] < lower) | (df['x'] > upper)   # O
```

- 조건마다 괄호
- `or` 대신 `|`
- `and` 대신 `&`

---

# ==================== 개념 4. 이상치 개수와 비율 ====================

```python
print(mask.sum())
print(round(mask.mean() * 100, 1))
```

- `sum()` : 이상치 개수
- `mean() * 100` : 이상치 비율

비율이 너무 높으면 무작정 삭제하기 전에 **경계가 적절한지, 데이터 분포가 특이한지** 다시 확인해야 합니다.

---

# ==================== 개념 5. 이상치 처리 - 무조건 삭제가 아님 ====================

교재의 처리 선택:

```text
1. 보존   → 고장 신호로 의심되면 남김
2. 제거   → 명백한 노이즈 + 비율이 낮을 때
3. 보정   → 행은 살리고 극단값만 경계로 누름
4. 결측 변환 후 대체 → 이상치를 NaN으로 바꾸고 대표값으로 채움
```

### 제거

```python
df_clean = df[~mask]
```

행 전체가 없어지므로 같은 행의 다른 정상 센서값도 같이 사라집니다.

---

# ==================== 개념 6. clip() ====================

```python
df['temp_clipped'] = df['temperature'].clip(
    lower=lower,
    upper=upper
)
```

- 하한보다 작으면 하한으로
- 상한보다 크면 상한으로

행은 보존하지만 `250`과 `300`이 둘 다 같은 상한값으로 눌릴 수 있어 **극단값 크기 정보**는 잃습니다.

---

# ==================== 개념 7. 이상치를 NaN으로 바꾸고 중앙값 대체 ====================

```python
masked = df['temperature'].mask(mask)
print(masked.isna().sum())

med = masked.median()
fixed = masked.fillna(med)
```

이상치에 오염될 수 있는 평균보다 중앙값을 사용해 자연스럽게 대체하는 흐름입니다.

> 함수 `.mask()`와 변수 이름 `mask`를 혼동하지 않게 주의합니다.

---

# ==================== 개념 8. duplicated() ====================

중복 행이 있는지 True/False로 표시합니다.

```python
print(df.duplicated())
print(df[df.duplicated()])
```

중복 개수:

```python
print(df.duplicated().sum())
```

처음 등장한 행은 기본적으로 `False`, 같은 행이 다시 나오면 그 뒤 행이 `True`가 됩니다.

---

# ==================== 개념 9. keep 옵션 ====================

`duplicated()`와 `drop_duplicates()`에서 어떤 기록을 남길지 정합니다.

```text
keep='first'  → 먼저 온 기록을 남김 (기본)
keep='last'   → 마지막 기록을 남김
keep=False    → 겹친 행을 모두 중복으로 표시
```

시간순 갱신 데이터에서는 `last`로 최신 기록을 남기는 방식도 가능합니다.

---

# ==================== 개념 10. drop_duplicates() ====================

```python
df_unique = df.drop_duplicates()

print(len(df), len(df_unique))
print(df_unique.duplicated().sum())
```

제거 전후 행 수와 남은 중복이 0인지 확인합니다.

### 일부 열을 기준으로 중복 정의

```python
df_u = df.drop_duplicates(
    subset=['machine_id', 'cycle'],
    keep='last'
)
```

`subset`은 **무엇이 같으면 같은 기록으로 볼지** 정하는 기준입니다. 기준을 잘못 잡으면 정상 행을 중복으로 오해할 수 있습니다.

---

# ==================== 개념 11. reset_index ====================

행을 제거하면 인덱스가 끊길 수 있습니다.

```python
df_clean = (
    df.drop_duplicates()
      .reset_index(drop=True)
)
```

`drop=True`를 써야 옛 인덱스가 새 열로 들어오지 않습니다.

### 전처리 한 바퀴

```text
이상치 확인/처리
  ↓
중복 확인/처리
  ↓
reset_index(drop=True)
  ↓
처리 전후 통계·행 수·중복 수 검증
```
