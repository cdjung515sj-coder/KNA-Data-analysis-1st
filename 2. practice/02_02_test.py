print("=== 실습 1 - 여러 자료형 변수 ===")
count = 5
temp = 9.8
name = "Park Min Ho"
is_ok = True
print(count, ",", temp, ",", name, ",", is_ok)
print("\n")

print("=== 실습 2 - type()으로 자료형 확인하기 ===")
print(count, ":", type(count))
print(temp, ":", type(temp))
print(name, ":", type(name))
print(is_ok, ":", type(is_ok))
print("\n")

print("=== 실습 3 - 자료형 맞히기 퀴즈 ===")
# 100은 int
# 100.0은 float
# "100"은 string
# 채점해보자
print(type(100))
print(type(100.0))
print(type("100"))
print("\n")

print("=== 실습 4 - 문자열 숫자와 숫자 비교하기 ===")
print(10 + 8)
print("3" + "5")
print("88" + "99")
print("\n")

print("=== 실습 5 - bool 값 만들어 확인하기 ===")
# 1단계: 3이 2보다 큰가?: 크니까 True
print(bool(3 > 2))
print(bool(5 == 5))
print(type(5 == 5))

print("=== 실습 6 – 변수의 자료형 변경하기 ===")
integer = 45
print(type(integer))
integer = 45.7
print(type(integer))
print("\n")

print("=== 실습 7 - 직접 자료형 표현하기 ===")
device_temp = 70.0
check_count = 5
device_name = "Mealing Machine"
is_normal = False