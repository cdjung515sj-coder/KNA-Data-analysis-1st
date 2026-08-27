# 실습 2. 조건 필터로 이상치 골라내고 개수·비율
# 목표
# 경계 밖 값을 조건으로 골라 개수와 비율 확인

import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
df.info()

q1 = df["사이클타임"].quantile(0.25)
q3 = df["사이클타임"].quantile(0.75)

IQR = q3 - q1
print(round(q1, 2), round(q3, 2), round(IQR, 2))

lower = q1 - 1.5 * IQR
upper = q3 + 1.5 * IQR
print(f"하한 : {lower:.2f}, 상한 : {upper:.2f}")

# 단계
# · 하한보다 작거나 상한보다 큰 조건을 각각 괄호로 감싸 또는로 연결
mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)

# · 조건에 맞는 이상치 행만 골라 확인
print(df[mask][["샷", "사이클타임", "상태"]])

# · sum으로 개수, mean으로 비율 계산
print(mask.sum(), round(mask.mean() * 100, 1))

outlier_count = mask.sum()
outlier_ratio = mask.mean() * 100
print(f"사이클타임 이상치 {outlier_count}건, 비율 {outlier_ratio:.1f}%")

# 예상 결과
# 사이클타임 이상치 6건, 비율 3.0%
