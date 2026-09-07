"""
열화 추세와 P-F 개념 예제
- 완만한 마모형 추세 생성
- P점과 F점 사이의 P-F 간격 계산
- 점검 주기 절반 규칙 계산
"""

import pandas as pd


# 압연롤 보정량이 시간이 지나며 증가한다고 가정
roll = pd.DataFrame(
    {
        "day": list(range(0, 121, 10)),
        "gap_compensation": [0.020, 0.025, 0.031, 0.037, 0.044, 0.052, 0.061, 0.071, 0.082, 0.094, 0.107, 0.121, 0.136],
    }
)

# 예시 기준
# P점: 분석적으로 변화를 신뢰할 수 있게 된 보정량 0.060 이상
# F점: 요구 기능 기준에 가까운 보정량 0.130 이상
p_threshold = 0.060
f_threshold = 0.130

p_row = roll[roll["gap_compensation"] >= p_threshold].iloc[0]
f_row = roll[roll["gap_compensation"] >= f_threshold].iloc[0]

p_day = int(p_row["day"])
f_day = int(f_row["day"])
pf_interval = f_day - p_day
inspection_interval = pf_interval / 2

print("=== 압연롤 열화 데이터 ===")
print(roll)

print("\n=== P-F 계산 ===")
print(f"P점: {p_day}일")
print(f"F점: {f_day}일")
print(f"P-F 간격: {pf_interval}일")
print(f"기본 점검 주기 상한(P-F/2): {inspection_interval:.1f}일")

# 실제 현장에서는 P점과 F점을 임의 숫자로 잡지 않고,
# 정비 이력, 기능 기준, 센서 검출 한계, 필요한 리드타임을 근거로 정의해야 합니다.
