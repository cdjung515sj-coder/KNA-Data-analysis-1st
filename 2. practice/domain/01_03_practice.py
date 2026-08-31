# 앞 6시간과 뒤 6시간 비교
# 목표 : 정상 구간과 변화 구간의 평균 비교
# 요구사항
# 앞 6시간과 뒤 6시간으로 나누어 아래 평균을 비교하라
# 송풍량, 송풍압, 송풍기 진동 세 값의 변화 방향을 각각 적을 것

# 제출물 : 앞, 뒤 6시간 평균 비교표와 변화 방향 3개

# 힌트
# before = df.iloc[:360]
# after = df.iloc[360:]

# cols = ["blast_flow_nm3min", "blast_pressure_kpa", "blower_vib_mms"]

# before[cols].mean()
# after[cols].mean()

import pandas as pd

df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv")
print(df.shape)

before = df.iloc[:360]
after = df.iloc[360:]

cols = ["blast_flow_nm3min", "blast_pressure_kpa", "blower_vib_mms"]

before_mean = before[cols].mean()
after_mean = after[cols].mean()

# 비교표
compare = pd.DataFrame(
    {
        "앞 6시간 평균": before_mean,
        "뒤 6시간 평균": after_mean,
    }
)

print(compare.round(1))

#                     앞 6시간 평균  뒤 6시간 평균
# blast_flow_nm3min     5198.7    4977.8
# blast_pressure_kpa     379.8     397.7
# blower_vib_mms           3.4       3.4

print(
    "송풍량 변화 :",
    round((after_mean["blast_flow_nm3min"] - before_mean["blast_flow_nm3min"]), 3),
)
print(
    "송풍압 변화 :",
    round((after_mean["blast_pressure_kpa"] - before_mean["blast_pressure_kpa"]), 3),
)
print(
    "송풍기 진동 변화 :",
    round((after_mean["blower_vib_mms"] - before_mean["blower_vib_mms"]), 3),
)


cols_kr = {
    "blast_flow_nm3min": "송풍량",
    "blast_pressure_kpa": "송풍압",
    "blower_vib_mms": "송풍기 진동",
}

for col in cols:
    change = after_mean[col] - before_mean[col]

    if change > 0:
        direction = "증가"

    elif change < 0:
        direction = "감소"

    else:
        direction = "변화 없음"

    if col == "blast_flow_nm3min":
        if direction == "감소":
            reason = "원료층을 통과하는 공기량이 줄어 통기성이 악화되었을 가능성이 있음"
        elif direction == "증가":
            reason = "원료층을 통과하는 공기량이 늘어 통기성이 개선되었을 가능성이 있음"
        else:
            reason = "송풍량의 변화가 없음"

    elif col == "blast_pressure_kpa":
        if direction == "증가":
            reason = "공기를 밀어 넣기 위해 더 높은 압력이 필요해져 공기 흐름 저항이 증가했을 가능성이 있음"
        elif direction == "감소":
            reason = "공기를 밀어 넣는 데 필요한 압력이 낮아져 공기 흐름 저항이 감소했을 가능성이 있음"
        else:
            reason = "송풍압의 변화가 없음"

    elif col == "blower_vib_mms":
        if direction == "증가":
            reason = "송풍기 진동이 증가하여 설비의 흔들림이 커졌을 가능성이 있음"
        elif direction == "감소":
            reason = "송풍기 진동이 감소하여 설비의 흔들림이 줄어든 것으로 볼 수 있음"
        else:
            reason = "송풍기 진동의 변화가 없음"

    print(f"\n {cols_kr[col]} : { round(change, 3)}  ➡️  {direction} \n💡 {reason}")
