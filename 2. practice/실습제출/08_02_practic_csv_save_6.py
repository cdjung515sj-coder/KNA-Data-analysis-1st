# 실습 6. csv 읽어 조건 저장하기

import os
import csv

csv_path = os.path.join("data", "08_press.csv")
write_path = os.path.join("data", "08_press_over90.csv")

over_90 = []

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)

    for row in reader:
        elect = float(row[4])

        if elect > 90:
            over_90.append(row)

with open(write_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(over_90)

print("파일 생성 완료, 08_press_over90.csv 파일 생성 확인 요망")
