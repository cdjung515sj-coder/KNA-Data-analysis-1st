# 실습 7. 센서 데이터 표로 정리하기

import numpy as np

# · 시점과 센서 수를 곱한 개수만큼 연속값을 arange로 생성
# 만약 시점이 오후 3시,
# 오전 3시라면 시점(timestamp)은 ## 2개
# 센서는 ## 5개 있다고 가정
# 시점 * 센서 = 10개
data = np.arange(10)


# · 행을 시점, 열을 센서 수로 정해 reshape로 표 형태 변환
converted_data = data.reshape(2, 5)

# · 정리된 표 배열 출력
print(converted_data)

# [[0 1 2 3 4]
#  [5 6 7 8 9]]

# ----------------------------------------------------

data = np.arange(6)

converted_data = data.reshape(3, 2)

print(converted_data)

# [[0 1]
#  [2 3]
#  [4 5]]
