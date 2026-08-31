# reshape로 형태 바꾸기
# size로 확인되는 값 개수는 같아야 함 ⭐⭐⭐

import numpy as np

under_ten = np.arange(10)
print(under_ten)
print("ndim : ", under_ten.ndim)
print("shape : ", under_ten.shape)
print("size : ", under_ten.size)

reshape_ten = under_ten.reshape(2, 5)
print(reshape_ten)
# [[0 1 2 3 4]
# [5 6 7 8 9]]

print("ndim : ", reshape_ten.ndim)
print("shape : ", reshape_ten.shape)
print("size : ", reshape_ten.size)


# flatten으로 1차원 만들기
flatten_ten = reshape_ten.flatten()
print(flatten_ten)  # [0 1 2 3 4 5 6 7 8 9]
