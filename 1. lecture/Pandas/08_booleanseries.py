# boolean Series
import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

# <class 'pandas.DataFrame'>
# RangeIndex: 30 entries, 0 to 29
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       30 non-null     int64
#  1   실린더압력   30 non-null     float64
#  2   주조압력    30 non-null     float64
#  3   사이클타임   30 non-null     float64
#  4   비스킷두께   30 non-null     float64
#  5   형체력     30 non-null     float64
#  6   품질등급    30 non-null     str
# dtypes: float64(5), int64(1), str(1)
# memory usage: 1.8 KB


print(df.describe())

#                샷       실린더압력         주조압력       사이클타임      비스킷두께         형체력
# count  30.000000   30.000000    30.000000   30.000000  30.000000   30.000000
# mean   15.500000  219.666667   971.466667   46.113333  11.633333  267.800000
# std     8.803408   27.096677   179.023546  115.292640   4.491243   35.905431
# min     1.000000  108.000000   522.000000   20.600000   2.000000  222.000000
# 25%     8.250000  215.000000  1037.000000   20.800000  11.000000  254.250000
# 50%    15.500000  217.000000  1040.500000   20.900000  11.000000  257.000000
# 75%    22.750000  218.000000  1052.750000   21.375000  12.000000  258.000000
# max    30.000000  265.000000  1137.000000  652.300000  21.000000  359.000000


s = df["비스킷두께"]  # Serise
s.info()

# <class 'pandas.Series'>
# RangeIndex: 30 entries, 0 to 29
# Series name: 비스킷두께
# Non-Null Count  Dtype
# --------------  -----
# 30 non-null     float64
# dtypes: float64(1)
# memory usage: 372.0 bytes

print("\n앞----------------------------\n")
print(s.head())

# 0    10.0
# 1    11.0
# 2    21.0
# 3    11.0
# 4    14.0
# Name: 비스킷두께, dtype: float64

print("\n뒤----------------------------\n")
print(s.tail())

# 25    11.0
# 26    12.0
# 27    19.0
# 28    11.0
# 29     2.0
# Name: 비스킷두께, dtype: float64

# 비스킷두께 숫자들만 담긴 Series에 13 이상인지 따져보는 연산을 시킨다면?
# Boolean Serise 생성 : True 아니면 False만 담김

s_boolean = s >= 13
print(s_boolean.head())
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# Name: 비스킷두께, dtype: bool

# 위에서 생성된 Boolean Serise에서 True값들이 모두 몇개일까요?
# = 최초 CSV 파일에서 "비스킷두께" 컬럼의 값들중에 13 이상인 경우는 몇개인가?

# Boolean  Serise의 sum() 같은 통계를 낸다면
# True = 1, False = 0 처리
print(s_boolean.sum()) # 6 (True 개수)

# TMI
# SQL 앎? 
# 문법을 이식으래서 파이선안의 