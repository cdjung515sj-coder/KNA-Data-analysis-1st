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
            print("'09_ict_inspection_dirty.csv'파일을 읽었습니다.")

        return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []


header, rows = read_file_ict("data/09_ict_inspection_dirty.csv")

print(f"총 데이터 : {len(rows)} 행")


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


# ================================================================
# 실습 3. 통계 함수


def calc_stats(rows):

    numbers = []

    for row in rows:

        try:
            value = float(row["측정값"])

        except (ValueError, TypeError):
            continue

        numbers.append(value)

    if len(numbers) == 0:
        return None

    count = len(numbers)
    average = sum(numbers) / count
    minimum = min(numbers)
    maximum = max(numbers)

    return count, average, minimum, maximum # 계산한 통계값(개수, 평균, 최솟값, 최댓값)을 호출한 곳으로 반환


stats = calc_stats(rows)

if stats is None:
    print("계산할 수 있는 데이터가 없습니다.")
else:
    count, average, minimum, maximum = stats

    print("\n[측정값 통계]")
    print(f"개수 : {count}")
    print(f"평균 : {average:.2f}")
    print(f"최솟값 : {minimum}")
    print(f"최댓값 : {maximum}")
