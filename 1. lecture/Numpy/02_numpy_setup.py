# 중요하니 이건 꼭 읽어줘 다시 읽고 읽어줘

# 파이썬에서 기본 제공하는 기능들 외에 다양한 외부 라이브러리들을 가져오려면,
# https://pypi.org/ 사이트에서 검색

# numpy : https://pypi.org/project/numpy/
# pandas : https://pypi.org/project/pandas/
# pytouch : https://pypi.org/project/pytouch/


# 터미널에서 바로 pip로 설치를 시도하면 (pip install numpy)
# 전체 시스템에 영향을 주는 설치로 생각되어 거절당한다.
# 그래서 개별 Working Directory마다 별도의 환경을 구축해 그 안에 개별 프로젝트가 사용할 pip 라이브러리들을 따로 받아 쓰게 한다.
# 이것이 바로 가상환경(venv)이라고 한다.


# 1. 현재 경로에 가상환경 생성
# 터미널에서 실행
# python -m venv .venv


# 2. 가상환경 활성화
# source .venv/bin/activate (맥)
# source .venv/Scripts/activate
# (이후엔 가상환경 안에서 터미널 명령 실행 가능, 예) pip install numpy)


# 3. (작업/실행이 끝나고) 가상환경 종료
# deactivate


# Numpy 불러오기

import numpy as np

numbers = [1, 2, 3, 4, 5]
# 위 int 값들의 리스트를 사용해서 numpy의 배열 만들기
np_numbers = np.array(numbers)
print(np_numbers)
# [1 2 3 4 5] 이렇게 쉼표가 없으니 넘파이 사용 + 배열이구나~ 리스트가 아니니까 구분 좀 해~
