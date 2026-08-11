import numpy as np

# 합계와 평균(mean)
s = np.array([70, 72, 71, 95, 73])
print(f" 합계 : {s.sum()}")
print(f" 평균 : {s.mean()}")
# 평균의 약점은 크거나 작은 값(이상치)에 휘둘림
print(f"중앙값 : {np.median(s)}")
# 이상치에 흔들리지 않은 강점이 있음 하지만 중앙값과 평균이 다르면 이상치가 있다는 것임

# 최대/최소 범위

print(f"최대값 : {s.max()}")
print(f"최소값 : {s.min()}")
# 하나의 극단 값이 있을 수 있기 때문에 평균과 표준편차와 함께 봐야함
# 정상 범위를 넘은 최댓값 = 위험했던 순간의 신호임
# 단 하나의 극단값이라 전체 판단에는 부족하다는 약점
print(f"범위(R) : {s.max() - s.min()}")

# 분산
stables = np.array([70, 71, 70, 72, 71])
unstables = np.array([60, 85, 65, 95, 70])

print("stables 분산 값: ", stables.var())
print(round(stables.var(), 2))

print("unstables 분산 값: ", unstables.var())
print(round(unstables.var(), 2))


# 표준편차
print("--")
s2 = np.array([70, 71, 70, 72, 71])
print(round(s2.var(), 2))
print(round(s2.std(), 2))

# axis 개념 (행과 열의 방향)
mat = np.array([[70, 2.1], [72, 2.3]])

print(mat.mean())  # 36.6
# 열별(센서별) 평균
print(mat.mean(axis=0))  # [71.   2.2]
# 행별(시점별) 평균
print(mat.mean(axis=1))  # [36.05 37.15]
