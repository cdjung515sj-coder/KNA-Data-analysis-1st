# 실습 6. describe로 이상 신호 찾기
# 평균 / 분위수 / 최대를 읽어 이상 신호 있는 열 찾기

# 12_metro_compressor.csv
# 온도 / 진동의 이상값 존재

import pandas as pd

df_metro_compressor = pd.read_csv("data/12_metro_compressor.csv")
print(df_metro_compressor.shape)
print(df_metro_compressor.head())
print(df_metro_compressor.tail())

df_metro_compressor.info()

# STEP 1 : describe 후 75%와 max 차이 큰 열 찾기
print(df_metro_compressor.describe())


# 1 온도의 평균과 최댓값 차이를 숫자로 적었는가
# 평균 75 대 max 75.0 — 차이를 기록
oil_temp_max = 75.000000
oil_temp_min = 63.181910
temp_diff = oil_temp_max - oil_temp_min  # 11.8181
print(f"온도의 평균과 최댓값 차이 : {temp_diff:.4f}")

# 2 75%와 max 차이가 큰 열을 두 개 이상 찾았는가
# 온도와 진동 — max가 멀리 튄 열 찾기
# 해당 열을 찾아 주석으로 적어줘
# 1. 오일온도 : 75%(68.10℃) 대비 max(75.00℃)가 6.9℃ 높음 (상위 구간에서 열 누적으로 인한 과열 징후)
# 2. 배출압력 : 75%(-0.02) 대비 max(0.60)가 크게 튐 (표준편차 0.047 대비 격차가 매우 큰 돌발 스파이크 이상치)


# 3 모터전류처럼 고른 열과 비교해 차이를 설명
# 모터전류는 75%와 max가 가까움 - 온도와의 차이 설명 서술
# - 75% 지점(68.100000) 대비 최댓값(75.000000)의 차이 = 6.900000
# - 평균(63.18) 및 중앙값(62.90) 대비 상위 구간에서 수치가 급격히 상승함.
