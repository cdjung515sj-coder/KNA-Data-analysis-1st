"""
예지보전 성과 지표 계산 예제
- MTBF
- MTTR
- OEE
- Precision / Recall
- Lead Time
"""

import pandas as pd


# ---------------------------------------------------------------------
# 1. MTBF / MTTR
# ---------------------------------------------------------------------
operating_hours_between_failures = [420, 510, 470, 530]
repair_hours = [6.0, 4.5, 5.5, 4.0]

mtbf = sum(operating_hours_between_failures) / len(operating_hours_between_failures)
mttr = sum(repair_hours) / len(repair_hours)

print("=== 현장 지표 ===")
print(f"MTBF: {mtbf:.1f} 시간")
print(f"MTTR: {mttr:.1f} 시간")


# ---------------------------------------------------------------------
# 2. OEE
# ---------------------------------------------------------------------
availability = 0.92   # 가동률
performance = 0.95    # 성능률
quality = 0.98        # 양품률

oee = availability * performance * quality
print(f"OEE: {oee * 100:.2f}%")


# ---------------------------------------------------------------------
# 3. Precision / Recall
# ---------------------------------------------------------------------
# 예: 실제 고장 10건 중 7건 사전 검출, 경보는 총 20건
TP = 7
FN = 3
FP = 13

recall = TP / (TP + FN)
precision = TP / (TP + FP)

print("\n=== 모델 판정 지표 ===")
print(f"Recall(재현율): {recall * 100:.1f}%")
print(f"Precision(정밀도): {precision * 100:.1f}%")


# ---------------------------------------------------------------------
# 4. Lead Time
# ---------------------------------------------------------------------
alerts = pd.DataFrame(
    {
        "failure_id": ["F01", "F02", "F03"],
        "first_valid_alert": pd.to_datetime(["2026-08-01", "2026-08-10", "2026-08-18"]),
        "failure_time": pd.to_datetime(["2026-08-09", "2026-08-15", "2026-08-20"]),
    }
)

alerts["lead_time_days"] = (
    alerts["failure_time"] - alerts["first_valid_alert"]
).dt.total_seconds() / 86400

print("\n=== 리드타임 ===")
print(alerts)
print("평균 리드타임:", round(alerts["lead_time_days"].mean(), 2), "일")
print("최소 리드타임:", round(alerts["lead_time_days"].min(), 2), "일")
