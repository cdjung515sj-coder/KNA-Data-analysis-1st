# 1차원 인덱싱 - 번호로 값 꺼내기

# 배열의 인덱스 번호는 파이썬 리스트처럼 0부터 시작

import numpy as np

temp = np.array([70, 72, 71, 95, 73])
print(temp)

# 첫번째 내용만 콕찝어 보여주기
print(temp[0])

# 앞으로 쭉 돌아서 뒤끝 내용 보여주기
print(temp[-1])
