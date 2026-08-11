import numpy as np

# 실습 6. 센서별 기초 통계 구하기

# 목표 : 표 모양 데이터에서 센서별(열별) 통계 계산
# "axis(축) 옵션 문제"


# # · 여러 설비의 회전수·토크 이차원 배열 준비
# data6 = np.array([[1242, 42.5], [1532, 33.2], [1494, 49.4], [2839, 4.6]])


# # · axis를 열 방향으로 지정해 센서별 평균 계산
# print(data6.mean(axis=0))  # [1776.75    32.425]
# print(np.raound(data6.mean(axis=0), 2))

# # · 센서별 표준편차 계산
# print(np.raound(data6.std(axis=0), 2))

# 예상 결과 : 회전수·토크 각각의 평균과 표준편차가 출력

# --------------------------------------------------------------

sensor_data = np.array([[1242, 42.5], [1532, 33.2], [1494, 49.4], [2839, 4.6]])

sensor_means = sensor_data.mean(axis=0)
sensor_stds = sensor_data.std(axis=0)

print(
    f"센서 값 평균 : {np.round(sensor_means),2}, 센서별 표준편차 : {np.round(sensor_stds, 2)}"
)
