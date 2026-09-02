import pandas as pd

# ==================================================
# 1. 데이터 불러오기
# ==================================================

tags = pd.read_csv("data/03-01_회전기계_신호_회전기계태그목록.csv")

df = pd.read_csv("data/03-01_회전기계_신호_진동추세.csv")


# ==================================================
# 2. 데이터 컬럼 확인
# ==================================================

print("===== 실제 측정 데이터 컬럼 =====")
print(df.columns.tolist())


# ==================================================
# 3. 태그가 실제 데이터에 존재하는지 확인
# ==================================================

tags["보유여부"] = tags["tag"].isin(df.columns).map({True: "O", False: "X"})


# ==================================================
# 4. CASE A : 1번 모터
# ==================================================

print("\n===== CASE A : 1번 모터 =====")

motor_tags = tags[tags["equipment"] == "1번 모터"][
    [
        "tag",
        "physical_qty",
        "indicator",
        "summary",
        "unit",
        "direction",
        "install_location",
        "보유여부",
    ]
]

print(motor_tags)


# 베어링 손상 판단에 사용할 컬럼
motor_cols = [
    "MTR01_VIB_ACC",
    "MTR01_VIB_H",
    "MTR01_TEMP",
    "MTR01_CURRENT",
    "MTR01_RPM",
]


# 최솟값, 최댓값, 평균
print("\n===== 모터 데이터 요약 =====")

print(df[motor_cols].agg(["min", "max", "mean"]).round(2))


# 시작값과 마지막값 변화 확인
print("\n===== 모터 데이터 변화 =====")

for col in motor_cols:

    start = df[col].iloc[0]
    end = df[col].iloc[-1]

    change = end - start
    change_rate = change / start * 100

    print(
        f"{col}: "
        f"{start} → {end}, "
        f"변화량={round(change, 2)}, "
        f"변화율={round(change_rate, 2)}%"
    )


# ==================================================
# 5. CASE B : 1번 팬
# ==================================================

print("\n===== CASE B : 1번 팬 =====")

fan_tags = tags[tags["equipment"] == "1번 팬"][
    [
        "tag",
        "physical_qty",
        "indicator",
        "summary",
        "unit",
        "direction",
        "install_location",
        "보유여부",
    ]
]

print(fan_tags)


# ==================================================
# 6. 데이터의 실제 저장 주기 확인
# ==================================================

df["date"] = pd.to_datetime(df["date"])

interval = df["date"].diff().mode()[0]

print("\n실제 데이터 저장 주기:", interval)
