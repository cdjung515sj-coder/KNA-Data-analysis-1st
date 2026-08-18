# 실습 5. 위험 순으로 정렬하기
# 목표
# 데이터를 위험한 순서로 정렬하고 상위만 추출

import pandas as pd

df_shot = pd.read_csv("data/13_diecasting_shot.csv")
df_shot.info()

# 단계
df_sorted = df_shot.sort_values("비스킷두께")  # 기본 배열

# · sort_values로 비스킷두께를 큰 값부터 내림차순 정렬
df_sorted = df_shot.sort_values("비스킷두께", ascending=False)

# · head로 상위 다섯 개만 추출해 값 확인
print(df_sorted.head(5))

# 직접 해당 값들만 뽑아서 list로 출력해보려면?
print(df_sorted["비스킷두께"].head(5).tolist())


# · 여러 열을 리스트로 묶어 우선순위 다중 정렬
# 품질등급을 우선 오름차순으로 정렬하고 형체력을 그 다음 순서로 내림차순 정렬하기
df_multisorted = df_shot.sort_values(["품질등급", "형체력"], ascending=[True, False])
# 예상 결과
# 상위 5개 비스킷두께 값과 다중 정렬 첫 행 품질등급 출력
print(df_multisorted.head(5))


# ---------------------------------------------------------


import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")
print(df.shape)
df.info()
print(df.head(3))

# · sort_values로 비스킷두께를 큰 값부터 내림차순 정렬
# · head로 상위 다섯 개만 추출해 값 확인
print(df.sort_values("비스킷두께", ascending=False).head())


# · 여러 열을 리스트로 묶어 우선순위 다중 정렬
df_multi = df.sort_values(["품질등급", "형체력"], ascending=[True, False])
print(df_multi.head())
# 품질등급은 True 오름차순(불량 → 양품 → 주의) / 형체력은 False로 내림차순 정렬
# 품질등급을 오름차순으로 정렬
# 그 결과 불량 그룹이 앞쪽에 배치됨
# 불량 그룹 안에서는 형체력을 큰 값 → 작은 값으로 정렬
# head()로 위에서 5개만 출력

# 예상 결과
# 상위 5개 비스킷두께 값과 다중 정렬 첫 행 품질등급 출력
