import numpy as np


print("------ np.zeros() -------")
# np.zeros() : 0으로 채우기

block_zeros = np.zeros(5)
print(block_zeros)  # [0. 0. 0. 0. 0.]


print("----- np.full(개수, 채울값) -------")
# np.full() : 원하는 지정 값으로 채우기
# np.full(개수, 채울값)
# 7으로 채우기
block_seven = np.full(4, 7)
print(block_seven)  #  [7 7 7 7]

# 명시적으로 7.0처럼 float값을 지정해줘야
# float 타입 값으로 채워지는 배열이 만들어진다.
block_seven = np.full(4, 7.0)
print(block_seven)  #  [7. 7. 7. 7.]


print("------- np.ones() --------")
# np.ones() : 1로 채우기

# 1차원 배열 (원소 3개)
o1 = np.ones(3)
print(o1)
# 출력: [1. 1. 1.]

# 2차원 배열 (3행 2열)
o2 = np.ones((3, 2))
print(o2)
# 출력:
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]