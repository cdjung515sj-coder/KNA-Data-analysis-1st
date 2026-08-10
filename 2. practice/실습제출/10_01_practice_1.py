# 미국식 속도 (miles)를 우리가 쓰는 속도(km)로 변환시켜주는 NumPy 배열 예제 코드

# import numpy as np

# miles = np.array([94.7, 104.5, 105.5])

# # 속도(km/h) = 속도(mph) * 1.609
# print(miles * 1.609)

# 실습 1. 센서값 배열 만들기

import numpy as np

celsius = np.array([0.0, 10.1, 25.5, 100.0])
f_array = celsius * 1.8 + 32
# 화씨(F) = 섭씨(C) * 1.8 + 32

# 3. 변환된 배열 출력
print("섭씨 배열:", celsius)
print("화씨 배열:", f_array)
