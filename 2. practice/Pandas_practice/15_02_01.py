# 실습 1. dropna로 행,열 삭제

# 결측 있는 행과 열을 삭제하고 크기 변화 확인할 것


import pandas as pd

df_imp_2 = pd.read_csv("data/15_02_Injection_Molding_process.csv", encoding="utf-8")
df_imp_2.info()

# 원본 크기 shape로 확인

print(df_imp_2.shape)

# dropna로 행 모두 삭제

print(df_imp_2.dropna().shape)

# 방향을 열로 바꿔 결측 있는 열 삭제

print(df_imp_2.dropna(axis=1).shape)


# 예상 결과
# 250×22 → 행삭제 76×22, 열삭제 250×10
