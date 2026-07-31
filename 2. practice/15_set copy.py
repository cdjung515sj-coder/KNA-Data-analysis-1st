# 실습 4. 셋으로 중복 센서 제거하기

logs = [
    "WQR_01",
    "WQR_06",
    "WQR_03",
    "WQR_03",
    "WQR_01",
    "WQR_06",
    "WQR_01",
    "WQR_01",
    "WQR_03",
    "WQR_05",
]
unique = set(logs)
print(sorted(unique))
print(f"종류 수 : {len(unique)}")


# 실습 5. 두 라인의 센서 구성 비교하기
sensor_1 = {"WQR_01", "WQR_02", "WQR_03", "WQR_04"}
sensor_2 = {"WQR_03", "WQR_05", "WQR_04", "WQR_06", "WQR_7"}
print("전체(합집합): ", sensor_1 | sensor_2)
print("공통(교집합): ", sensor_1 & sensor_2)
print("차이(차집합) [1-2]: ", sensor_1 - sensor_2)
print("차이(차집합) [2-1]: ", sensor_2 - sensor_1)
