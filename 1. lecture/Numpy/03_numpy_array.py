# 파이썬의 리스트로부터 NumPy 배열 만들기
# np.array

import numpy as np

temp = np.array([70.5, 69.8, 73.7])

print(temp)  # [70.5 69.8 73.7] 배열이기 떄문에, 항목 사이에 콤마 없음 유의

# 배열의 항목들마다 +5씩 더하려면?
# 리스트였다면 for문으로 돌려서 항목마다 직접 처리해줘야했음
# BUT, NumPy라면

print(temp + 5)  # [75.5 74.8 78.7]

# 소숫점 이하가 없는 숫자 타입들로 가득찬 배열
print(np.array([1, 2, 3, 4, 5]))  # [1 2 3 4 5]

# 소숫점 이하가 있는 숫자 타입들로 가득찬 배열
print(np.array([3.14, 6.7, 7.67]))  # [3.14 6.7  7.67]

# 소숫점 이하가 o/x 섞인 경우?
# 모두 소숫점 이하가 있는 것으로 배열 생성
print(np.array([1, 3, 5, 3.14, 7.6, 4]))  # [1.   3.   5.   3.14 7.6  4.  ]


# 0 ~ 3까지 생성 ( 5는 제외 됨)
import numpy as np

under_five = np.arange(5)
print(under_five)  # [0 1 2 3 4]

# 0 ~ 8까지 2간격 ( 8보다 큰 숫자가 만들어지면 덧붙이지 않고 끝)
gab_two = np.arange(0, 9, 2)
print(gab_two)  # [0 2 4 6 8]
