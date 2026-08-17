# 실습 3. 두 조건 묶기
# 목표
# 두 조건을 그리고(&)·또는(|)로 묶어 행을 추출

import pandas as pd

df_diecasting_small = pd.read_csv("data/13_diecasting_small.csv")
df_diecasting_small.info()

# 단계
# · 비스킷두께 조건과 사이클타임 조건을 각각 괄호로 감싸기
# · 두 조건을 그리고 기호로 묶어 모두 만족하는 행 추출
# · 같은 두 조건을 또는 기호로 묶어 결과 수 비교
# 예상 결과
# 그리고는 12건, 또는는 94건으로 개수 차이 확인

# · 두 조건을 그리고 기호 & 로 묶어 모두 만족하는 행 추출
df_sub1 = df_diecasting_small[(df_diecasting_small["비스킷두께"] >= 13)]
print(len(df_sub1))  # 결과 : 6

df_sub2 = df_diecasting_small[(df_diecasting_small["사이클타임"] >= 25)]
print(len(df_sub2))  # 결과 : 6

df_and = df_diecasting_small[
    (df_diecasting_small["비스킷두께"] >= 13)
    & (df_diecasting_small["사이클타임"] >= 25)
]
print(len(df_and))  # 결과 : 5

df_and = df_diecasting_small[
    (df_diecasting_small["비스킷두께"] <= 13)
    & (df_diecasting_small["사이클타임"] <= 25)
]
print(len(df_and))  

# · 같은 두 조건을 또는 기호 | 로 묶어 결과 수 비교
df_or = df_diecasting_small[
    (df_diecasting_small["비스킷두께"] >= 13)
    | (df_diecasting_small["사이클타임"] >= 25)
]
print(len(df_or))  # 결과 : 7

df_or = df_diecasting_small[
    (df_diecasting_small["비스킷두께"] <= 13)
    | (df_diecasting_small["사이클타임"] <= 25)
]
print(len(df_or))  
