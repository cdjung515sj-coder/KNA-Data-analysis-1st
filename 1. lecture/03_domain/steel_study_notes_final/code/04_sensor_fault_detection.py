"""
센서 고장 후보 탐지 예제
- 고착(stuck)
- 스파이크(spike)
- 드리프트(drift)

주의:
이 코드는 '후보 구간을 찾는 1차 탐색'입니다.
최종 판정은 가동 신호, 동종 센서, 정비 기록과 함께 해야 합니다.
"""

import numpy as np
import pandas as pd


n = 30
time = pd.date_range("2026-09-01", periods=n, freq="min")

# 기준 센서
sensor_ref = 80 + np.sin(np.arange(n) / 4) * 0.5

# 테스트 센서: 후반부 드리프트 + 일부 고착 + 한 점 스파이크
sensor_test = sensor_ref.copy()
sensor_test[10:15] = sensor_test[10]       # 고착 후보
sensor_test[18] = 120                      # 스파이크 후보
sensor_test[20:] += np.linspace(0, 4, 10)  # 드리프트 후보

run_flag = np.ones(n, dtype=int)  # 설비 가동 중이라고 가정

df = pd.DataFrame(
    {
        "time": time,
        "run_flag": run_flag,
        "TEMP_A": sensor_ref,
        "TEMP_B": sensor_test,
    }
)

# ---------------------------------------------------------------------
# 1. 고착 후보: 가동 중인데 값이 연속으로 동일
# ---------------------------------------------------------------------
df["same_as_prev"] = df["TEMP_B"].eq(df["TEMP_B"].shift())

# 연속 동일값 길이 계산
group_id = (~df["same_as_prev"]).cumsum()
df["same_run_length"] = df.groupby(group_id)["same_as_prev"].transform("size")

df["stuck_candidate"] = (
    (df["run_flag"] == 1)
    & df["same_as_prev"]
    & (df["same_run_length"] >= 3)
)

# ---------------------------------------------------------------------
# 2. 스파이크 후보: 한 시점 변화량이 매우 큼
# ---------------------------------------------------------------------
diff = df["TEMP_B"].diff().abs()
threshold = diff.median() + 8 * diff.mad() if hasattr(diff, "mad") else diff.median() + 8 * (diff - diff.median()).abs().median()
# pandas 버전에 따라 Series.mad가 없을 수 있으므로 위처럼 처리

df["spike_candidate"] = diff > threshold

# ---------------------------------------------------------------------
# 3. 드리프트 후보: 동종 센서 차이의 이동평균이 점진적으로 증가
# ---------------------------------------------------------------------
df["sensor_gap"] = df["TEMP_B"] - df["TEMP_A"]
df["gap_ma5"] = df["sensor_gap"].rolling(5, min_periods=3).mean()
df["drift_candidate"] = df["gap_ma5"].abs() > 1.5

print(df[[
    "time", "TEMP_A", "TEMP_B", "sensor_gap",
    "stuck_candidate", "spike_candidate", "drift_candidate"
]])

print("\n=== 후보 개수 ===")
print("고착 후보:", int(df["stuck_candidate"].sum()))
print("스파이크 후보:", int(df["spike_candidate"].sum()))
print("드리프트 후보:", int(df["drift_candidate"].sum()))

print("\n최종 판단 전에 반드시 확인할 것:")
print("1) 다른 센서도 같은 시각에 반응했는가")
print("2) 물리적으로 가능한 변화인가")
print("3) 교정/교체/통신장애/설비정지 기록이 있는가")
