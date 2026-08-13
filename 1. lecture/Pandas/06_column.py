# 단일 컬럼(column) 선택

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

df_sub = df["형체력"]
df_sub.info()

# 데이터 프레임(2차원)에서 컬럼 한개를 도려내보면 시리즈(1차원)가 된다.
s = df["형체력"]
s.info()

df["형체력"].info()  # Series
df[["형체력"]].info()  # DataFrame
df["형체력", "실린더압력"].info()
df[["형체력", "실린더압력"]].info()

