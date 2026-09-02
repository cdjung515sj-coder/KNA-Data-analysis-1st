import pandas as pd

# 데이터 불러오기
tags = pd.read_csv("data/03-01_유압·열설비_신호_계통태그목록.csv")
df = pd.read_csv("data/03-01_유압·열설비_신호_가열로온도.csv")


# ==================================================
# Step 1. FUR 태그 분류
# ==================================================

fur_tags = tags[tags["tag"].str.startswith("FUR")]["tag"]

atmosphere = fur_tags[fur_tags.str.contains(r"_Z[123]_TEMP_[LR]")].tolist()

material = fur_tags[fur_tags.str.contains("MAT_TEMP")].tolist()

exhaust = fur_tags[fur_tags.str.contains("EXH_TEMP")].tolist()

line_speed = fur_tags[fur_tags.str.contains("LINE_SPEED")].tolist()

print("[Step 1]")
print("분위기 온도:", atmosphere)
print("소재 표면 온도:", material)
print("배기가스 온도:", exhaust)
print("라인 속도:", line_speed)


# ==================================================
# Step 2. 앞 20일 평균 편차
# 편차 = 우측 - 좌측
# ==================================================

df["Z1_diff"] = df["FUR01_Z1_TEMP_R"] - df["FUR01_Z1_TEMP_L"]
df["Z2_diff"] = df["FUR01_Z2_TEMP_R"] - df["FUR01_Z2_TEMP_L"]
df["Z3_diff"] = df["FUR01_Z3_TEMP_R"] - df["FUR01_Z3_TEMP_L"]

avg_diff = df.iloc[:20][["Z1_diff", "Z2_diff", "Z3_diff"]].mean().round(1)

print("\n[Step 2]")
print(avg_diff)


# ==================================================
# Step 3. 1, 20, 40, 60일차 편차
# ==================================================

days = [1, 20, 40, 60]
idx = [day - 1 for day in days]

step3 = df.iloc[idx][["Z1_diff", "Z2_diff", "Z3_diff"]].copy()

step3.index = days

print("\n[Step 3]")
print(step3)


# ==================================================
# Step 4. Z2 좌측 / 우측 온도
# ==================================================

step4 = df.iloc[idx][["FUR01_Z2_TEMP_L", "FUR01_Z2_TEMP_R"]].copy()

step4.index = days

print("\n[Step 4]")
print(step4)


# ==================================================
# Step 5. 소재 온도 / 라인 속도
# ==================================================

days2 = [1, 20, 44, 45, 60]
idx2 = [day - 1 for day in days2]

step5 = df.iloc[idx2][["FUR01_MAT_TEMP", "FUR01_LINE_SPEED"]].copy()

step5.index = days2

print("\n[Step 5]")
print(step5)


# 답안
print("\n\n================ 답안 ================")


tags = pd.read_csv("data/03-01_유압·열설비_신호_계통태그목록.csv")
fur = pd.read_csv("data/03-01_유압·열설비_신호_가열로온도.csv")

# ==================================================
# Step 1. FUR 태그 분류
# ==================================================

zones = ["Z1", "Z2", "Z3"]
for z in zones:
    fur["Diff_" + z] = fur["FUR01_" + z + "_TEMP_R"] - fur["FUR01_" + z + "_TEMP_L"]

print(fur.head(20)[["Diff_Z1", "Diff_Z2", "Diff_Z3"]].mean())

# Diff_Z1    5.1
# Diff_Z2    3.1
# Diff_Z3    3.1

# ==================================================
# Step 2. 앞 20일 평균 편차
# 편차 = 우측 - 좌측
# ==================================================

print(fur[["Diff_Z1", "Diff_Z2", "Diff_Z3"]].iloc[[0, 19, 39, 59]])
