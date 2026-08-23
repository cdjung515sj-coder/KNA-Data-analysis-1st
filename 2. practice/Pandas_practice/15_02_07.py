# 실습 7. 그룹별 대체
# 목표
# 그룹별 평균으로 채워 집단 특성 반영
import pandas as pd

df_imp_2 = pd.read_csv("data/15_02_Injection_Molding_process.csv", encoding="utf-8")


# 단계
# · 제품유형으로 그룹을 나누기
print(df_imp_2.groupby("사출기")["스크루속도"].mean())
# 사출기
# 1호기    38.857339
# 2호기    38.858118
# 3호기    37.878909

print(df_imp_2.groupby("사출기")["감압시간"].mean())
# 사출기
# 1호기    0.322179
# 2호기    0.322368
# 3호기    0.322400

# · 각 그룹의 평균으로 그 그룹의 결측을 채우기
df_imp_2["감압시간"] = df_imp_2.groupby("사출기")["감압시간"].transform(
    lambda x: x.fillna(x.mean())
)
# 사출기 그룹을 나누고, 그룹마다 감압시간의 시리즈를 뽑아서 그 시리즈의 NaN들을 그 시리즈의 평균들로 채운다
# lambda x: x.fillna(x.mean()) 이렇게 하면 시리즈에 대해 모든 값을 채운다
# = lambda s: s.fillna(s.mean())

print(df_imp_2["감압시간"].isna().sum())


# · 남은 수치 결측은 전체 중앙값으로 마무리하고 검증
# 이런 코드는 실제로 쓸 가능성이 없음 - 컬럼 특성을 전혀 고려하지 않기 때문
df_numbers = df_imp_2.select_dtypes("number")
df_imp_2[df_numbers.columns] = df_numbers.fillna(df_numbers.median())

print(df_imp_2.isna().sum())
print(df_imp_2.isna().sum().sum())


# 예상 결과
# 토크를 유형별 평균으로 대체, 남은 결측 0
