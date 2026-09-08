import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv("data/05-02_라벨설계_센서데이터.csv")

# timestamp를 날짜/시간 형식으로 변환
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 그래프 그리기
plt.figure(figsize=(12, 5))

plt.plot(
    df["timestamp"],
    df["vibration_rms"]
)

plt.xlabel("timestamp")
plt.ylabel("vibration_rms")
plt.title("MTR01 Vibration RMS")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

print("\n----\n")

import pandas as pd
import matplotlib.pyplot as plt

# 센서 데이터 불러오기
df = pd.read_csv("data/05-02_라벨설계_센서데이터.csv")

# 시간 형식 변환
df["timestamp"] = pd.to_datetime(df["timestamp"])

# R003 고장 발견 시각
failure_time = pd.to_datetime("2026-07-15 11:20:00")

# 그래프
plt.figure(figsize=(12, 5))

plt.plot(
    df["timestamp"],
    df["vibration_rms"],
    label="vibration_rms"
)

# 고장 시각 표시
plt.axvline(
    failure_time,
    linestyle="--",
    label="R003 failure"
)

plt.xlabel("timestamp")
plt.ylabel("vibration_rms")
plt.title("MTR01 Vibration RMS")

plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()