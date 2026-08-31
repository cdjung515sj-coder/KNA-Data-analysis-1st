import numpy as np

# 배열의 산술 연산
# 두 배열을 같은 위치끼리 한 번에 계산

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(x + y)
print(x * y)
print(x * 2)

# 요소별 연산의 조건 : 같은 위치 값 끼리 계산되며, 두 배열의 크기가 같아야만 계산가능

# << 스칼라 연산 >>
# 배열 안의 섭씨 온도들을 화씨 온도로 바꿔 출력하기
celsius = np.array([20.0, 25.0, 30.0])
fahrenheit = celsius * 18 + 32

print(f"섭씨(℃) = {celsius} ℃")
print(f"화씨(F) = {fahrenheit} F")

# 스칼라 연산은 위 처럼 배열 전체에 항목마다 계산시켜 다시 새로운 배열 만들기

# 브로드 캐스팅
# 한 줄짜리 기준값이 모든 행에 퍼져서 계산
table = np.array([[72, 2.3], [95, 6.8]])

base = np.array([70, 2.0])

# table의 각 행에서 기준값(base)을 뺴기
print(table - base)
