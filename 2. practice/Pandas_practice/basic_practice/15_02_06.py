# 실습 6. 최빈값·앞뒤 값 대체
# 목표
# 범주형은 최빈값, 시계열은 앞뒤 값으로 채우기
import pandas as pd

df_imp_2 = pd.read_csv("data/15_02_Injection_Molding_process.csv", encoding="utf-8")


# 단계
# · 범주형 열의 최빈값을 구해 채우기
# 사출기 컬럼은 1~3호기 범주형으로 판단
print(f"채우기 전 사출기 결측치 수: {df_imp_2['사출기'].isna().sum()}")
print(f"사출기 최빈값 : {df_imp_2["사출기"].mode()[0]}")  # 1호기

df_imp_2["사출기"] = df_imp_2["사출기"].fillna(df_imp_2["사출기"].mode()[0])
print(f"채운 후 사출기 결측치 수: {df_imp_2['사출기'].isna().sum()}")

# · 측정시각 순으로 정렬해 시계열 순서 만들기
df_imp_2 = df_imp_2.sort_values("측정시각")

# · ffill로 앞 값, bfill로 남은 앞쪽 결측까지 채우기
print(df_imp_2["전환압력"].isna().sum())  # 68

df_imp_2["전환압력"] = (
    df_imp_2["전환압력"].ffill().bfill()
)  # 자주 볼 시계열 채우기 패턴⭐⭐
print(df_imp_2["전환압력"].isna().sum())  # 0개 NaN

# 예상 결과
# 설비명은 최빈값(절삭기A), 온도는 앞뒤 값으로 대체
