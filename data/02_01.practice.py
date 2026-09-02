import pandas as pd

df_tag = pd.read_csv("data/02-01_측정의_3요소_설비태그목록.csv")
df = pd.read_csv("data/02-01_측정의_3요소_측정샘플.csv")

case_a = df_tag[df_tag["tag"].str.startswith("MTR")]
print(case_a[["tag", "description", "unit", "install_location", "sampling_sec"]].head())

# CASE B : HYD, FUR 태그
case_b = df_tag[df_tag["tag"].str.startswith(("HYD", "FUR"))]
print(case_b[["tag", "description", "unit", "install_location", "sampling_sec"]])

# Step 2 # timestamp를 날짜/시간 자료형으로 변환

df["timestamp"] = pd.to_datetime(df["timestamp"])

# 앞 행과의 시간 차이 계산
time_diff = df["timestamp"].diff().dt.total_seconds()
print("실제 저장 간격:", time_diff.dropna().unique())

# 결과: [60.]
#
# # Step 3
#
sensor_cols = [
    "MTR01_VIB_RMS_H",
    "MTR01_CURRENT",
    "MTR01_TEMP",
    "HYD01_PRESS_IN",
    "FUR01_TEMP_Z1",
]

for col in sensor_cols:
    min_value = df[col].min()
    max_value = df[col].max()
    mean_value = df[col].mean()
    # 앞의 값과 현재 값의 차이
    change = df[col].diff().abs()
    # 변화가 0인 경우 제외
    min_change = change[change > 0].min()
    print(
        col,
        "최솟값:",
        min_value,
        "최댓값:",
        max_value,
        "평균:",
        round(mean_value, 2),
        "최소 변화폭:",
        min_change,
    )


for col in sensor_cols:
    min_value = df[col].min()
    max_value = df[col].max()
    mean_value = df[col].mean()

    change = df[col].diff().abs()
    min_change = change[change > 0].min()

    print(col, min_value, max_value, round(mean_value, 2), min_change)


import pandas as pd

df = pd.read_csv("data/02-01_측정의_3요소_측정샘플.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

print(df["timestamp"].diff().dt.total_seconds().dropna().unique())


import matplotlib.pyplot as plt

sensor_cols = [
    "MTR01_VIB_RMS_H",
    "MTR01_CURRENT",
    "MTR01_TEMP",
    "HYD01_PRESS_IN",
    "FUR01_TEMP_Z1",
]

df[sensor_cols].plot(subplots=True, figsize=(10, 10))

plt.tight_layout()
plt.show()


# -------------------------------------------------------------------------------------------------

# <3단원 실습문제 4>

import pandas as pd

# 02-01_측정의_3요소_설비태그목록
# 02-01_측정의_3요소_측정샘플

tags = pd.read_csv("data/02-01_측정의_3요소_설비태그목록.csv")
df = pd.read_csv("data/02-01_측정의_3요소_측정샘플.csv")

##### 실습1

#   - 케이스 A : 회전기계 계통 (MTR 로 시작하는 태그)
#   - 케이스 B : 유압·열설비 계통 (HYD, FUR 로 시작하는 태그)

# tag,description,unit,sampling_sec,range_min
# range_max,resolution,install_location

##### case A
print(tags["tag"].str.startswith("MTR"))  # tag컬럼에서 MTR로 시작되는지 검사: T/F

# 대괄호 안에 조건식 -> True인 데이터만 모아서 저장
case_a = tags[tags["tag"].str.startswith("MTR")]
# print(case_a)

##### case B
print(tags["tag"].str.startswith(("HYD", "FUR")))
case_b = tags[tags["tag"].str.startswith(("HYD", "FUR"))]
print(case_b)

##### 실습2
df["timestamp"] = pd.to_datetime(df["timestamp"])
gaps = df["timestamp"].diff().value_counts()
print(gaps)
# 0 days 00:01:00    119
# Name: count, dtype: int64

##### 실습3, 최솟값, 최댓값, 평균, 값이 변하는 최소 폭
cols = [
    "MTR01_VIB_RMS_H",
    "MTR01_CURRENT",
    "MTR01_TEMP",
    "HYD01_PRESS_IN",
    "FUR01_TEMP_Z1",
]

print(df[cols].agg(["min", "max", "mean"]).round(2))


# ------------------------------------------------
import pandas as pd

tags = pd.read_csv("data/02-01_측정의_3요소_설비태그목록.csv")
df = pd.read_csv("data/02-01_측정의_3요소_측정샘플.csv")

cols = [
    "MTR01_VIB_RMS_H",
    "MTR01_CURRENT",
    "MTR01_TEMP",
    "HYD01_PRESS_IN",
    "FUR01_TEMP_Z1",
]

# 최솟값, 최댓값, 평균
print(df[cols].agg(["min", "max", "mean"]).round(2))


# 행간 데이터 변화 중 최소 폭
for col in cols:
    diff = df[col].diff().abs()

    # diff 데이터 프레임에서 0을 제외하고 최솟값을 가지고 오고 있는 중
    min_change = diff[diff > 0].min()
    repeated = (diff==0).sum()

    print(f"태그 이름, 최소 차이, 반복횟수 {col} 최소 변화폭: {round(min_change, 2)}, {repeated}")
