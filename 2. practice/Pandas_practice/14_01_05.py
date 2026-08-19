# 실습 5. 그룹별 평균 비교와 정렬
# 그룹별 평균을 구해 정렬로 두드러진 그룹 찾기
import pandas as pd

df_hydraulic = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df_hydraulic.info()

# · 설비로 그룹을 나눠 진동 평균 집계
# 밸브상태 그룹별로 진동의 평균
print(df_hydraulic.groupby("밸브상태")["진동"].mean().round(3))
# 밸브상태
# 경미    0.617
# 심각    0.629
# 정상    0.609
# 지연    0.621

# · 집계 결과에 정렬을 이어 붙여 내림차순으로 정렬
# 앞선 평균결과에 맞춰서 심각 > 지연 > 경미 > 정상 순서로 출력
print(
    df_hydraulic.groupby("밸브상태")["진동"]
    .mean()
    .round(3)
    .sort_values(ascending=False)
)
# 밸브상태
# 심각    0.629
# 지연    0.621
# 경미    0.617
# 정상    0.609

# · 가장 진동이 큰 설비를 맨 위에서 확인
# 앞선 결과에서 심각 0.629가 맨 윗줄인걸 확인. 끝.
# 심각    0.629 확인 완료 !


# 예상 결과
# 진동 평균이 큰 설비 순 정렬 (정상 최대)
