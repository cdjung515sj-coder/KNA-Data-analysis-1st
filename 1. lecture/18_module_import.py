# 수학 관련 모듈을 불러옵니다
import math

# 해당 모듈이름.함수() 이런 식으로 호출해야함
result = math.sqrt(16)
print(result)

# =========================================================

# 수학 관련 모듈에서 sqrt 기능만 불러오기
from math import sqrt

# 이젠 sqrt만 불러도 됨
result = sqrt(16)
print(result)


