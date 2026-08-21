# 실습 2. SECOM 첫 탐색 -> 사출성형_공정.csv
# head·shape·info·describe로 결측 분위기 파악
# 처음 받은 데이터의 구조와 결측 분위기 파악
import pandas as pd

df_imp = pd.read_csv("data/15_01_Injection_Molding_process.csv", encoding="utf-8")

print(df_imp.head())
print(df_imp.shape)  # (250, 22)
df_imp.info()
# RangeIndex: 250 entries, 0 to 249
# Data columns (total 22 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    250 non-null    str
#  1   불량여부    250 non-null    int64
#  2   사이클시간   250 non-null    float64
#  3   성형사이클   250 non-null    float64
#  4   배럴온도1   250 non-null    float64
#  5   배럴온도2   250 non-null    float64
#  6   배럴온도3   250 non-null    float64
#  7   배럴온도4   250 non-null    float64
#  8   호퍼온도    250 non-null    float64
#  9   최대사출속도  250 non-null    float64
#  10  사출압력    249 non-null    float64
#  11  스크루위치   247 non-null    float64
#  12  전환위치    245 non-null    float64
#  13  계량시간    241 non-null    float64
#  14  계량시작점   241 non-null    float64
#  15  최대사출압   216 non-null    float64
#  16  전환압력    216 non-null    float64
#  17  계량시작위치  216 non-null    float64
#  18  스크루속도   190 non-null    float64
#  19  최소쿠션    182 non-null    float64
#  20  계량종료점   141 non-null    float64
#  21  감압시간    141 non-null    float64
# dtypes: float64(20), int64(1), str(1)
# memory usage: 43.1 KB

print(df_imp.describe())
#             불량여부       사이클시간       성형사이클       배럴온도1       배럴온도2  ...      계량시작위치       스크루속도        최소쿠션 계량종료점        감압시간
# count  250.00000  250.000000  250.000000  250.000000  250.000000  ...  216.000000  190.000000  182.000000  141.000000  141.000000
# mean     0.13200   16.638320   16.651760  209.998800  200.057200  ...   10.990463   46.894632    6.503956   63.112128    0.322411
# std      0.33917    0.020874    0.024067    0.057723    0.129752  ...    0.083648    2.084040    0.073573    0.004107    0.004293
# min      0.00000   16.540000   16.520000  209.900000  199.900000  ...   10.510000   35.380000    6.020000   63.110000    0.320000
# 25%      0.00000   16.620000   16.640000  210.000000  200.000000  ...   10.957500   46.450000    6.470000   63.110000    0.320000
# 50%      0.00000   16.640000   16.660000  210.000000  200.100000  ...   11.000000   47.415000    6.510000   63.110000    0.320000
# 75%      0.00000   16.660000   16.660000  210.000000  200.100000  ...   11.040000   48.040000    6.550000   63.110000    0.320000
# max      1.00000   16.680000   16.710000  210.200000  200.800000  ...   11.150000   49.490000    6.650000   63.120000    0.330000

# [8 rows x 21 columns]

# · read_csv로 불러와 head와 shape로 크기 확인
# · info로 컬럼별 채워진 값 개수 훑기
# · describe의 count로 결측 있는 컬럼 짐작

# 예상 결과
# 250행 22열, 뒤쪽 센서 컬럼일수록 채워진 수 감소
