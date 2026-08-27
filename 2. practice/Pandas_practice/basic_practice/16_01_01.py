# 실습 1. 주조 데이터 구조·분포 살펴보기
# 목표
# 주조 데이터를 불러와 크기·컬럼·자료형을 확인
import pandas as pd

df_diecasting = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# 단계
# · read_csv로 데이터를 불러와 head로 앞부분 확인
print(df_diecasting.head(3))

# · shape와 columns로 크기와 컬럼 이름 확인
print(df_diecasting)
print(df_diecasting)

# · info로 자료형과 결측 여부 훑기
df_diecasting.info()

# 예상 결과
# 202행 7열, 실린더압력·사이클타임 등 컬럼 확인
