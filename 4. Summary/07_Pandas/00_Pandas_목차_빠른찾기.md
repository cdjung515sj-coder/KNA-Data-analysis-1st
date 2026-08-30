# Pandas 학습 노트 - 목차 & 빠른 찾기

> 목적: `pandas` 폴더 안에서 **파일 이름만 보고도 필요한 개념을 바로 찾기** 위한 인덱스입니다.
> 
> 정리 기준: 첨부한 Pandas 교재 10개 PDF의 내용만 바탕으로 재구성했습니다.

---

## 📌 파일 구성 한눈에 보기

| 번호 | 파일명 | 바로 찾는 개념 | 대표 코드/키워드 |
|---|---|---|---|
| 01 | `01_DataFrame_구조_EDA_head_info_describe.md` | 데이터 처음 확인, 구조, 자료형, 기초통계 | `head`, `tail`, `shape`, `columns`, `dtypes`, `info`, `describe` |
| 02 | `02_행열선택_Series_DataFrame_loc_iloc.md` | 열/행 선택, Series vs DataFrame | `df['열']`, `df[['열']]`, `loc`, `iloc` |
| 03 | `03_조건필터링_Boolean_isin_between_sort_copy.md` | 조건으로 행 거르기, 정렬 | `df[조건]`, `&`, `|`, `~`, `isin`, `between`, `sort_values`, `copy` |
| 04 | `04_빈도_그룹집계_value_counts_cut_groupby.md` | 값 개수, 구간화, 그룹별 집계 | `value_counts`, `normalize`, `pd.cut`, `groupby`, `size`, `count` |
| 05 | `05_그룹통계_mean_var_std_median_agg.md` | 평균/분산/표준편차/여러 통계 | `mean`, `var`, `std`, `median`, `agg` |
| 06 | `06_상관관계_corr_상관행렬_통합리포트.md` | 센서끼리 함께 움직이는지 | `corr`, 상관행렬, 상관≠인과 |
| 07 | `07_결측치_확인_NaN_isna_notna_na_values.md` | NaN 찾기, 위장 결측 확인 | `isna`, `notna`, `na_values`, `sum(axis=1)` |
| 08 | `08_결측치_처리_dropna_fillna_ffill_bfill.md` | 결측 제거/대체 | `dropna`, `fillna`, `median`, `mode`, `ffill`, `bfill` |
| 09 | `09_이상치_개념_사분위수_quantile_describe.md` | 이상치 개념, Q1/Q2/Q3 | `quantile`, `describe`, 사분위수 |
| 10 | `10_IQR_이상치처리_중복_duplicated_drop_duplicates.md` | IQR 탐색, 이상치 처리, 중복 제거 | `IQR`, `clip`, `mask`, `duplicated`, `drop_duplicates` |

---

# 🔎 상황별로 어떤 파일을 열면 될까?

| 내가 궁금한 것 | 열 파일 |
|---|---|
| CSV를 받았는데 **뭐부터 확인하지?** | `01_...` |
| 원하는 **열/행만 고르고 싶다** | `02_...` |
| `온도 > 80`, `양품/주의만`, **조건으로 거르고 싶다** | `03_...` |
| 정상/고장이 **각각 몇 개인지** 세고 싶다 | `04_...` |
| 상태별 **평균·표준편차를 비교**하고 싶다 | `05_...` |
| 온도와 진동이 **같이 움직이는지** 알고 싶다 | `06_...` |
| NaN이 **어디에 몇 개 있는지** 찾고 싶다 | `07_...` |
| NaN을 **삭제할지 채울지** 결정하고 싶다 | `08_...` |
| 이상치가 **무엇인지 / 사분위수가 뭔지** 찾고 싶다 | `09_...` |
| IQR로 이상치를 **직접 잡고 처리**하거나 중복을 없애고 싶다 | `10_...` |

---

# 🧭 전체 Pandas 분석 흐름

```text
불러오기
  ↓
구조 확인
head / shape / info / describe
  ↓
행·열 선택
[] / loc / iloc
  ↓
조건 필터링
Boolean Series / isin / between
  ↓
정렬
sort_values
  ↓
집계
value_counts / groupby / agg
  ↓
전처리
결측치 → 이상치 → 중복
  ↓
관계 분석
corr
```

## ⭐ 가장 자주 돌아오는 기본 패턴

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.shape)
df.info()
print(df.describe())
```

```python
# 필터 → 정렬 → 필요한 열 선택
result = (
    df[df["온도"] >= 80]
    .sort_values("온도", ascending=False)
    [["설비명", "온도"]]
)
```

> 기억 문장: **불러오고 → 확인하고 → 거르고 → 줄 세우고 → 골라낸다.**
