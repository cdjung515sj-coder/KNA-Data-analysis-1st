print("=== 실습 - 여러 줄 / 이스케이프 다루기 ===")
print("""
설비 점검 안내
1. 전원 확인
2. 센서 점검
""")


print("\n=== 실습 - 설비 라벨 문자열 만들기 ===")
eq_code = "PUMP-A"
eq_state = "정상"
date = "2026.07.16"
print(eq_code, eq_state, date, sep=" / ")


print("\n=== 실습 - 설비 정보 출력 카드 만들기 ===")
code = "PUMP-A"
state = "normal"
runtime = 1200
inspec = "2026.07.16"

print(
    "코드: " + code,
    "\n상태: " + state,
    "\n가동: " + str(runtime),
    "\n점검: " + inspec,
)