import numpy as np

# 실습 7. 파일 데이터로 기초 통계 구하기
# 파일로 저장된 공정 데이터를 불러와 기초 통계 계산

# ----------------------------------------------------------------------
# np.loadtxt: CSV 파일 데이터를 직접 NumPy 배열로 로드하는 함수입니다.
# * delimiter=',' :  쉼표 구분자
# * skiprows=1 : 맨 윗줄 열 이름(헤더) 1줄 건너뜀
# * usecols=4: 4번 인덱스 열(회전수) 데이터만 선택 로드
# - 로드된 실제데이터의 값들을 한줄로 정량 산출합니다.
# ----------------------------------------------------------------------

# np.loadtxt로 회전수 열을 파일에서 불러오기
rpm7 = np.loadtxt(
    "data/10_mct_tool.csv", delimiter=",", skiprows=1, usecols=4, encoding="utf-8"
)
# 불러온 배열의 평균과 표준편차 계산
print(round(rpm7.mean(), 1))  # 4212.6
print(round(rpm7.std(), 1))  # 1144.9

# 최솟값과 최댓값으로 갔의 범위 확인
print(rpm7.min(), rpm7.max())  # 58.0 4987.0
print(rpm7.max() - rpm7.min())  # 4929.0


# 회전수의 평균, 표준편차와 최솟값,최댓값이 출력

# -----------------------------------------------------
file_content = np.loadtxt(
    "data/10_mct_tool.csv", delimiter=",", skiprows=1, usecols=4, encoding="utf-8"
)

file_mean = file_content.mean()
file_std = file_content.std()
print(round(file_mean, 1))  # 4212.6
print(round(file_std, 1))  # 1144.9

print(file_content.min(), file_content.max())  # 58.0 4987.0
print(file_content.max() - file_content.min())  # 4929.0

