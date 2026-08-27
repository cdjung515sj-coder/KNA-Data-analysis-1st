# 실습 2. 비율과 불균형 데이터
# 목표
# 합격·불합격 빈도와 비율을 구해 불균형 데이터 확인
import pandas as pd

df_hydraulic_qc = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8")
df_hydraulic_qc.info()
print(df_hydraulic_qc.head())

# 단계
# · 공정 데이터의 판정 열에 value_counts로 합격·불합격 개수 세기
print(df_hydraulic_qc["검사결과"].value_counts())
# 검사결과
# 합격     188
# 불합격     12

# · normalize 옵션으로 각 값의 비율을 소수로 확인
print(df_hydraulic_qc["검사결과"].value_counts(normalize=True))
# 검사결과
# 합격     0.94
# 불합격    0.06

# · round로 비율을 소수점 첫째 자리까지 정리
print(df_hydraulic_qc["검사결과"].value_counts(normalize=True).round(1))
# 검사결과
# 합격     0.9
# 불합격    0.1


# 예상 결과
# 불합격이 전체 약 6%인 불균형 확인
# 불합격    0.06 ==> 6% 불견형 확인 !!
