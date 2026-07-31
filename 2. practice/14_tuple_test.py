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
