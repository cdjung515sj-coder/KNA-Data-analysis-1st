# 실습2. 표준 라이브러리로 센서값 만들기
import random

random_count = random.randint(1, 10)
print(random_count)

import math

random_sqrt = math.sqrt(random.randint(1, 10))
print(f"랜덤 수 :{random_count}, 제곱근 값 :{random_sqrt:.2f}")
