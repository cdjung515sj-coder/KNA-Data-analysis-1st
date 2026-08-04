# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)


# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)


# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)


# TODO 4. 전체 평균 온도 출력 (round)


# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)


# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())


# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"

# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

danger_count = 0
worning_count = 0
normal_count3 = 0

total_temp = 0

temp_max = []
for name, temp, vib in sensors:
    temp_max.append((temp, name, vib))
temp_max.sort(reverse=True)
top_temp, top_name, top_vib = temp_max[0]

danger_list =[]

print("""
======================================== 
| | | | 설비 종합 모니터링 리포트
========================================
""")
for i, (name, temp, vib) in enumerate(sensors, 1):
    total_temp += temp
    if temp > 90 or vib > 5.0:
        danger_count += 1
        state = "위험 🚨"
        danger_list.append(name)
    elif temp >= 80 or vib >= 3.0:
        worning_count += 1
        state = "주의 ⚠️"
    else:
        normal_count3 += 1
        state = "정상 ✅"
    print(f"{i}. {name} | 온도 {temp}℃ | 진동 {vib}mm/s | {state}")


print("\n----------------------------------------\n")
total = len(sensors)
danger_list.sort()
print("총 설비:", total)
print(f"정상: {normal_count3} / 주의: {worning_count} / 위험: {danger_count}")
print(f"이상 설비 비율: {((worning_count+danger_count)/total)*100:.1f}%")
print(f"평균 온도: {total_temp/total:.1f}℃")
print(f"최고 온도 설비: {temp_max[0][1]} ({temp_max[0][0]}℃ ) ")
print(f"위험 설비 목록: {danger_list}")
print("\n=======================================")