# 표준 라이브러리의 math 모듈
import math

print(math.sqrt(9))  # 제곱근값
print(math.ceil(4.2))  # 올림값
print(2**3)  # 2의 2승 = 2 * 2 * 2 = 8 math와 무관

# math에서 sqrt, ceil 두개만 사용한다면 이렇게 써도 됩니다.
from math import sqrt, ceil

print(sqrt(9))

print("=" * 20)
# ==============================================================

# 표준 라이브러리의 random 모듈
import random

print(random.randint(1, 10))  # 1~10 중 무작위 정수
print(random.choice(["정상", "경고", "위험"]))

print("=" * 20)
# ==============================================================

# 표준 라이브러리의 datetime 모듈
import datetime

# datetime 모듈 안의 datetime 클래스에서 지원하는 now() 함수 호출
now = datetime.datetime.now()
print(now)  # 2026-08-05 13:19:26.523858

print("=" * 20)
# ==============================================================
# 모듈 도움말 보기 : 참고만 하고 구글링한 웹사이트에서 보자!
# print(dir(math))
# print(help(math.sqrt))


print("=" * 20)
# ==============================================================

# 절대경로와 상대경로
# pwd : 현재 위치 확인

# 절대경로의 예 : c:\Users\mzlap\Desktop\KNA-Data-analysis-1st
# 만약 /c/Users/mzlap/Desktop/KNA-Data-analysis-1st 폴더에 터미널을 연 상태에서
# code.py 코드를 실행하고 싶다면
# python code.py

# 위 code.py 언급부분은 사실 상대경로를 의미한다
# 그래서 절대경로로 지정해줘도 똑같이 실행될 것이다

# 현재 경로에 있는 해당 파일이란걸 더 강조하는 상대경로 지정으로 써도 된다
# python./code.py

# 만약 아닌
# 폴더 경로(cwd)에서 위 코드를 실행하고 싶다면
# 절대경로 : python
# 상대경로 : python .. \

# 표준 라이브러리의 os 모듈 활용
import os

current_working_directory = os.getcwd()
print(current_working_directory)

file_list = os.listdir()
print(file_list)

# 현재 작업디렉토리의 파일 목록 가져오기
file_list = os.listdir()
for file_name in file_list:
    print(file_name)
