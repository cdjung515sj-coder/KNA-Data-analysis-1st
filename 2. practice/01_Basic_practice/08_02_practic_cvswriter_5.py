# 실습 5. csv.writer로 csv 쓰기

import os
import csv

csv_path = os.path.join("data", "result2.csv")

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "펌프 설비"])
    writer.writerow(["09:00", "PUMP-01"])
    writer.writerow(["09:01", "PUMP-01"])
    writer.writerow(["09:02", "PUMP-01"])
    writer.writerow(["09:03", "PUMP-01"])
