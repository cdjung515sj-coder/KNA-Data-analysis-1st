# 실습 3. 구조 파악 3종 도구
# shape · columns · dtypes로 데이터 뼈대 읽기
# GOAL
# shape · columns · dtypes로 데이터 뼈대 읽기
# 실습 과제
# metro_digital_sample.csv
# 25열, 결측 많음
# STEP 1
# shape · columns · dtypes로 크기·열·자료형 파악 후 한 문장 정리

import pandas as pd

# 데이터 로드
df_digital = pd.read_csv("data/12_metro_digital.csv")

# 1. 크기 (shape)
print("=== 1. 데이터 크기 (shape) ===")
print(df_digital.shape)

# 2. 열 이름 (columns)
print("\n=== 2. 열 목록 (columns) ===")
print(df_digital.columns)

# 3. 자료형 (dtypes)
print("\n=== 3. 열별 자료형 (dtypes) ===")
print(df_digital.dtypes)


# 실습 4. 열 이름·자료형 점검
# 자료형이 의도와 맞는지 빠르게 판단
# GOAL
# 자료형이 의도와 맞는지 빠르게 판단
# 실습 과제
# 설비 센서 데이터 점검
# 12_metro_compressor.csv의 자료형 점검
# STEP 1
# dtypes로 숫자·글자 열이 의도와 맞는지 판단

# 설비 센서 데이터 로드
df_comp = pd.read_csv("data/12_metro_compressor.csv")

# 자료형 및 열 이름 확인
print("=== 12_metro_compressor.csv dtypes 점검 ===")
print(df_comp.dtypes)

# 실습 5. info로 데이터 건강검진
# info로 행 수·자료형·결측을 종합 점검하고 진단
# GOAL
# info로 행 수·자료형·결측을 종합 점검하고 진단
# 실습 과제
# 12_metro_digital_sample.csv
# 결측 많음
# STEP 1
# info로 다섯 요소 읽고 결측 개수 계산해 건강 진단

import pandas as pd

# 디지털 샘플 데이터 로드 및 info 실행
df_sample = pd.read_csv("data/12_metro_digital_sample.csv")

print("=== info() 데이터 건강검진 ===")
df_sample.info()
