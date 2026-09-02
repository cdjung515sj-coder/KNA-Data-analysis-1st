import pandas as pd

tags = pd.read_csv("data/03-01_회전기계_신호_회전기계태그목록.csv")
df = pd.read_csv("data/03-01_회전기계_신호_진동추세.csv")

# 1번 모터에 대한 태그 목록

print(
    tags.loc[tags["equipment"] == "1번 모터"],
    ["tag", "indicator", "summary", "unit", "direction"],
)

"""
             tag equipment physical_qty indicator summary  unit direction  install_location
0    MTR01_VIB_H     1번 모터           진동        속도     RMS  mm/s        수평       구동측 베어링 하우징
1    MTR01_VIB_V     1번 모터           진동        속도     RMS  mm/s        수직       구동측 베어링 하우징
2    MTR01_VIB_A     1번 모터           진동        속도     RMS  mm/s       축방향       구동측 베어링 하우징
3  MTR01_VIB_ACC     1번 모터           진동       가속도    PEAK     g        수평       구동측 베어링 하우징
4  MTR01_CURRENT     1번 모터           전류        전류     순시값     A      해당없음     모터 제어반 전류 변성기
5     MTR01_TEMP     1번 모터           온도        온도     순시값  degC      해당없음  구동측 베어링 매입 측온저항체
6      MTR01_RPM     1번 모터          회전수       회전수     순시값   rpm      해당없음       축 단부 회전수 센서 
 
 ['tag', 'indicator', 'summary', 'unit', 'direction']
 
 """

# 진동의 정상 번위 정하기
# 맨 앞 기준으로 20일 구간을 정상 기간으로 볼 것.

MTR = ["MTR01_VIB_H", "MTR01_VIB_V", "MTR01_VIB_A", "MTR01_VIB_ACC"]
normal = df.head(20)

print(normal[MTR].agg(["min", "max"]))  # 극단값 (최소, 최대값) 출력


## 펌프 극단값 출력하기

PMP = [
    "PMP01_VIB_H",
    "PMP01_VIB_V",
    "PMP01_VIB_A",
    "PMP01_VIB_ACC",
]

normal = df.head(20)
print(normal[PMP].agg(["min", "max"]))

"""
     PMP01_VIB_H  PMP01_VIB_V  PMP01_VIB_A  PMP01_VIB_ACC
min          2.0          1.6          0.9           0.60
max          2.2          1.7          1.0           0.63

"""

print("")


def first_over(col):
    """ 어상 구간 최댓값을 처음 넘어선 행의 순서를 반환합니다."""
    limit = normal[col].max()  # 20일 구간(normal)의 최댓값을 정상 범위로 설정
    over = df.index[df[col] > limit]  # 정상 번위를 넘는 index를 불러온다
    # print(over)
    # # Index([38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
    # #    58, 59],
    # #   dtype='int64')
    # print(over[0])  # 38
    return int(over[0]) + 1 if len(over) else None


print("----------------------")
print("[1번 모터]")
for c in MTR:
    print(c, first_over(c))

"""
[1번 모터]
MTR01_VIB_H 39
MTR01_VIB_V 44
MTR01_VIB_A None
MTR01_VIB_ACC 22
"""

print("----------------------")
print("[1번 펌프]")
for c in PMP:
    print(c, first_over(c))

"""
[1번 펌프]
PMP01_VIB_H 39
PMP01_VIB_V 38
PMP01_VIB_A 35
PMP01_VIB_ACC None
"""

## 모터의 전류와 온도

print("--------------")
print("[1번 모터: 전류와 온도]")
for c in ["MTR01_CURRENT","MTR01_TEMP"]:
    print(c, first_over(c))

# 전류와 온도가 이상반응에 대해서 늦게 반응한다.
'''
[1번 모터: 전류와 온도]
MTR01_CURRENT 49
MTR01_TEMP 53
'''

##### 모터1번의 회전수
# 모터1번 회전수의 컬럼 이름
# 1780, 1450 종류의 숫자가 각각 몇 번 찍히는지
print(df["MTR01_RPM"].value_counts())
'''
MTR01_RPM
1780    56
1450     4
'''
print("==========")
print(df.loc[
    df["MTR01_RPM"]==1780, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]
].head(4))
print(df.loc[
    df["MTR01_RPM"]==1450, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]
])

'''
         date  MTR01_VIB_H  MTR01_VIB_ACC  MTR01_RPM
0  2026-01-01          1.8           0.52       1780
1  2026-01-02          1.9           0.54       1780
2  2026-01-03          1.8           0.53       1780
3  2026-01-04          2.0           0.55       1780
          date  MTR01_VIB_H  MTR01_VIB_ACC  MTR01_RPM
29  2026-01-30          1.3           0.61       1450
30  2026-01-31          1.3           0.63       1450
31  2026-02-01          1.4           0.67       1450
32  2026-02-02          1.3           0.68       1450
'''
# 설비의 변화가 아닌 회전수(RPM)의 변화로 진동수가 변경되었다.