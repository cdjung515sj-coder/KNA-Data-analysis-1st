"""
측정의 3요소 중 '얼마나 자주'와 '최소 변화폭' 확인 예제
- 실제 저장 간격 확인
- 같은 값 반복 횟수 확인
- 행간 데이터 변화 중 최소 변화폭 계산

강의 개념 연결:
02-01 설비 4대 분류 - 측정의 3요소 / 측정값의 한계
"""

import pandas as pd


# 철강 설비 샘플 데이터
# 실제 파일 사용 시: df = pd.read_csv("data.csv", parse_dates=["time"])
df = pd.DataFrame(
    {
        "time": pd.date_range("2026-09-01 00:00:00", periods=10, freq="60s"),
        "MTR01_VIB_RMS_H": [1.7, 1.8, 1.8, 1.9, 2.0, 2.0, 2.1, 2.2, 2.2, 2.4],
        "MTR01_CURRENT": [62.0, 62.5, 62.5, 63.0, 63.5, 64.0, 64.0, 64.5, 65.0, 66.0],
        "FUR01_TEMP_Z1": [1180.0, 1180.5, 1180.5, 1181.0, 1181.5, 1182.0, 1182.0, 1182.5, 1183.0, 1183.5],
    }
)

sensor_cols = ["MTR01_VIB_RMS_H", "MTR01_CURRENT", "FUR01_TEMP_Z1"]

# 1) 실제 저장 간격
interval = df["time"].diff().dt.total_seconds()
print("=== 실제 저장 간격(초) ===")
print(interval.value_counts(dropna=True).sort_index())

# 2) 연속된 동일값 개수 확인
print("\n=== 연속 동일값이 발생한 횟수 ===")
for col in sensor_cols:
    same_as_prev = df[col].eq(df[col].shift())
    print(f"{col}: {int(same_as_prev.sum())}회")

# 3) 값이 실제로 변한 경우만 대상으로 최소 변화폭 계산
print("\n=== 최소 변화폭 ===")
for col in sensor_cols:
    diff = df[col].diff().abs()
    diff = diff[diff > 0]
    min_change = diff.min()
    print(f"{col}: {round(min_change, 1)}")

# 주의:
# 이 값은 '파일에서 관찰된 최소 변화폭'입니다.
# 센서의 공식 분해능이라고 단정하려면 센서 사양/전처리/반올림 규칙 확인이 필요합니다.
