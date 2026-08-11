import numpy as np

# 비교 연산과 불리언 배열

v = np.array([70, 95, 71, 88, 73])
print(v > 85)  # [False  True False  True False]

# Boolean indexing
# 불리언 배열로 조건에 맞는 값만 골라내기
print(v[v > 85])  # [95 88]

# np.where
# 조건에 따라 값을 둘 중 하나로 바꾸기
# - 조건/참/거짓 ... 3가지 인자
# 조건이 참이면 1(위험) / 거짓이면 0(정상)
print(np.where(v > 85, 1, 0))  # [0 1 0 1 0]

# 다중 조건 결합
print(v)  # [70 95 71 88 73]
v_step1 = v[v > 70]
print(v_step1)  # [95 71 88 73]
v_step2 = v_step1[v_step1 < 90]
print(v_step2)  # [71 88 73]

v_mixed = v[(v > 70) & (v < 90)]
print((v_mixed))  # [71 88 73]
