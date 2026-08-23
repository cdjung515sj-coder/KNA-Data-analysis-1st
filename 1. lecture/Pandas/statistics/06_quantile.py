import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
df = df.dropna()
df.info()

print(df.describe())

# quantile 계산을 위해 sort 처리는 필요 없음
# df = df.sort_values("주조압력")

print(df["주조압력"].quantile(0.25))
print(df["주조압력"].quantile(0.50))
print(df["주조압력"].quantile(0.75))

print(df["주조압력"].quantile([0.25, 0.50, 0.75]))
# 0.25     595.0
# 0.50    1037.0
# 0.75    1052.0

# 결과 값을 리스트로 바꿔주는 방법 .tolist() 매서드 사용
print(df["주조압력"].quantile([0.25, 0.50, 0.75]).tolist())  # [595.0, 1037.0, 1052.0]

# .describe() 사용해도 알 수 있음
print(df["주조압력"].describe())
# count     188.000000
# mean      848.696809
# std       244.726145
# min       255.000000
# 25%       595.000000
# 50%      1037.000000
# 75%      1052.000000
# max      1159.000000

# 예지보전(Predictive Maintenance)
# https://share.google/aimode/qTmLVi4aQWBjVKbax

# 데이터로 고장을 미리 알아채 대비하는 일로 그 출발점이자 토대가 데잍로 전처리가 필요하다.
# 결측치, 이상치 처리가 모두 전처리에 속함.

# 좋은 데이터가 좋은 모델을 만듦
# 노이즈 정리하되/ 신호는 보존 할 것.
# 노이즈를 두면 모델이 센서 오류를 학습할 수 있음
# 신호를 다 지우면 모델이 고장 단서를 못 볼 수 있음
# 실제 제조 연구도 사분위수로 찾아 중앙값 대체하는 흐름으로 흘러 가는 중