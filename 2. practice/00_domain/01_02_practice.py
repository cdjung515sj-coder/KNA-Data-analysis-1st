import pandas as pd

# 1. csv에서 detetime 데이터 불러오기 (to_datetime() 메서드 이용)
df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv")
print(df.shape)  # (720, 6)

# timestamp 열 데이터타입 확인
print(f"timestamp의 데이터 타입 : {df["timestamp"].dtypes}")  # str

df["timestamp"] = pd.to_datetime(df["timestamp"])
print(f"timestamp의 데이터 타입 변경 : {df['timestamp'].dtypes}")  # datetime64[us]

# 2. read_csv() 옵션값 이용
df = pd.read_csv(
    "data/01-02_원료_전처리와_제선_제선조업.csv", parse_dates=["timestamp"]
)
print(df.shape)  # (720, 6)
print(f"timestamp의 데이터 타입 변경 : {df['timestamp'].dtypes}")  # datetime64[us]


# timestamp의 시간 간격
gaps = df["timestamp"].diff().value_counts()  # .diff() 앞,뒤 행 차이를 알려줌
print(gaps)
# timestamp
# 0 days 00:01:00    719  # 720행의 데어 중에서 서로 인접한 719개의 시간 간격이 전부 0 days 00:01:00 이다
# Name: count, dtype: int64

# 송풍량, 송풍압, 송풍기 진동
print(
    df[["blast_flow_nm3min", "blast_pressure_kpa", "blower_vib_mms"]]
    .describe()
    .round(2)
)
"""

       blast_flow_nm3min  blast_pressure_kpa  blower_vib_mms
count             720.00              720.00          720.00
mean             5088.25              388.75            3.40
std               159.64               12.97            0.08
min              4681.80              372.80            3.17
25%              4977.50              379.40            3.34
50%              5180.75              381.70            3.40
75%              5202.52              398.32            3.45
max              5258.20              421.40            3.63

"""

# ====================== 이동 평균 ======================

# 이동 평균 : N 분 간의 흔들림을 확인하여 송풍량의 장기적인 방향을 보는 지표
# 통기성이 나빠지면 공기가 원료층을 통과하기 어려워져서 실제 들어가는 풍량이 감소할 수 있음

# blast_flow_nm3min 컬럼을 기준으로 15개씩 이동평균 계산
# window=15 → 현재 행을 포함하여 최근 15개의 값의 평균을 구함
df["flow_ma"] = df["blast_flow_nm3min"].rolling(window=15).mean()

# 처음 3개의 값 확인
print(df["flow_ma"].head(3).tolist())
# [nan, nan, nan]
# → 평균을 계산하려면 15개의 데이터가 필요하지만,
#   초기에는 데이터 개수가 부족하므로 NaN으로 표시됨

# 처음 16개의 값 확인
print(df["flow_ma"].head(16).tolist())
# [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
#  nan, nan, nan, nan, 5201.473333333333, 5200.413333333333]

# 인덱스 0~13까지는 15개의 데이터가 모이지 않았기 때문에 NaN
# 인덱스 14에서는 인덱스 0~14까지 총 15개의 데이터가 모이므로
# 처음으로 15개 데이터의 이동평균을 계산할 수 있음

# 즉, window=15일 경우 첫 이동평균 값은 인덱스 14부터 생성됨
# (파이썬 인덱스는 0부터 시작하기 때문)

print(round(df["flow_ma"].iloc[14], 1), round(df["flow_ma"].iloc[400], 1))
# 5201.5 5200.8  ==> 차이가 크지 않음. 이 값으로는 통기성 악화가 보이지 않음
# 현재 csv에서는 송풍량으로 통기성 악화를 확인할 수 없음.


# ====================== 이동 표준편차 ======================

# ====================== 이동 표준편차 ======================

# top_pressure_kpa를 기준으로 30개 구간의 이동 표준편차 계산
df["top_sd"] = df["top_pressure_kpa"].rolling(window=30).std()

# 200번째와 560번째 위치의 이동 표준편차 확인
print(round(df["top_sd"].iloc[200], 2), round(df["top_sd"].iloc[560], 2))
# 2.64 4.28

# 동일한 노정압 계측 데이터에서 뒤쪽 구간의 표준편차가 더 크게 나타남.
# → 시간이 지날수록 압력 변동(흔들림)이 증가함을 알 수 있음.