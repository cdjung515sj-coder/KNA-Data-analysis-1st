# 실습 1단계 csv 읽기

import os, sys, csv

file_path = os.path.join("data", "09_ict_inspection_dirty.csv")

header = []
rows = []


def read_file_ict(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            header = lines[0]
            rows = lines[1:]

        return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []


header, rows = read_file_ict("data/09_ict_inspection_dirty.csv")
print(header)
print(f"데이터 행 수 : {len(rows)} 행")
