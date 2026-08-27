
# 실습 5. fillna 평균·중앙값 대체
# 목표
# 결측을 평균과 중앙값으로 채우고 차이 이해
import pandas as pd

df_imp_2 = pd.read_csv("data/15_02_Injection_Molding_process.csv", encoding="utf-8")
df_imp_2.info()

# 1. df["컬럼명"].isna().sum(): 지정한 특정 컬럼 하나 안의 결측치 개수
print(df_imp_2["최대사출압"].isna().sum())  # 60개 NaN 확인

# · 대상 컬럼의 평균과 중앙값을 각각 구해 비교
mean = df_imp_2["최대사출압"].mean().round(2)
print(f"최대사출압 평균 : {mean}")  #  1241.67

s_fillmean = df_imp_2["최대사출압"].fillna(mean)
print(s_fillmean)
df_imp_2["최대사출압"] = s_fillmean
print(
    f"채운 후 결측치 개수: {df_imp_2["최대사출압"].isna().sum()}"
)  # 최대사출압 컬럼 NaN 평균으로 채워 0개의 결측치


# · fillna로 평균을 채운 결과 만들기
median = df_imp_2["최대사출압"].median()
print(f"최대사출압 중앙값 : {median}")  # 최대사출압 중앙값 : 1240.84


# · fillna로 중앙값을 채운 결과 만들기(이상치에 강함)
s_fillmedian = df_imp_2["최대사출압"].fillna(median)
print(s_fillmedian)
df_imp_2["최대사출압"] = s_fillmedian
print(
    f"채운 후 결측치 개수: {df_imp_2["최대사출압"].isna().sum()}"
)  # 최대사출압 컬럼 NaN 중앙값으로 채워 0개의 결측치


# 예상 결과
# 센서17 평균 466.26·중앙값 465.9로 대체, 남은 결측 0
