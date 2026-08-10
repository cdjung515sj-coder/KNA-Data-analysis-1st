import numpy as np

# 형변환(astype)
# 예를들어 아래의 float 들로 가득한 배열이 있다면,
convertable = np.array([3.14, 7.6, 1.24])
print(convertable.dtype)  # float64

# int 들로 가득한 배열로 알아서 바꿔줌
converted = convertable.astype(int)
print(converted)  # [3 7 1]
print(converted.dtype)  # int64
# 실수를 정수로 바꾸면 소수점 아래를 버림 (1.9 → 1)
# 원본은 그대로, 새 배열이 생김 — 결과를 새 이름에 담기
