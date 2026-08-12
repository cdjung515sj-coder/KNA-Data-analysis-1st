# 실습 5. 센서 통계 함수 만들기
# 내장 함수 min(), max(), sum(), len() 활용
# ① 센서값 목록을 매개변수로 받는 함수를 정의
# ② min·max·합÷개수로 최소·최대·평균을 계산
# ③ 세 값을 쉼표로 함께 return
# ④ 돌려받은 값을 세 변수로 언패킹해 출력



def analyze_sensor_data(sensor_values):
    min_val = min(sensor_values)
    max_val = max(sensor_values)
    avg_val = sum(sensor_values) / len(sensor_values)
    return min_val, max_val, avg_val


sensors_values = [77, 88, 99, 78, 87, 97]
min_temp, max_temp, avg_temp = analyze_sensor_data(sensors_values)
print(f"최소값: {min_temp}")
print(f"최대값: {max_temp}")
print(f"평균값: {avg_temp:.2f}")
