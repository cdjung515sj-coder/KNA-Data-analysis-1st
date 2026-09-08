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
    print(name, value)

for name, value in sensors:
    if value > warning:
        print(f"{name} warning!!")


# 실습 3. 중첩 튜플로 센서 위치 관리
sensors = [
    ("모터온도", 77, (1, 2)),
    ("모터진동", 10, (3, 4)),
    ("모터압력", 91, (5, 6)),
    ("회전속도", 1133, (7, 8)),
    ("유량", 42, (9, 10)),
]

for name, value, i in sensors:
    x, y = i
    print(f"{name} | 위치 : {x,y}")

for name, value, i in sensors:
    x, y = i
    if x <= 5:
        print("x가 5이하 :",name)
