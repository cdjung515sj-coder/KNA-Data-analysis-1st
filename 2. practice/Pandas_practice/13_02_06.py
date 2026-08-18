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
print(
    df_shot[df_shot["품질등급"] == "불량"]
    .sort_values("비스킷두께", ascending=False)
    .head(5)
)

# 예상 결과
# 5개 행, 비스킷두께 큰 순 샷 목록 출력


# =============================================================================

import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")
df.info()
print(df.tail())


# · 고장 여부 조건으로 고장 설비만 먼저 거르기
df_bad = df[df["품질등급"] == "불량"]
print(len(df_bad))
print(df_bad.head())

# · 거른 결과에 sort_values를 점으로 이어 비스킷두께 내림차순 정렬
# · head로 상위 다섯 개만 남겨 샷 확인
df_filterd = (
    df[df["품질등급"] == "불량"].sort_values("비스킷두께", ascending=False).head()
)
print(df_filterd)


# 샷  실린더압력   주조압력  사이클타임  비스킷두께    형체력 품질등급
# 197  198  113.0  255.0   36.6   27.0  354.0   불량
# 191  192  113.0  255.0   36.9   26.0  366.0   불량
# 196  197  265.0  595.0   36.2   20.0  355.0   불량
# 193  194  113.0  255.0   34.4   19.0  370.0   불량
# 198  199  264.0  595.0   36.1   19.0  372.0   불량

print(df_filterd["비스킷두께"].tolist())
# [27.0, 26.0, 20.0, 19.0, 19.0]


