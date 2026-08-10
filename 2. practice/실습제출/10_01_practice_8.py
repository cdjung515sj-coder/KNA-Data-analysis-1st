# 실습 8. 배열 생성부터 정리까지
import numpy as np

# [최종결과]
# 형태와 자료형 확인 후 3행 2열 표로 정리된 배열 출력
# 최종형태 shape : (3,2)
# 최종형태 size  : 3*4 = 6

# · 센서 측정값을 np.array로 배열 생성
data = np.array([4.5, 3.2, 1.8, 9.8, 5.5, 7.6])

# · shape과 dtype으로 구조 확인
print(f"shape : {data.shape}")
print(f"dtype : {data.dtype}")

# · reshape으로 분석용 표 형태로 정리한 뒤 출력
converted = data.reshape(3, 2)
print(converted)

# [[4.5 3.2]
#  [1.8 9.8]
#  [5.5 7.6]]

# ---------------------------------------------------

data = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])

# · shape과 dtype으로 구조 확인
print(f"shape : {data.shape}")  # shape : (9,)
print(f"dtype : {data.dtype}")  # dtype : float64

# · reshape으로 분석용 표 형태로 정리한 뒤 출력
converted = data.reshape(3, 3)
print(converted)

# [[1.1 2.2 3.3]
#  [4.4 5.5 6.6]
#  [7.7 8.8 9.9]]
