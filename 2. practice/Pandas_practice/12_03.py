# 실습 3. 한글, 구분자 깨짐 옵션 다루기

# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=";"이면

import pandas as pd

df = pd.read_csv("data/12_metro_compressor_semicolon.csv")
print(df.shape)  # (200, 1) 200행 1열
# 왜 여기 1개 밖에 없다고 뜨지? 보통 컬럼이 최소 2개 이상임. 하나만 있다? 이상함을 인지하고 함 봐
# 확인하는 방법은 head로 확인해

print(df.head(4))


# 구분자를 바꿔 보기 쉽게 만들자!
df = pd.read_csv("data/12_metro_compressor_semicolon.csv", sep=";", encoding="utf-8")
print(df.shape)
print(df.head(4))
