# 실습 4. 이상치 제거 후 크기 비교
# 목표
# 경계 밖 행을 제거하고 남은 크기·평균 확인
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

mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)
print(df[mask][["샷", "사이클타임", "상태"]])

# 단계
# · 조건을 뒤집어 정상 범위 행만 남기기
정상 = df[~mask]

# · 원본과 제거 후의 행 수를 비교
print(f"{len(df)}행 → {len(정상)}행")


# · 제거 후 평균을 구해 변화 확인
before_mean = df["사이클타임"].mean()
after_mean = 정상["사이클타임"].mean()

print(f"제거 전 사이클타임 평균: {before_mean:.2f}")
print(f"제거 후 사이클타임 평균: {after_mean:.2f}")

# 예상 결과
# 202행 → 196행, 제거 후 사이클타임 평균 27.28