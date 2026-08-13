# 실습 2. head·tail 행 개수 조절
# 숫자 인자를 바꿔가며 원하는 만큼 보는 감각 익히기
# GOAL : 숫자 인자를 바꿔가며 원하는 만큼 보는 감각 익히기
# 실습 과제
# 설비 센서 데이터
# 12_metro_compressor.csv로 연습
# STEP 1
# head(1) · head(10) · tail(7) · head(500) 출력 비교

import pandas as pd

df = pd.read_csv("data/12_metro_compressor.csv")

print(df.shape)  # (200, 7)
print("상위 1개 행", df.head(1))
print("상위 10개 행", df.head(10))
print("하위 7개 행", df.tail(7))
print("상위 500개 행", df.head(500))  # [200 rows x 7 columns]

# 1. head(1)과 head(10)의 출력 줄 수 차이 확인
# head(1)은 상위 1줄, head(10)은 상위 10줄이 출력됨

# 2. 데이터보다 큰 숫자를 넣어의 오류 안 나는지 확인
""" 오류가 발생하지 않음 """
# 전체 데이터 행 수는 200개(shape: (200, 7))이지만 head(500)처럼 더 큰 숫자를 입력해도 판다스는 에러를 내지 않고, 가지고 있는 최대 데이터 수(200행)까지만 안전하게 출력하기 때문

# 3. 앞 3줄과 뒤 3줄을 보려면 어떤 명령 두 개가 필요한지
print(df.head(3))
print(df.tail(3))

