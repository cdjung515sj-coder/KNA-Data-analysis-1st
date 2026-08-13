# loc 행과 열
"""df.loc[행 라벨, 열 라벨]"""

"""

df.loc[0]                    # 행 하나
df.loc[0:4]                  # 행 범위
df.loc[:, "품질등급"]         # 열 하나
df.loc[:, ["품질등급", "형체력"]]  # 열 여러 개
df.loc[0:4, ["품질등급", "형체력"]] # 행 + 열 동시 선택

"""

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
print(df_sub2)  # 출력해보면 품질등급 형체력 순으로 출력됨


# iloc 인덱스 선택
"""df.iloc[행, 열]"""
""" loc과 달리 이름이 아니라 위치 번호를 사용한다는 차이 """
"""

df.iloc[0]        # 0번째 행
df.iloc[0, 2]     # 0번째 행, 2번째 열
df.iloc[0:10]     # 0~9번째 행
df.iloc[0:10, 0:6] # 0~9번째 행 + 0~5번째 열

"""

# ==============================================================

# 열 1개
df["열이름"]

# 열 여러 개
df[["열1", "열2"]]


# loc : 라벨 기준
# df.loc[행라벨, 열라벨]

# 행 하나
df.loc[0]

# 행 범위
df.loc[0:4]

# 행 + 열
df.loc[0:4, ["열1", "열2"]]


# iloc : 위치 번호 기준
# df.iloc[행번호, 열번호]

# 행 하나
df.iloc[0]

# 행 범위
df.iloc[0:5]

# 행 + 열
df.iloc[0:5, 0:2]


# 행 개수
len(df)

# 행, 열 개수
df.shape