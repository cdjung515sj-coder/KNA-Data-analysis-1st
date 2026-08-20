# 실습 5. 그룹별 통계량 종합

import pandas as pd

df_hydraulic = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df_hydraulic.info()

# 목표
# 전체 통계부터 그룹 진단표까지 한 흐름으로 종합


# 단계
# · 온도 열의 전체 평균과 표준편차로 기준선 파악
print(df_hydraulic["온도"].mean().round(3))  # 전체 평균 : 45.339
print(df_hydraulic["온도"].std().round(3))  # 전체 표준편차 : 8.042


# · 라인별(냉각기) 평균과 중앙값을 함께 구해 치우침 확인
print(df_hydraulic.groupby("냉각기상태")["온도"].agg(["mean", "median"]).round(3))
#          mean  median
# 냉각기상태
# 고장     54.668   55.45
# 저하     45.465   44.90
# 정상     35.885   35.90

print(df_hydraulic.groupby("운전부하")["진동"].agg(["mean", "median"]).round(3))
#        mean  median
# 운전부하
# 고부하   0.602   0.554
# 저부하   0.629   0.617

print(df_hydraulic.groupby("밸브상태")["압력"].agg(["mean", "median"]).round(1))
#        mean  median
# 밸브상태               
# 경미    161.6   159.6
# 심각    163.4   160.5
# 정상    160.0   158.6
# 지연    161.3   160.5

# · 설비 진단표를 온도편차 순으로 정렬해 우선 점검 대상 선정
report = (
    df_hydraulic.groupby("밸브상태")
    .agg(
        평균온도=("온도", "mean"),
        온도편차=("온도", "std"),
        평균진동=("진동", "mean"),
    )
    .round(2)
)

print(report)
#        평균온도  온도편차  평균진동
# 밸브상태
# 경미    44.86  8.11  0.62
# 심각    46.02  8.40  0.63
# 정상    45.11  7.79  0.61
# 지연    45.86  8.93  0.62

# print(report.sort_values("온도편차"))
#        평균온도  온도편차  평균진동
# 밸브상태
# 정상    45.11  7.79  0.61
# 경미    44.86  8.11  0.62
# 심각    46.02  8.40  0.63
# 지연    45.86  8.93  0.62
# 온도 편차가 클수록 점검 대상으로 내림차순으로 정렬해야함

print(report.sort_values("온도편차", ascending=False))


# 예상 결과
# 전체 기준선·라인 치우침·진단표 정렬 결과 출력

#        평균온도  온도편차  평균진동
# 밸브상태
# 지연    45.86  8.93  0.62
# 심각    46.02  8.40  0.63
# 경미    44.86  8.11  0.62
# 정상    45.11  7.79  0.61
