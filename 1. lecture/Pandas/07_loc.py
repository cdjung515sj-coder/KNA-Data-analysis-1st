# loc 행과 열

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

print("=" * 40)

df.loc[0].info()  # <class 'pandas.Series'>
df.loc[0:2].info()  # <class 'pandas.DataFrame'>

print("=" * 40)

s = df.loc[0]
s.info()

df_sub = df.loc[0:2]
df_sub.info()
print(df_sub)  # 0~1 뻔쨰 행 출력
print(df_sub.head())


# 행(row)과 열(column) 언급 서브 DF 만들기
df_sub2 = df.loc[0:2, ["품질등급", "형체력"]]  # 이렇게 차례대로 선택하지 않아도 됨
df_sub2.info()
print(df_sub2) # 출력해보면 품질등급 형체력 순으로 출력됨
