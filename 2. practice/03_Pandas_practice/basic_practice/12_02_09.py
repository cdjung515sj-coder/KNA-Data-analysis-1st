# 실습 9. 첫 탐색 종합

import pandas as pd

df_metro_small = pd.read_csv("data/12_metro_small.csv")

print(df_metro_small.head())
print(f"행, 열 크기 : {df_metro_small.shape}")  # (30, 7)

print(f"열 이름 목록 : {df_metro_small.columns}")
# 열 이름 목록:
#  Index(['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태'], dtype='str')

print("=== 자료형 (dtypes) ===")
print(df_metro_small.dtypes)

print("=== 상세 건강검진 (info) ===")
df_metro_small.info()


print("=== 요약 통계량 (describe) ===")
print(df_metro_small.describe())
# 오일온도 - 평균 54.675862 / min 50.100000 / max 59.600000
# 모터전류 - 평균 1.383000 /min 0.030000 / mid 0.030000 / max 6.070000
# 압력 센서: 압축압력(평균 8.895333)과 저장압력(8.896000)이 상응하며 안정적인 작동 수치를 보임

print("=== 열별 결측치 개수 (isnull) ===")
print(df_metro_small.isnull().sum())  # 오일온도    1  "결측 발생 !!"
# 센서 수집 누락: 오일온도 센서에서 3번 행(2020-02-27 09:07:27) 수치가 누락되어 NaN 발생함
