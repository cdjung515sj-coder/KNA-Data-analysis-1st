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

# =========================================================

# mathㄹ라는 모듈 이름 다 쓰기 귀찮아서 줄이기
import math as emt

# 별칭으로 가져온 모듈 이름을 언급하기
result = emt.sqrt(16)
print(result)


# ========================================================

# detetime 모듈 사용
import datetime

# datetime의 now()는 현재의 지역 날짜와 시간을 반환함
now = datetime.datetime.now()
print(now)  # 2026-08-05 11:20:14.819660

# --------------------------
# 위와 같음
import datetime as dt

# datetime의 now()는 현재의 지역 날짜와 시간을 반환함
now = dt.datetime.now()
print(now)  # 2026-08-05 11:20:14.819660
print(type(now))   # <class 'datetime.datetime'>

