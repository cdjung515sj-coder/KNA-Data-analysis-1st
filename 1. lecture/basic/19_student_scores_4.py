# 학생들의 점수를 가져와서 각 학생별 합계와 보든 학생들의 평균 점수를 내는 코드

import os
import sys
import csv

# 0. 미리 전체 합산 점수 낼 준비를 한다
total_all = 0
student_count = 0


# 1. 파일을 연다
file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾지 못 했습니다.")
    sys.exit(1)

# 2. 파일 내용으로부터 리스트 데이터를 얻는다
with open(file_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("이름", "(이름없음)")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))

        total = (kor + eng + math) / 3
        print(f"{name} | {kor} | {eng} | {math} | {total:.2f}")

        # 3. 점수 계산(합계, 평균)
        student_count += 1
        total_all += total
# 4. 결과를 화면에 보여주기
avg_all = total_all / student_count
print(f"전체 {student_count}명 | 평균 {avg_all:.2f}")


# [제출 안하는 실습] ============================================================
print("\n ============================================== \n")
# student_score.py를 기반으로
# 1. 실행 끝날 때 최고점 학생, 최저점 학생도 찾아서 출력해보세요
import os
import sys
import csv

# 0. 미리 전체 합산 점수 낼 준비를 한다
total_all = 0
student_count = 0

max_name = ""
max_score = 0

min_name = ""
min_score = 100  # 모든 학생 개별 점수는 100점 이하라고 보고 처리. ⭐⭐⭐⭐⭐⭐
# 최저점을 잡을 때 이거야 !!!!!!!!

kor_total = 0
eng_total = 0
math_total = 0

# 1. 파일을 연다
file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾지 못 했습니다.")
    sys.exit(1)

# 2. 파일 내용으로부터 리스트 데이터를 얻는다
with open(file_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("이름", "(이름없음)")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))

        student_count += 1
        total = (kor + eng + math) / 3
        print(f"{student_count} | {name} | {kor} | {eng} | {math} | {total:.2f}")

        # 3. 점수 계산(합계, 평균)
        kor_total += kor
        eng_total += eng
        math_total += math
        total_all += total

        if total > max_score:
            max_name = name
            max_score = total

        if total < min_score:
            min_name = name
            min_score = total


# 4. 결과를 화면에 보여주기
print(f"최고점 학생: {max_name} ({max_score:.2f})")
print(f"최저점 학생: {min_name} ({min_score:.2f})")

avg_all = total_all / student_count
print(f"전체 {student_count}명 | 평균 {avg_all:.2f}")

print(f"국어 평균: {kor_total / student_count:.2f}")
print(f"영어 평균: {eng_total / student_count:.2f}")
print(f"수학 평균: {math_total / student_count:.2f}")


# 2. 실행 끝날 때 각 과목별 평균도 출력해보세요 (선택)
