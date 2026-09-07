"""
이상 판정과 라벨 창 설계 예제
- 부하 조건별 정상 기준
- 조건을 고려한 관계 이탈 탐지
- 고장 시점 기준 라벨 창 생성
- 시간 순서 분할 예시
"""

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------
# 1. 조건별 정상 관계 예시: 압연 모터 부하 vs 전류
# ---------------------------------------------------------------------
np.random.seed(0)
n = 60
load = np.linspace(40, 100, n)
current = 1.8 * load + 10 + np.random.normal(0, 3, n)

# 마지막 8개 점은 같은 부하 대비 전류가 과도하게 증가했다고 가정
current[-8:] += 25

df = pd.DataFrame(
    {
        "time": pd.date_range("2026-08-01", periods=n, freq="h"),
        "load": load,
        "current": current,
    }
)

# 정상 학습 구간은 앞부분만 사용
train = df.iloc[:40].copy()

# 단순 선형 정상관계: current ≈ a*load + b
coef = np.polyfit(train["load"], train["current"], 1)
df["expected_current"] = coef[0] * df["load"] + coef[1]
df["residual"] = df["current"] - df["expected_current"]

# 정상 학습구간 잔차의 분포로 기준 생성
resid_std = train.assign(
    expected_current=coef[0] * train["load"] + coef[1]
)["current"].sub(coef[0] * train["load"] + coef[1]).std()

# 3시그마 예시: 실제 현장 기준은 별도 검증 필요
df["relation_anomaly"] = df["residual"].abs() > 3 * resid_std

print("=== 관계 기반 이상 판정 ===")
print(df.tail(12)[["time", "load", "current", "expected_current", "residual", "relation_anomaly"]])


# ---------------------------------------------------------------------
# 2. 고장 사건 기준 라벨 창
# ---------------------------------------------------------------------
failure_time = df["time"].iloc[-1]
lead_start = failure_time - pd.Timedelta(hours=24)   # 24시간 전부터 예측 대상
exclude_start = failure_time - pd.Timedelta(hours=4)  # 마지막 4시간은 너무 임박해 제외

# 기본 정상 0
df["label"] = 0

# 예측 대상 1
predict_mask = (df["time"] >= lead_start) & (df["time"] < exclude_start)
df.loc[predict_mask, "label"] = 1

# 이미 고장이 너무 진행된 제외 구간은 -1로 표현
exclude_mask = df["time"] >= exclude_start
df.loc[exclude_mask, "label"] = -1

print("\n=== 라벨 창 ===")
print(df.tail(30)[["time", "label"]])


# ---------------------------------------------------------------------
# 3. 시계열은 무작위 섞기보다 시간 순서로 분할
# ---------------------------------------------------------------------
usable = df[df["label"] != -1].copy()
split_idx = int(len(usable) * 0.8)
train_set = usable.iloc[:split_idx]
test_set = usable.iloc[split_idx:]

print("\n=== 시간 순서 분할 ===")
print("학습:", train_set["time"].min(), "~", train_set["time"].max())
print("검증:", test_set["time"].min(), "~", test_set["time"].max())

print("\n주의: 평균/표준편차 같은 전처리 통계도 학습 구간에서만 계산해야 라벨 누수를 줄일 수 있습니다.")
