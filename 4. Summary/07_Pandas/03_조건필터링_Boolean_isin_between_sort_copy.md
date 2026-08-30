# 03. 조건 필터링과 정렬 - Boolean / isin / between / sort_values / copy

> 원본 PDF: `13_02_조건_필터링과_정렬_45_260813_2.pdf`
> 
> 빠른 검색 키워드: **Boolean Series, 필터링, &, |, ~, isin, between, str.contains, sort_values, ascending, copy, SettingWithCopyWarning**

---

## 📌 목차

1. Boolean Series 만들기
2. `df[조건]`으로 행 추출
3. 복합 조건 `&`, `|`, `~`
4. `isin`, `between`, `str.contains`
5. `sort_values` 정렬
6. `copy()`와 SettingWithCopyWarning
7. 분석 워크플로우 5단계

---

## 👀 한눈에 배운 코드 정리

```python
# Boolean Series
cond = df['비스킷두께'] >= 13
print(cond.sum())

# 필터링
danger = df[df['비스킷두께'] >= 13]

# AND / OR
both = df[(df['비스킷두께'] >= 13) & (df['사이클타임'] >= 25)]
either = df[(df['비스킷두께'] >= 13) | (df['사이클타임'] >= 25)]

# NOT
not_bad = df[~(df['품질등급'] == '불량')]

# 목록 / 범위 / 문자열
pick = df[df['품질등급'].isin(['양품', '주의'])]
normal = df[df['비스킷두께'].between(70, 80)]
text = df[df['샷'].str.contains('L')]

# 정렬
sorted_df = df.sort_values('사이클타임', ascending=False)
top5 = df.sort_values('비스킷두께', ascending=False).head(5)
```

---

# ==================== 개념 1. Boolean Series ====================

```python
조건 = df['비스킷두께'] >= 13
print(조건.head())
print(조건.sum())
```

열 전체에 비교를 하면 각 행마다 `True/False`가 생깁니다. 이것이 **Boolean Series**입니다.

```text
True
False
True
...
```

`True`는 계산할 때 1처럼 취급되므로 `sum()`으로 조건 만족 개수를 셀 수 있습니다.

---

# ==================== 개념 2. df[조건] ====================

```python
df[df['비스킷두께'] >= 13]
```

안쪽:

```python
df['비스킷두께'] >= 13
```

→ True/False 목록 생성

바깥:

```python
df[ ... ]
```

→ True인 행만 통과

> 필터링은 **체로 거르기**라고 생각하면 쉽습니다.

---

# ==================== 개념 3. 복합 조건 ====================

### AND

```python
both = df[
    (df['비스킷두께'] >= 13) &
    (df['사이클타임'] >= 25)
]
```

두 조건을 **모두 만족**.

### OR

```python
either = df[
    (df['비스킷두께'] >= 13) |
    (df['사이클타임'] >= 25)
]
```

둘 중 **하나라도 만족**.

### NOT

```python
not_bad = df[~(df['품질등급'] == '불량')]
```

`~`는 True/False를 뒤집습니다.

### ⚠ Pitfall

Pandas Boolean Series에서는:

```python
&   # and 역할
|   # or 역할
~   # not 역할
```

을 사용합니다.

그리고 **각 조건을 괄호로 감싸는 습관**이 중요합니다.

---

# ==================== 개념 4. isin / between / str.contains ====================

## `isin()` - 여러 값 중 하나인지

```python
df[df['품질등급'].isin(['양품', '주의'])]
```

여러 번 `|`를 쓰는 것보다 간결합니다.

반대로 목록에 없는 값:

```python
df[~df['품질등급'].isin(['불량'])]
```

## `between()` - 범위 안인지

```python
df[df['비스킷두께'].between(70, 80)]
```

양쪽 경계를 모두 포함합니다.

범위 밖:

```python
df[~df['비스킷두께'].between(70, 80)]
```

## `str.contains()` - 글자 포함

```python
df[df['샷'].str.contains('L')]
```

글자 열에서 특정 문자열이 포함됐는지 검사합니다.

---

# ==================== 개념 5. sort_values ====================

기본은 오름차순입니다.

```python
df.sort_values('비스킷두께')
```

내림차순:

```python
df.sort_values('사이클타임', ascending=False)
```

다중 기준:

```python
df.sort_values(['품질등급', '사이클타임'])
```

열별 정렬 방향을 다르게:

```python
df.sort_values(
    ['품질등급', '사이클타임'],
    ascending=[True, False]
)
```

### 상위 N개

```python
df.sort_values('비스킷두께', ascending=False).head(5)
```

> `sort_values()`는 행을 통째로 같이 이동시키기 때문에 다른 열과 값이 어긋나지 않습니다.

---

# ==================== 개념 6. copy() ====================

필터링한 결과를 따로 수정할 계획이면 독립 복사본을 만드는 것이 안전합니다.

```python
위험설비 = df[df['비스킷두께'] >= 13].copy()
```

### 규칙

- 결과를 **보기만** 한다 → 꼭 `copy()`할 필요 없음
- 필터링 결과에 새 열 추가/수정한다 → `.copy()` 권장
- 원본 자체를 수정한다 → `.loc`으로 명확하게 지정

### SettingWithCopyWarning

원본 일부를 보고 있는지 복사본인지 Pandas가 확신하지 못할 때 뜨는 경고입니다.

해결 방향:

```text
따로 수정 → .copy()
원본 수정 → .loc
```

---

# ==================== 개념 7. 분석 워크플로우 5단계 ====================

```text
1. 불러오기
2. 확인
3. 필터링
4. 정렬
5. 선택
```

```python
import pandas as pd

df = pd.read_csv('data.csv')       # 1. 불러오기
print(df.head())                    # 2. 확인

danger = df[df['온도'] >= 80]      # 3. 필터링
danger = danger.sort_values(        # 4. 정렬
    '온도', ascending=False
)
result = danger[['설비명', '온도']]  # 5. 선택
```

> 기억 문장: **불러오고, 확인하고, 거르고, 줄 세우고, 골라낸다.**
