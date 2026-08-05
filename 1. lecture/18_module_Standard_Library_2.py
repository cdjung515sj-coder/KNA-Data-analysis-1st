# 표준 라이브러리의 math 모듈
import math

print(math.sqrt(9))  # 제곱근값
print(math.ceil(4.2))  # 올림값
print(2**3)  # 2의 2승 = 2 * 2 * 2 = 8 math와 무관

# math에서 sqrt, ceil 두개만 사용한다면 이렇게 써도 됩니다.
from math import sqrt, ceil

print(sqrt(9))

print("=" * 20)
# ==============================================================

# 표준 라이브러리의 random 모듈
import random

print(random.randint(1, 10))  # 1~10 중 무작위 정수
print(random.choice(["정상", "경고", "위험"]))

print("=" * 20)
# ==============================================================

# 표준 라이브러리의 datetime 모듈
import datetime

# datetime 모듈 안의 datetime 클래스에서 지원하는 now() 함수 호출
now = datetime.datetime.now()
print(now)  # 2026-08-05 13:19:26.523858

print("=" * 20)
# ==============================================================
# 모듈 도움말 보기 : 참고만 하고 구글링한 웹사이트에서 보자!
# print(dir(math))
# print(help(math.sqrt))


print("=" * 20)
# ==============================================================

