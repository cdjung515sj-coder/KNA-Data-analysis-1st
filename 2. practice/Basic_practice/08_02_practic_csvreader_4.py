# 실습 4. csv.reader로 csv 읽기

import os
import csv

file_path = os.path.join("data","08_press.csv")

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])

