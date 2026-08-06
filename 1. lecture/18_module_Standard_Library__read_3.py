# 기본 내장함수인 open()으로 sample.txt 파일 열기
# 읽기모드(r)로 utf-8 형식의 변환을 거쳐 읽기로 한다
# 가져온 정도(파인 접근 열쇠/참조값)를 f에 담는다

f = open("data/sample.txt", "r", encoding="utf-8")


print(type(f).__name__)  # __name__ 이 언더바 두개씩은 약속임
# 타입 이름 : TextIOWrapper

# 텍스트파일 파일 한 줄씩 문자열 만들기
lines = f.readlines()
print(lines)

f.close()  # 열었다면 꼭 닫아줘야함

print("-=-" * 20)
# 만약 신경써서 파일 닫기(close) 해주기 귀찮다면
# with open ... as 문법을 쓰는 것도 좋다
with open("data/sample.txt", "r", encoding="utf-8") as f:
    # 앞으로 이렇게 들여쓰기 된 코드가 끝나면
    # 파일 접은을 닫습니다(close)

    # 텍스트파일 파일 한줄씩 문자열을 만들어 리스트만들기
    lines = f.readlines()

print(lines)


# ==============
# 쓰기모드(write)로 파일을 새롭게 만들어보겠습니다.
f = open("data/hello.txt", "w", encoding="utf-8")

# 파일 쓰기에 줄바꿈을 포함하려면 \n을 포함 시킨다
f.write("안녕하세요\n")
# 파일 쓰기에 들여쓰기를 포함하는 경우
f.write("\t반갑습니데이~")

f.close()

# ===============
# 이어쓰기 모드(append)로 파일에 내용을 추가해보자
f = open("data/hello.txt", "a", encoding="utf-8")

# 파일 쓰기에 줄바꿈을 포함하려면 \n을 포함 시킨다
f.write("맛점!!!\n")

f.close()


# ============================================================

import os
import sys
import csv

csv_path = os.path.join("data", "08_press.csv")

# 위 경로의 파일을 찾지 못한다면 강제종료시키기
if not os.path.exists(csv_path):
    print("파일있음")
    sys.exit(1)  # 비정상 종료시 보통 0이 아닌 값(예 1) 전달

print("파일없음")

with open(csv_path, "r", encoding="utf-8") as f:
    # print(f.readlines()) # 이제 csv 전문가에게 맡기자 !
    reader = csv.reader(f)

    for row in reader:
        print(row)  # 각 행(row)마다 리스트로 출력됨

# -------------------------

import os
import csv

csv_path = os.path.join("data", "result.csv")

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])
