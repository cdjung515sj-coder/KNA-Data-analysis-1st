# 실습 5. 경로,옵션 오류 고치기
# 오류 메시지를 읽고 스스로 원인을 찾아 고치기

# data/ 누락, 철자, .csv 누락- 세 종류의 FileNotFoundError

import pandas as pd

df = pd.read_csv("아무거나내주세요.csv")
print(df.shape)  # ModuleNotFoundError: No module named 'pandas'
