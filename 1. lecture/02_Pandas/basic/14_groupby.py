# groupby 기본 코드

import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()
print(df.head())

# '냉각기상태' 컬럼의 내용별로 그룹핑 처리 -> 분할
print(
    df.groupby("냉각기상태")
)  # <pandas.api.typing.DataFrameGroupBy object at 0x0000018A0B7F1550>

# 분할된 DF 마다 '온도' 컬럼이 있으니 '온도'의 평균을 구해보자
print(
    df.groupby("냉각기상태")["온도"]
)  # <pandas.api.typing.SeriesGroupBy object at 0x000001F5577A7D90>

print(df.groupby("냉각기상태")["온도"].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89


# 온도 말고 냉각기상태별 진동 평균도 알고 싶다면?
print(df.groupby("냉각기상태")["진동"].mean().round(2))
# 냉각기상태
# 고장    0.69
# 저하    0.61
# 정상    0.55

# 이렇게 계속 새로 만들어야되나? Nope !
# 대괄호가 중첩된 상태 [[...]]
print(df.groupby("냉각기상태")[["진동", "온도"]].mean().round(2))
#          진동     온도
# 냉각기상태
# 고장     0.69  54.67
# 저하     0.61  45.46
# 정상     0.55  35.89
# 냉각기상태에 따른 그룹별 온도 평균과 진동 평균을 동시에 볼 수 있음

# 냉각기상태 별로 다시 운전부하 상태들에 따라 group들을 만들어 평균온도 계산
print(df.groupby(["냉각기상태", "운전부하"])["온도"].mean().round(2))
# 냉각기상태  운전부하
# 고장     고부하     55.51
#        저부하     54.05
# 저하     고부하     44.07
#        저부하     45.58
# 정상     고부하     35.89
