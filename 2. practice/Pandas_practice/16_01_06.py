# 실습 6. describe로 격차 큰 컬럼 찾기
# 목표
# describe 표에서 이상치 의심 컬럼을 찾아 해석
import pandas as pd

df_diecasting = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# 단계
# · 여러 공정 컬럼을 describe로 요약
print(df_diecasting.describe())

# · 요약을 컬럼별로 정리하고 평균과 중앙값 격차 계산
report = (
    df_diecasting[["샷", "실린더압력", "주조압력", "사이클타임", "비스킷두께", "형체력"]]
    .describe()
    .T
)
print(report)
# .T -> describe 결과의 axis를 바꿔줌

# · 격차가 큰 순으로 정렬해 이상치 의심 컬럼 확인
# -> 격차라는 새로운 컬럼을 추가해서 계산 결과들 확인 : 새로운 컬럼이름을 언급하면 추가 됨
# => 격차 결과 순서로 정렬
report["격차"] = (report["mean"] - report["50%"]).abs()
print(report.head())
print(
    report.sort_values("격차", ascending=False)[["mean", "50%", "max", "격차"]].head()
)

# 예상 결과
# 주조압력·형체력·사이클타임 등 격차 큰 컬럼 확인
