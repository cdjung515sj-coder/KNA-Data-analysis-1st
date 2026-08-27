# 실습 9. SECOM·AI4I 종합 처리
# 목표
# 제거와 대체를 조합해 전체 결측을 처리하고 저장
import pandas as pd

df_imp_2 = pd.read_csv("data/15_02_Injection_Molding_process.csv", encoding="utf-8")

# 단계
# · 결측 비율 높은 컬럼을 제거하고 나머지는 중앙값으로 채우기
standard = df_imp_2.drop(columns=["최대사출속도", "감압시간"])
remove = standard.dropna()
alterna = standard.fillna(standard.median(numeric_only=True))
print(alterna.isna().sum().sum())

# · 처리 후 남은 결측과 크기를 확인하고 파일로 저장
alterna.to_csv(
    "data/15_02_Injection_Molding_process_alterna.csv", index=False, encoding="utf-8"
)

# · 같은 절차를 AI4I 데이터에도 반복해 결측 0 확인
df_imp_2_ai4i = pd.read_csv(
    "data/15_02_Injection_Molding_process_alterna.csv", encoding="utf-8"
)
print(df_imp_2_ai4i.isna().sum().sum())

# 예상 결과
# SECOM 결측 0·저장, AI4I 결측 0
