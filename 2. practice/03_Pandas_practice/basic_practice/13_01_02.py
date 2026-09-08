# 실습 2. 열 선택하기

# data/13_diecasting_small.csv  파일 열기
import pandas as pd

df_diecasting_small = pd.read_csv("data/13_diecasting_small.csv")

print(df_diecasting_small.columns)

# 대괄호 한 겹으로 단일 열을 Series로 선택
# '형체력' 컬럼 하나만 빼오기

print(df_diecasting_small["형체력"].info())  # <class 'pandas.Series'>
print(df_diecasting_small["형체력"])

# 대괄호 두 겹으로 복수 열을 DataFrame으로 선택
# '형체력', '실린더압력' 두개를 선택하기

print(
    df_diecasting_small[["형체력", "실린더압력"]].info()
)  # <class 'pandas.DataFrame'>
print(df_diecasting_small[["형체력", "실린더압력"]])

#  선택한 열에 mean으로 평균 계산
# df['형체력'].mean() -> round로 소수점 이하 1자리까지만 나오게 조정해주세요
print(df_diecasting_small["형체력"].mean())
print(df_diecasting_small["실린더압력"].mean())
print(df_diecasting_small[["형체력", "실린더압력"]].mean())

print(round(df_diecasting_small["형체력"].mean(), 1))
print(round(df_diecasting_small[["형체력", "실린더압력"]].mean(), 1))
