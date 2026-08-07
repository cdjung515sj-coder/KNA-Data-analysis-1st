# 실습 1단계 csv 읽기

import os, sys, csv

# csv 파일 경로 생성
file_path = os.path.join("data", "09_ict_inspection_dirty.csv")

# 헤더, 행 변수 지정
header = []
rows = []


def read_file_ict(file_path):
    try:
        # 파일 열기
        with open(file_path, "r", encoding="utf-8") as file:

            # DictReader : 헤더를 키로 사용하는 딕셔너리 형태로 앍어줌
            reader = csv.DictReader(file)

            # fieldnames : 헤더(컬럼명) 저장
            header = reader.fieldnames

            # 모든 뎅터 행을 리스트로 저장
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

    # 설비별 데이터 저장 딕셔너리
    classified_data = {}

    # 모든 행 반복
    for row in rows:

        # 빈 데이터 건너뜀
        if not row:
            continue

        equipment_name = row.get("부품명")

        # 기존 리스트 있으면 가져오고  / 없으면 빈 리스트 생성 시키기
        equipment_list = classified_data.get(equipment_name, [])

        # 현재 행 추가
        equipment_list.append(row)

        classified_data[equipment_name] = equipment_list

    # 설비별 데이터 개수 출력
    for eq_name, eq_rows in classified_data.items():
        print(f"{eq_name}: {len(eq_rows)}")

    return classified_data


classify_by_equipment(rows)


# ================================================================
# 실습 3. 통계 함수


def calc_stats(rows):

    numbers = []  # 숫자만 리스트로 저장

    for row in rows:

        try:
            value = float(row["측정값"])

        except (ValueError, TypeError):
            # 숫자가 아니면 건너뜀
            continue

        numbers.append(value)

    if len(numbers) == 0:
        return None

    count = len(numbers)
    average = sum(numbers) / count
    minimum = min(numbers)
    maximum = max(numbers)

    return count, average, minimum, maximum


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


# ================================================================
# 실습 4. 불량 방어


def clean_data(rows):

    clean_rows = []
    errors = []

    for line_no, row in enumerate(rows, start=2):

        try:
            value = float(row["측정값"])

            # 상한치, 하한치가 없으면 직접 오류 발생
            if not row["상한치"] or not row["하한치"]:
                raise ValueError("상한치 또는 하한치가 없습니다.")

            # 상한치, 하한치 숫자로 변환
            upper = float(row["기준값"])
            lower = float(row["하한치"])

            # 측정값이 정상 범위를 벗어나면 오류 발생
            if value < lower or value > upper:
                raise ValueError("정상 범위를 벗어났습니다.")

            # 여기까지 오류가 없으면 정상 데이터
            clean_rows.append(row)

        except (ValueError, TypeError) as e:
            # 불량 행 번호와 이유 저장
            errors.append([line_no, str(e)])

            continue

    return clean_rows, errors


clean_rows, errors = clean_data(rows)

print("\n[정상 데이터]")
print(f"정상 데이터 수 : {len(clean_rows)}개")

print("\n[불량 데이터]")

for error in errors:
    print(f"{error[0]}번째 줄 : {error[1]}")
