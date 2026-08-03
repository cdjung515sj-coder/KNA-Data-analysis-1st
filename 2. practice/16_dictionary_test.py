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

# =======================================================================================
print("============== 실습2 ===============")
# 실습 2. update로 여러 값 한 번에 갱신하기

# 1) 센서 딕셔너리와 새 데이터 딕셔너리 각각 저장
sensors = {"모터온도": 78, "진동": 0.5, "유량": 44}
new_sensors = {"모터온도": 78, "진동": 0.8, "유량": 33, "압력": 1}

# 2) update로 새 데이터를 한 번에 반영(있으면 수정, 없으면 수정)
sensors.update(new_sensors)
print(sensors)

# 3) del로 특정 키 삭제하고 len으로 개수 확인하기
del sensors["모터온도"]
print(sensors)
print(len(sensors))


# =======================================================================================
print("============== 실습3 ===============")
# 실습 3. 딕셔너리로 통계 내기

# 1) 센서명, 측정값 딕셔너리 저장
senors = {"모터온도": 78, "진동": 0.5, "유량": 44, "압력": 1}

# 2) values 합을 개수로 나눠 평균 구하기
total = 0
for value in sensors.values():
    total = total + value

print("평균:", total / len(sensors))

# 3) items로 순회하며 가장 큰 값고 그 센서명 찾아 출력하기

max_value = 0
max_name = ""
for name, value in sensors.items():
    if value > max_value:
        max_value = value
        max_name = name
print(f"최댓값 센서:{name}{value}")

# =========================================================================================
print("============== 실습4 ===============")
names = ["모터온도", "진동", "유량", "압력"]
values = [78, 0.5, 44, 95]
sensors = dict(zip(names, values))

for names, values in sensors.items():
    print(f"{names}:{values}")


# =========================================================================================
print("============== 실습5 ===============")

# 실습 5. 임계값으로 경고 센서 분류하기
values = {"모터온도": 78, "진동": 0.5, "유량": 44, "압력": 1}
limits = {"모터온도": 40, "진동": 0.3, "유량": 35, "압력": 1.5}

over_val = []

for name, value in values.items():
    if value > limits.get(name, 0):
        over_val.append(name)
print(f"경고센서:{over_val}")


# =========================================================================================
print("============== 실습6 ===============")

equipments = {
    "모터1": {"진동": 0.5, "유량": 44, "압력": 1, "상태": "정상"},
    "모터2": {"진동": 0.7, "유량": 56, "압력": 1.5, "상태": "경고"},
    "모터3": {"진동": 0.4, "유량": 45, "압력": 1.2, "상태": "정상"},
    "모터4": {"진동": 0.4, "유량": 43, "압력": 1.2, "상태": "정상"},
    "모터5": {"진동": 0.8, "유량": 60, "압력": 1.7, "상태": "경고"},
}

for e_name, state in equipments.items():
    if state["상태"] == "경고":
        print(f"{e_name} 점검 필요")


# =========================================================================================
print("============== 실습7 ===============")

senors = ["모터온도,78", "진동,0.5", "유량,44", "압력,1"]
sensors = {}


for senors_value in senors:
    name, value = senors_value.split(",")
    sensors[name] = float(value)
print(sensors)


# =========================================================================================
print("============== 실습8 ===============")

# 실습 8. 센서 데이터 통합 정리

eq_values = {"모터온도": 78, "진동": 0.5, "유량": 44, "압력": 1}
limits = {"모터온도": 40, "진동": 0.3, "유량": 35, "압력": 1.5}

total = 0
for value in eq_values.values():
    total = total + value

print(f"평균: {total / len(values):.2f}")

sets = set()

for name, value in eq_values.items():
    if value > limits[name]:
        sets.add(name)

print("위험 센서:", sorted(sets))
