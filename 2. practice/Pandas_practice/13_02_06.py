# 실습 6. 필터링과 정렬 연결
# 목표
# 조건으로 거른 결과에 정렬을 이어 붙이기

import pandas as pd

df_shot = pd.read_csv("data/13_diecasting_shot.csv")

df_shot.info()
# 단계
# · 고장 여부 조건으로 고장 설비만 먼저 거르기
# 품질등급 컬럼 == 불량
df_filterd = df_shot[df_shot["품질등급"] == "불량"]
print(df_filterd.head())
# · 거른 결과에 sort_values를 점으로 이어 비스킷두께 내림차순 정렬

df_sorted_after_filtered = df_shot[df_shot["품질등급"] == "불량"].sort_values(
    "비스킷두께", ascending=False
)

# · head로 상위 다섯 개만 남겨 샷 확인
print(df_shot[df_shot["품질등급"] == "불량"].sort_values("비스킷두께", ascending=False).head(5))

# 예상 결과
# 5개 행, 비스킷두께 큰 순 샷 목록 출력
