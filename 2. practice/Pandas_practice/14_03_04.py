# 실습 4. 통합 리포트 종합
# 그룹 통계와 상관 분석을 묶어 발견·해석·행동 리포트 구성
import pandas as pd

df_equipment = pd.read_csv('data/14_equipment_sensor.csv', encoding='utf-8')
df_equipment.info()

# · 라인(line)으로 그룹을 나눠 
# (temp의) 측정수(count)·평균온도(mean)·온도편차(std) 요약 -> agg
report = df_equipment.groupby('line')['temp'].agg(['count', 'mean', 'std']).round(2)
print(report)
#       count   mean    std
# line                     
# A라인      54  76.86  10.18
# B라인      35  77.69   7.60
# C라인      31  79.88  10.38

# 위 결과를 그대로 복사해서 보고서에 붙여넣기하면 다른 사람은 알아보기 어렵다
# 그래서 label 처리를 해주는게 좋다. (Pandas 권장사항)
report = df_equipment.groupby('line').agg(
    측정수 = ('temp', 'count'),
    평균온도 = ('temp', 'mean'),
    온도편차 = ('temp', 'std')
).round(2)
print(report)
#       측정수   평균온도   온도편차
# line                   
# A라인    54  76.86  10.18
# B라인    35  77.69   7.60
# C라인    31  79.88  10.38

# 표 안에서도 심각한 정보를 먼저 보여주는 게 필요하다.
# 이 경우에는 온도편차가 큰 경우가 심각한 정보라서 우선 나타나게 해주자
print("----------------------------")
print("라인별 통계")
print(report.sort_values('온도편차', ascending = False))
#       측정수   평균온도   온도편차
# line                   
# C라인    31  79.88  "10.38"
# A라인    54  76.86  10.18
# B라인    35  77.69   7.60

# · 온도(temp)와 진동(vibration)의 상관계수(corr)를 구해 함께 움직임 확인
r = df_equipment['temp'].corr(df_equipment['vibration'])

print("----------------------------")
print("온도와 진동의 상관계수")
print(r.round(3)) # 0.345

# · 고장(result == 고장) 행을 걸러 라인별(line) 고장 건수까지 더해 우선 점검 대상 정리
df_bad = df_equipment[df_equipment['result'] == '고장']
# print(df_bad.head(2))

print("----------------------------")
print("라인별 고장 건수")
print(df_bad.groupby('line').size())
# A라인    16
# B라인     6
# C라인     6

# 예상 결과
# 라인 요약표·상관 0.931·라인별 고장 건수 출력

# 최종결과

# ----------------------------
# 라인별 통계
#       측정수   평균온도   온도편차
# line                   
# C라인    31  79.88  10.38
# A라인    54  76.86  10.18
# B라인    35  77.69   7.60
# ----------------------------
# 온도와 진동의 상관계수
# 0.345
# ----------------------------
# 라인별 고장 건수
# line
# A라인    16
# B라인     6
# C라인     6
# dtype: int64