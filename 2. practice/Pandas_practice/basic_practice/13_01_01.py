# 실습 1. 데이터 불러오기와 구조 확인

import pandas as pd

df_diecasting_small = pd.read_csv("data/13_diecasting_small.csv")

print(df_diecasting_small.head())
# shape 확인
print(df_diecasting_small.shape)  # (30, 7)

# columns의 열 이름 출력 확인
print(df_diecasting_small.columns)
# Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급'], dtype='str')

# 실제 CSV 파일 열어보고 shape, columns 그대로 나온건지 비교
""" 실제 파일과 같은 값 출력 확인"""

