# 실습 2. 한 컬럼의 최소·최대·범위
# 목표
# 한 컬럼의 최솟값·최댓값·범위를 구해 퍼짐 확인
import pandas as pd

df_diecasting = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
df_diecasting.info()
print(df_diecasting.head(3))
#    샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 0  1  214.0  1037.0   20.7   10.0  258.0   0
# 1  2  217.0  1052.0   20.7   11.0  257.0   0
# 2  3  214.0  1037.0   20.8   11.0  254.0   0

# 단계
# · 실린더압력 열의 최솟값 구하기
min_temp = df_diecasting["실린더압력"].min()
print(min_temp)

# · 실린더압력 열의 최댓값 구하기
max_temp = df_diecasting["실린더압력"].max()
print(max_temp)

# · 최댓값에서 최솟값을 빼 범위 계산
range = max_temp - min_temp
print(range)

# 예상 결과
# 실린더압력 최소 108·최대 265·범위 157
