# 실습 6. 특정 구간 추출 종합
# 열 선택·loc·iloc를 결합해 특정 구간을 추출하는 종합
import pandas as pd

df_diecasting_shot = pd.read_csv("data/13_diecasting_shot.csv")

# · 여러 feature 열을 선택한 뒤 iloc로 앞 구간 추출
cols = ["실린더압력", "주조압력", "사이클타임", "비스킷두께", "형체력"]
print(df_diecasting_shot[cols].iloc[0:10].shape)  # 결과는? (10, 5)

# · loc 라벨 범위로 두 열 구간 추출
cols2 = ["실린더압력", "주조압력"]
print(df_diecasting_shot.loc[0:10, cols2].shape)  # (11, 2)


# · iloc 위치 범위로 앞쪽 열 구간 추출
# .iloc(50:60, 0:6)
df_sub3 = df_diecasting_shot.iloc[0:10, 0:6]
print(df_sub3.shape)  # (10, 6)