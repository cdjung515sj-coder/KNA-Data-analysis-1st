# 실습 4. groupby로 그룹 집계
# 기준 → 열 → 함수 순으로 그룹별 통계 구하기
# 기준 열로 그룹을 나눠 그룹별 통계 구하기
import pandas as pd

df_hydraulic = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df_hydraulic.info()

# · 라인으로 그룹을 나눠 압력 열의 평균 집계
# 냉각기상태별 압력 평균
print(df_hydraulic.groupby("냉각기상태")["압력"].mean().round(2))
# 냉각기상태
# 고장    163.68
# 저하    158.49
# 정상    160.84

# · 집계 함수를 바꿔 설비별 최고 온도 확인 - max, min
# 벨브상태별로 최고 온도
print(f"밸브상태 최고 온도 : {df_hydraulic.groupby("밸브상태")["온도"].max()}")
# 밸브상태
# 경미    57.1
# 심각    57.6
# 정상    57.8
# 지연    57.5
print(f"밸브상태 최저 온도 :{df_hydraulic.groupby("밸브상태")["온도"].min()}")

print(f"운전부하 최고 온도 : {df_hydraulic.groupby("운전부하")["온도"].max()}")
print(f"운전부하 최저 온도 : {df_hydraulic.groupby("운전부하")["온도"].min()}")


# · size로 교대별 측정 건수까지 확인
# 운전부하별로 size로 갯수 세기 (결측-null값 갯수도 포함)
print(df_hydraulic.groupby("운전부하").size())
# 운전부하
# 고부하    60
# 저부하    60

# 예상 결과
# 라인별 평균 압력·설비별 최고 온도·교대별 건수 출력
