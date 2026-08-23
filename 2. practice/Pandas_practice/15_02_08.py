# 실습 8. 제거 vs 대체 비교
# 목표
# 같은 데이터에 제거와 대체를 적용해 결과 비교
import pandas as pd

df_imp_2 = pd.read_csv("data/15_02_Injection_Molding_process.csv", encoding="utf-8")

# 단계
# · 결측 심한 컬럼을 먼저 뺀 기준 데이터 만들기
print(df_imp_2.isna().sum())
# 최대사출속도    109
# 감압시간      109

standard = df_imp_2.drop(columns=["최대사출속도", "감압시간"])
standard.info()  # 컬럼 제거 확인
print(standard.shape)  # (250, 20)

# · 기준 데이터에서 결측 행을 삭제한 제거 버전 만들기
remove = standard.dropna()
print(remove.shape)  # (110, 20)


# · 기준 데이터의 결측을 중앙값으로 채운 대체 버전 만들기
alterna = standard.fillna(standard.median(numeric_only=True))
print(alterna.shape) # (250, 20)


# 예상 결과
# 제거 버전 110행, 대체 버전 250행(모두 유지)
