# 실습 3. 결측 비율 기준 컬럼 제거
# 목표
# 결측 비율이 높은 컬럼만 골라 제거

import pandas as pd

df_imp_2 = pd.read_csv("data/15_02_Injection_Molding_process.csv", encoding="utf-8")
df_imp_2.info()
print(f" 행, 열 크기  : {df_imp_2.shape}")  # (250, 22)
print(f" === 열 이름 목록 === \n {df_imp_2.columns}")
print(f" === 컬럼별 결측치 개수 === \n {df_imp_2.isna().sum()}")

# 단계
# · 컬럼별 결측 비율을 계산
df_rate = df_imp_2.isna().sum() / len(df_imp_2)
print(f" === 컬럼별 결측 비율 === \n {df_rate}")


# · 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기
# -> 40% 이상 NaN으로 채워진 컬럼 목록
terminates = df_rate[df_rate > 0.4]
print(terminates)

# 최초 컬럼 이름들이 df_terminates.index.tolist() # ['최대사출속도', '감압시간']
list_terminates = terminates.index.tolist()
print(list_terminates)


# · 그 컬럼들을 drop으로 제거하고 크기 확인
# drop에 컬럼을 제시하면 기본동작 : 컬럼을 지워버림
df_final = df_imp_2.drop(columns=list_terminates)
df_final.info()


# 예상 결과
# 40% 초과 센서19·20 제거 → 250×20
