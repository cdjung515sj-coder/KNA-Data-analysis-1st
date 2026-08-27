# 실습 4. 평균·중앙값으로 이상치 영향 확인
# 목표
# 이상치가 평균을 끌어당기는 정도를 중앙값과 비교
import pandas as pd

df_diecasting = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# 단계
# · 사이클타임의 평균과 중앙값을 각각 구해 차이 확인 -> mean , median
mean = df_diecasting["사이클타임"].mean()
median = df_diecasting["사이클타임"].median()
print(f"평균 : {mean} , 중앙값 : {median}")  # 평균 : 64.75 , 중앙값 : 22.6

# · 상태가 정상인 행만 조건으로 골라내기 (상태가 0이면 정상 , 1이면 비정상)
df_ok = df_diecasting[df_diecasting["상태"] == 0]

# · 정상만의 평균이 중앙값에 가까워지는지 확인 (정상만의 평균을 출력해서 전체의 중앙갑과 비교)
print(f"정상만의 평균 : {df_ok['사이클타임'].mean().round(2)}")  # 정상만의 평균 : 27.67

# 예상 결과
# 평균 64.75 vs 중앙값 22.6, 정상만 평균 27.67
# 정상 평균과 전체 평균과 다름 그러나 중앙값과 정상만의 평균이 비슷함을 알 수 있음
# 평균과 중앙값을 비교하면 정상만의 평균이 중앙값에 가까워지는지 확인할 수 있음
