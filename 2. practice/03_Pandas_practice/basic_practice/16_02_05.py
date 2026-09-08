# 실습 5. 경계값 보정 clipping
# 목표
# 이상치를 버리지 않고 경계값으로 눌러 보정
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
df.info()

q1 = df["사이클타임"].quantile(0.25)
q3 = df["사이클타임"].quantile(0.75)

IQR = q3 - q1
lower = q1 - 1.5 * IQR
upper = q3 + 1.5 * IQR


# 단계
# · clip으로 하한보다 작은 값은 하한으로 올리기
df["사이클타임_보정"] = df["사이클타임"].clip(lower=lower, upper=upper)

# · 상한보다 큰 값은 상한으로 내리기
min_val = df["사이클타임_보정"].min()
max_val = df["사이클타임_보정"].max()
mean_val = df["사이클타임_보정"].mean()

print(f"보정 후 최소 ({min_val:.2f})·최대 ({max_val:.2f}), 평균 ({mean_val:.2f})")

# · 보정 후 최솟값·최댓값·평균 확인
# 보정 후 최소 20.8·최대 20.8, 평균 20.80


# 예상 결과
# 보정 후 최소 20.6·최대 58.6, 평균 28.28
