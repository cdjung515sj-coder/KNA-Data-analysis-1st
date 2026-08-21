# 실습 1. dropna로 행,열 삭제

# 결측 있는 행과

import pandas as pd

df_imp_2 = pd.read_csv("data/15_02_Injection_Molding_process.csv", encoding="utf-8")
df_imp_2.info()

print(df_imp_2.shape)  # (250, 22)

print(df_imp_2.dropna().shape)  # (76, 22)

print(df_imp_2.dropna(axis=1).shape)  # (250, 10)


# how로 완전히 빈 행만 삭데하는 기준 적용 -> how = "all"
print(df_imp_2.dropna(how="all").shape)
# 250개 row가 다 살아남았다는 건, NaN으로 모든 컬럼 내용이 다 채워진 row가 없다는 뜻이다.

#  thresh로 값이 일정(예)20개 ) 개수 "이상"인 행만 남기기 -> thresh = 20
print(df_imp_2.dropna(thresh=20).shape)  # (162, 22)
# 250 -162 =88 개 row는 NaN이 3개 이상이라는 뜻

# subset으로 특정 컬럼이 빈 행만 삭제
# 예, 불량여부 컬럼에 NaN이 있는 row들만 제거 --> subset = ["불량여부"]
print(df_imp_2.dropna(subset=["불량여부"]).shape)  # (250, 22)
# '불량여부" 컬럼에는 NaN이 하나도 없다고 판단할 수 있다.
