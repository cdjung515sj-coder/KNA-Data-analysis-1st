# 실습 1. 딕셔너리 만들고 다루기
# 1) 센서명을 키(key), 측정값을 값(value)로 딕셔너리 저장

sensors = {
    "모터온도": 78,
    "진동": 0.5,
}

# 2) 키로 값을 꺼내고 새 키로 추가,기존 키로 수정
print(sensors["진동"])
print(sensors.get("진동", 0))

sensors["압력"] = 95  # 없던 키를 언급하면 추가
sensors["진동"] = 0.3  # 있던 키를 언급하면 수정

print(sensors)

# 3) get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인
print(sensors.get("면적", -1))  # 면적 key는 존재하지 않아서 -1로 대체
print("진동" in sensors)  # 존재하는 key
print("면적" in sensors)  # 존재하지 않는 key
