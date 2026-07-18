# 실습 01 - 사칙연산 계산기
def calculator(a, b):
    return a + b, a - b, a * b, a / b, a // b, a % b


print(calculator(10, 4))


# 실습 02 - 평균과 도형 계산 / 응용
width = 80
height = 91
depth = 100
print("평균:", (width + height + depth) / 3)

print("width와 height를 길이로 가지는 사각형의 넓이:", width * height)

print("부피:", width * height * depth)


# 실습 03 비교 연산 출력
print("실습 03 비교 연산 출력")
Temperature1 = 36.5
Temperature2 = 36.5

print(Temperature1 == Temperature2)  # True
print(
    Temperature1 == str(Temperature2)
)  # == 연산자는 서로 다른 데이터 타입끼리 비교해도 TypeError를 발생시키지 않고, 그냥 False를 반환하도록 파이썬 언어가 설계되어 있음

print(bool(Temperature1 > Temperature2))  # 초과하지 않기 때문에 False + bool
print(Temperature1 >= Temperature2)  # True
print(Temperature1 <= Temperature2)  # True
print(Temperature1 != Temperature2)  # False
print(not Temperature1 != Temperature2)  # True

# print(Temperature1 >= str(Temperature2))  # TypeError: '>=' not supported between instances of 'float' and 'str'

# 실습 04 정상범위 다중센서 판정 / 실전
print("\n실습 04 정상범위 / 다중센서 판정 / 실전")
temperature = 85
pressure = 5

check_temp = bool(temperature > 60 and temperature < 90)
check_pres = bool(pressure > 3 and pressure < 7)
check_both = bool(check_temp and check_pres)
print(
    "온도 정상", check_temp, "|", "압력 정상", "|", check_pres, "모두 정상:", check_both
)

print("\n 실습 5복합 할당으로 재고 추적 / 기초")
stock = 100
print(stock)
stock += 50
print(stock)
stock -= 30
print(stock)
stock += 5
print(stock)

print("\n 실습 6 설비 지표 계산 / 실전")
q = 500
err = 23
err_rate = 23 / 500

oper = 21
total_oper = 24
oper_rate = 21 / 24

print("불량률:", err_rate, "|", "가동률:", oper_rate)


print("\n시간 변환, 상자 포장, 도전")
min_total = 500
convert_hour = 500 // 60
convert_min = 500 % 60
print(f"{convert_hour}시간 {convert_min}분")