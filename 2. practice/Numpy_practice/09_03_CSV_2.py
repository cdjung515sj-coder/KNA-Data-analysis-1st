# 실습 1단계 csv 읽기

import os, sys, csv

file_path = os.path.join("data", "09_ict_inspection_dirty.csv")

header = []
rows = []


def read_file_ict(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            rows = list(reader)

        return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []


header, rows = read_file_ict("data/09_ict_inspection_dirty.csv")
print(header)
print(f"데이터 행 수 : {len(rows)} 행")


# ================================================================
# 실습 2단계 csv 읽기


def classify_by_equipment(rows):

    classified_data = {}

    for row in rows:
        if not row:
            continue

        equipment_name = row.get("부품명")

        equipment_list = classified_data.get(equipment_name, [])

        equipment_list.append(row)

        classified_data[equipment_name] = equipment_list

    for eq_name, eq_rows in classified_data.items():
        print(f"{eq_name}: {len(eq_rows)}")

    return classified_data


classify_by_equipment(rows)
