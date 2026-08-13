# 열 이름 확인

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

print(df.columns)
# Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급'], dtype='str')
