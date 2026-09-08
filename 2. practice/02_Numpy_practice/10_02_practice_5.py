# 실습 5. 조건별 개수와 비율 세기
# 조건을 만족하는 값의 개수와 전체 대비 비율 계산
# 토크 배열 준비

import numpy as np

# 토크 배열 준비
torque5 = np.array([42.8, 46.3, 49.4, 4.6, 41.9, 65.7, 40.2, 60.7])

# 비교 조건으로 참 거짓 불리언 배열 생성
high5 = torque5 > 50  # 문제에서 요구하는 코드
print(high5)  # [False False False False False  True False  True]

print(torque5[torque5 > 50])  # 참고 코드 [65.7 60.7]

# 불리언 배열의 합으로 개수, 평균으로 비율 계산
print(high5.sum())  # 2 (True 개수) (True = 1, False = 0으로 합산)
print(high5.mean())  # 0.25
print(round(high5.mean(), 1))  # 0.2, 소수점 이하 2자리까지 나오도록 처리

# 예상 결과
# 조건을 만족하는 값으 개수와 비율이 출력

temp = np.array([11.123521, 325.151513, 133.2341])
print(np.round(temp, 2))  # [ 11.12 325.15 133.23]

# ----------------------------------------------------------------------

torque = np.array([42.8, 26.3, 49.4, 4.6, 41.9, 65.7, 12.5, 55.0])

torque_over_40 = torque >= 40.0
print(torque_over_40)

over_sum = torque_over_40.sum()
over_mean = torque_over_40.mean()

print(over_sum)
print(over_mean)


print(f"전체 토크 데이터 : {torque}")
print(f"조건 만족 여부   : {torque_over_40}개")
print(f"40 이상인 데이터 개수 : {over_sum}개")
print(np.round(torque, 2))
