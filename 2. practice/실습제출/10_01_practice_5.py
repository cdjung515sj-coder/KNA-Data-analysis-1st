# 실습 5. 자료형 확인과 변환하기

import numpy as np

data = np.array([12334.232, 14543252345.23, 325345.243])

# dtype으로 현재 자료형 확인하기
print(data.dtype)

# astype으로 정수형으로 변환한 새 배열 출력
converted_data = data.astype(int)
print(converted_data)  #


# ===================================================

data = np.array([12.3333, 5114.4444, 1341.5555])

print(data.dtype)  # float64

converted_data = data.astype(int)
print(converted_data)  # [  12 5114 1341]
