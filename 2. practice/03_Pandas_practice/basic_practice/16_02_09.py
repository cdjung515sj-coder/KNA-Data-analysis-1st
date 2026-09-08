# 실습 9. reset_index로 인덱스 정리
# 목표
# 중복 제거로 생긴 인덱스 구멍을 0부터 다시 매기기
# 단계

import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# · drop_duplicates로 중복을 제거
df_clean = df.drop_duplicates()

# · reset_index로 인덱스를 0부터 다시 매기기
df_clean_idxreset = df_clean.reset_index(drop=True)

print(df_clean.index.min(), df_clean.index.max())
print(len(df_clean))

print(df_clean_idxreset.index.min(), df_clean_idxreset.index.max())
print(len(df_clean_idxreset))

# · 인덱스 최솟값·최댓값으로 연속성 확인
min_idx = df_clean_idxreset.index.min()
max_idx = df_clean_idxreset.index.max()
total_rows = len(df_clean_idxreset)
print(f"인덱스 {min_idx}~{max_idx}로 연속, 최종 {total_rows}행")

# 예상 결과
# 인덱스 0~199로 연속, 최종 200행
