test1 = "temp_sensor"
print(test1[:4])

test2 = "temp_sensor"
print(test2[0:])

test3 = "sensor_01"
print(test3[-2:])

test4 = "PYTHON"
print(test4[::2])  # PTO
print(test4[::-2])  # NHY 위와 반대로 출력됨⭐

test5 = "PYTHON"
print(test5[::-1])  # -1 뒤에서 앞으로 뛰기때문에 글자가 거꾸로 뒤집힘.

# len()으로 전화번호 길이 재기
number = "01012345678"
print(len(number))

# .count() 개수세기
abcd = "a,b,c,d"
print(abcd.count(","))

# f-string 안에서 계산
a=170
b=183
c=162
print(f"평균{(a+b+c)/3}")


# 소숫점 자릿수 지정하기
rate000 = 87.456
print(f"{rate000:.1f}")
print(f"{rate000:.2f}")
print(f"{rate000:.1f}/{rate000:2f}")