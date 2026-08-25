# 실습 1. IQR과 이상치 경계 구하기
# 목표
# IQR과 1.5배 규칙으로 이상치 경계를 구하기
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
df.info()

# 단계
# · 사이클타임의 25%·75% 값을 구해 IQR(Q3-Q1) 계산
q1 = df["사이클타임"].quantile(0.25)
q3 = df["사이클타임"].quantile(0.75)

# · Q1에서 IQR의 1.5배를 빼 하한 계산
IQR = q3 - q1
print(round(q1, 2), round(q3, 2), round(IQR, 2))

# · Q3에 IQR의 1.5배를 더해 상한 계산
lower = q1 - 1.5 * IQR
upper = q3 + 1.5 * IQR
print(f"하한 : {lower:.2f}, 상한 : {upper:.2f}")

# 예상 결과
# 사이클타임 IQR 15.12, 하한 -1.9·상한 58.6
