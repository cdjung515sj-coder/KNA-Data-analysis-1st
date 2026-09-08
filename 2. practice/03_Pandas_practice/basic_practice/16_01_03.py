# 실습 3. 정렬해서 이상치 후보 찾기
# 목표
# 정렬해 양 끝의 동떨어진 값을 후보로 찾고 분류
import pandas as pd

df_diecasting = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# 단계
# · 사이클타임 열을 기준으로 내림차순 정렬
s_sorted = df_diecasting.sort_values("사이클타임", ascending=False)

# · 위쪽 끝에서 동떨어진 큰 값 찾기
print(s_sorted.head())  # 6170.0, 652.3

# · 각 후보를 정상 상태와 이상 상태로 나누기



# 예상 결과
# 6170·652초 등 설비 잼 후보, 정상은 20~35초
