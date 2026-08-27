# 실습3. 구조 파악 3종

import pandas as pd

df_metro_digital = pd.read_csv("data/12_metro_digital.csv")

print("1. 데이터 크기 (shape):", df_metro_digital.shape)
print("2. 열 목록 (columns):", df_metro_digital.columns)
print("3. 열 개수 확인 (len):", len(df_metro_digital.columns))
print("4. 자료형 (dtypes): ", df_metro_digital.dtypes)

# 3. dtypes에서 숫자 열과 글자 열을 구분했는가
# # - 글자(문자열) 열: dtypes가 'object'로 표시되는 열 (예: 측정시각, 가동상태 등)
# # - 숫자 열: dtypes가 'int64' 또는 'float64'로 표시되는 열 (예: 압축압력, 모터전류 등)
