# pd.cut 구간 빈도 코드

import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()
print(df.head())

print(df["온도"].value_counts())
# 위와 같이 범위 없이 개별 경우의 수를 따지면 62가지나 되어버림

# 그래서 범위를 설정해 경우의 수를 줄여내는 것이 필요함 -> 범주화


# pd.cut 으로 수치형을 구간으로 묶어 세기
# 형식 : pd.cut(df['수치열], bins=[경계...], labels = [이름...]) -> 구간 라벨 Series
# 엣지 : 경계(bins)는 이름표(labels)보다 반드시 하나 많아야 함(경계 4개 -> 구간 3개)
# band= pd.cut(df['온도']) # 요롷게 하면 안됨
band = pd.cut(df["온도"], bins=[0, 40, 50, 200], labels=["낮음", "보통", "높음"])
print(band.value_counts())
# 온도
# 낮음    41
# 보통    40
# 높음    39