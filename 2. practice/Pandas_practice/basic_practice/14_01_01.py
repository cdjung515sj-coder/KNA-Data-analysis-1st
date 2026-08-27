# 실습 1. value_counts로 빈도 세기
# 목표
# 한 열의 값별 개수를 세어 데이터 구성 파악

import pandas as pd

df_hydraulic = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df_hydraulic.info()
print(df_hydraulic.head())

# 단계
# · 설비 데이터를 불러와 앞부분과 구조 확인
# · 설비 열(컬럼)에 value_counts를 붙여 값별 개수 세기
print(
    df_hydraulic["밸브상태"].value_counts()
)  # 온도, 진동, 압력 숫자 부분은 넣으면 안됨
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19


# · 교대 열도 같은 방법으로 세어 가장 많은 값 확인
print(df_hydraulic["운전부하"].value_counts())
# 운전부하
# 고부하    60
# 저부하    60

print(df_hydraulic["냉각기상태"].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40

# 예상 결과
# 설비별·교대별 빈도표 출력 (심각 42건이 최다)
