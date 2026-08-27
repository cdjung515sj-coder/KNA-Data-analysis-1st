# 실습 7. 빈도와 그룹 집계 종합
# 목표
# 빈도 집계와 그룹 집계를 한 흐름으로 연결해 분석
import pandas as pd

df_hydraulic = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df_hydraulic.info()

# 단계
# · value_counts로 설비 구성과 정상·고장 비율 파악
# 밸브상태별로 비율 확인 - 일단 각 상태별로 몇 건이 있는지 확인
# group-size와 다르게 여기는 counts라서 결측(null값) 무시
print(df_hydraulic["밸브상태"].value_counts())
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19

print(df_hydraulic["밸브상태"].value_counts(normalize=True).round(3))
# 밸브상태
# 정상    0.508
# 지연    0.167
# 경미    0.167
# 심각    0.158

# · 고장 행만 걸러 라인별 고장 건수 집계
# 다음 3가지 방법의 차이점은 잘 파악할 것
df_bad = df_hydraulic[df_hydraulic["result"] == "고장"]
print(len(df_bad))  # 고장 53

print(df_hydraulic.groupby("result").size())  # 이거는 고장 행만 걸러 라인별 건수 집계
# result
# 고장    53
# 정상    67

print(df_hydraulic["result"].value_counts())  # 고장 행만 걸러 라인별 고장 건수 집계
# result
# 정상    67
# 고장    53


# · groupby로 설비별 온도·진동 평균까지 비교
print(
    f"=== 냉각기 온도,진동 평균 === \n {df_hydraulic.groupby("냉각기상태")[["온도", "진동"]].mean().round(2)}"
)
#           온도    진동
# 냉각기상태
# 고장     54.67  0.69
# 저하     45.46  0.61
# 정상     35.89  0.55

print(
    f"=== 운전부하 온도,진동 평균 === \n {df_hydraulic.groupby("운전부하")[["온도", "진동"]].mean().round(2)}"
)
#           온도    진동
# 운전부하
# 고부하   41.85  0.60
# 저부하   48.82  0.63

print(
    f"=== 밸브상태 온도,진동 평균 === \n {df_hydraulic.groupby("밸브상태")[["온도", "진동"]].mean().round(2)}"
)
#           온도    진동
# 밸브상태
# 경미    44.86  0.62
# 심각    46.02  0.63
# 정상    45.11  0.61
# 지연    45.86  0.62

# 예상 결과
# 구성·비율·라인별 고장 건수·설비별 평균 출력
