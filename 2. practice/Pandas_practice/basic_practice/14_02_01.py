# 실습 1. 평균·분산·표준편차 구하기
# 목표
# 대푯값과 흩어짐을 나타내는 세 통계량 구하기

import pandas as pd

df_hydraulic = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")

# 단계
# · 진동 열 전체의 평균·분산·표준편차를 각각 구하기
print(df_hydraulic["진동"].mean().round(3))  # 평균 : 0.616
print(df_hydraulic["진동"].var().round(3))  #  분산 : 0.004
print(df_hydraulic["진동"].std().round(3))  #  표준편차 : 0.064

# · 표준편차를 제곱하면 분산과 같아지는지 확인
print((df_hydraulic["진동"].std() ** 2).round(5))  # 분산 : 0.00409

# · 라인으로 그룹을 나눠(groupby) 라인별 평균과 표준편차 비교
# print(df.groupby("냉각기상태")["진동"].mean().round(3))
# print(df.groupby("냉각기상태")["진동"].std().round(3))
# 판다스가 더 권장하는 방식으로 통계 항목별 이름 붙여 정리하기
print(
    df_hydraulic.groupby("냉각기상태")
    .agg(
        평균진동=("진동", "mean"),
        진동편차=("진동", "std"),
    )
    .round(3)
)

#         평균진동   진동편차
# 냉각기상태
# 고장     0.688  0.048
# 저하     0.610  0.010
# 정상     0.549  0.009

# 예상 결과
# 전체 통계와 라인별 평균·표준편차 출력 (표준편차²=분산)
#
