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
