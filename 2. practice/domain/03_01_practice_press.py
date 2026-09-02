import pandas as pd

tags = pd.read_csv("data/03-01_유압·열설비_신호_계통태그목록.csv")
df = pd.read_csv("data/03-01_유압·열설비_신호_유압운전.csv")


# =========================================================
# Step 1. 주요 태그 확인
# =========================================================

hyd_tags = tags[tags["tag"].str.startswith("HYD")]

print(hyd_tags[["tag", "physical_qty", "unit", "circuit_position"]])

#                     tag physical_qty   unit circuit_position
# 0      HYD01_PRESS_PUMP           압력    bar           펌프 토출부
# 1   HYD01_PRESS_FILT_IN           압력    bar            필터 전단
# 2  HYD01_PRESS_FILT_OUT           압력    bar            필터 후단
# 3       HYD01_DP_FILTER           차압    bar       필터 전후단 계산값
# 4            HYD01_FLOW           유량  L/min         펌프 토출 배관
# 5         HYD01_OILTEMP           온도   degC            탱크 내부
# 6           HYD01_LEVEL           유면      %           탱크 유면계
# 7    HYD01_PUMP_CURRENT           전류      A           펌프 제어반
# 8       HYD01_VALVE_CMD           개도      %      방향 제어 밸브 지령
# 9        HYD01_VALVE_FB           개도      %      방향 제어 밸브 실제


# =========================================================
# Step 2. 정상 30일과 최근 10일 평균 비교
# =========================================================

print("\n===== Step 2. 정상 30일 / 최근 10일 평균 =====")

cols = [
    "HYD01_PRESS_PUMP",
    "HYD01_FLOW",
    "HYD01_OILTEMP",
    "HYD01_LEVEL",
    "HYD01_PUMP_CURRENT",
]

# 첫 30일
normal_30 = df[cols].iloc[:30].mean()

# 마지막 10일
recent_10 = df[cols].iloc[-10:].mean()

result = pd.DataFrame({"정상 30일 평균": normal_30, "최근 10일 평균": recent_10})

# 변화 방향
result["변화 방향"] = "변화 없음"

result.loc[result["최근 10일 평균"] > result["정상 30일 평균"], "변화 방향"] = "증가"

result.loc[result["최근 10일 평균"] < result["정상 30일 평균"], "변화 방향"] = "감소"


print(result.round(2))

# ===== Step 2. 정상 30일 / 최근 10일 평균 =====
#                     정상 30일 평균  최근 10일 평균  변화 방향
# HYD01_PRESS_PUMP       152.30     149.50     감소
# HYD01_FLOW             117.95     116.95     감소
# HYD01_OILTEMP           42.35      48.35     증가
# HYD01_LEVEL             88.00      88.00  변화 없음
# HYD01_PUMP_CURRENT      31.45      32.45     증가


# =========================================================
# Step 3. 필터 차압 계산
# =========================================================

print("\n===== Step 3. 필터 차압 =====")

# 차압 = 필터 전단 압력 - 필터 후단 압력
df["FILTER_DP"] = df["HYD01_PRESS_FILT_IN"] - df["HYD01_PRESS_FILT_OUT"]

# 각 구간
periods = [
    ("1~30일", 0, 29),
    ("31~60일", 30, 59),
    ("61~90일", 60, 89),
]

for name, start, end in periods:

    start_dp = df["FILTER_DP"].iloc[start]
    end_dp = df["FILTER_DP"].iloc[end]

    increase = end_dp - start_dp

    print(
        name,
        "시작 차압:",
        round(start_dp, 2),
        "종료 차압:",
        round(end_dp, 2),
        "증가폭:",
        round(increase, 2),
    )

# ===== Step 3. 필터 차압 =====
# 1~30일 시작 차압: 2.5 종료 차압: 5.0 증가폭: 2.5
# 31~60일 시작 차압: 2.5 종료 차압: 6.0 증가폭: 3.5
# 61~90일 시작 차압: 2.5 종료 차압: 7.0 증가폭: 4.5
