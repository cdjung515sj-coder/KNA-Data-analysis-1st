# 실습 1. 센서를 튜플로 묶고 꺼내기
sensor = (
    "모터온도",
    78,
)

print(sensor)
print(sensor[0])
print(sensor[1])

name, value = sensor
print(name, value)

# 실습 2. 튜플 리스트를 반복 처리하기
sensors = [
    ("모터온도", 77),
    ("모터진동", 10),
    ("모터압력", 91),
    ("회전속도", 1133),
    ("유량", 42),
]

warning = 90
for name, value in sensors:
    print(name,value)

for name, value in sensors:
    if value > warning:
        print(f"{name} warning!!")
