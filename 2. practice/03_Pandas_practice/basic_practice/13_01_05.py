# 실습 5. loc·iloc로 행·열 동시 선택하기
# 행과 열을 동시에 지정해 원하는 부분만 추출

# data/13_diecasting_small.csv 사용
import pandas as pd

df_diecasting_small = pd.read_csv("data/13_diecasting_small.csv")
print(df_diecasting_small.columns)

# · loc로 행 범위와 열 이름을 함께 지정
df_sub = df_diecasting_small.loc[0:4, ["품질등급", "형체력"]]
print(df_sub.shape)  # 결과는? (5, 2)

# · 다른 행 범위에서 세 열 선택
df_sub2 = df_diecasting_small.loc[5:9, ["형체력", "실린더압력", "주조압력"]]
print(df_sub2.shape)  # 결과는? (5, 3)

# · iloc 음수 인덱스로 마지막 행 선택
print(len(df_diecasting_small.iloc[-3:]))  # 결과는? # 3
