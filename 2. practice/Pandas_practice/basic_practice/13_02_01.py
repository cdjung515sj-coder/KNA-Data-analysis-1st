# 실습 1. 단일 조건으로 행 추출하기
# 목표
# 조건을 만들고 그 조건으로 원하는 행만 추출

import pandas as pd

df_diecasting_smaill = pd.read_csv("data/13_diecasting_small.csv")
df_diecasting_smaill.info()


# 단계
# · 비교 연산자로 실린더압력 기준의 조건식을 만들어 Boolean Series 생성
s = df_diecasting_smaill["실린더압력"]
s.info()
s_boolean = s >= 230
s_boolean.info()


# · sum으로 조건을 만족하는 행 개수 확인
print(f"조건을 만족하는 행 개수 : {s_boolean.sum()}")

# · 만든 조건을 데이터프레임 대괄호에 넣어 행 추출 ->
# 전체 df를 대상으로 앞서 특정 컬럼에 대한 불리언 시리즈를 컬럼 요구하는 [] 사이에 넣어주면, 각 줄마다 비교를 해서 T인 경우만 추려 새로운 DF 를 만든다.
df_sub = df_diecasting_smaill[df_diecasting_smaill["실린더압력"] >= 230]
df_sub.info()
# df의 행의 갯수를 확인할 떄 len() 사용도 가능
print(len(df_sub))

# 예상 결과
# 참 개수와 추출 행 수가 같게 출력 (실린더압력 230 이상 19건)
