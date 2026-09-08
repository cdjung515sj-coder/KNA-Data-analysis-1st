# 선택 문제 : 첨부된 CSV 파일을 통해 다음 통계들을 내는 코드를 작성해 제출해주세요.
import pandas as pd

df_students = pd.read_csv("data/students_groupby_practice.csv", encoding="utf-8")
df_students.info()

# [문제 1] 이 학교의 전체 학생 수를 구하세요. (힌트: len 또는 shape)
print(len(df_students))  # 60명

# [문제 2] 학년별 학생 수를 구하세요. (힌트: groupby + count 또는 size)
print(df_students.groupby("학년")["학년"].count())
# 학년
# 1    20
# 2    20
# 3    20

# [문제 3] 학년 내 각 반별 학생 수를 구하세요. (힌트: 다중 컬럼 groupby)
print(df_students.groupby(["학년", "반"])["학년"].count())
# 학년  반
# 1   A    5
#     B    5
#     C    5
#     D    5
# 2   A    5
#     B    5
#     C    5
#     D    5
# 3   A    5
#     B    5
#     C    5
#     D    5

# [문제 4] 각 반(학년, 반 조합)의 국어 점수 평균을 소수점 둘째 자리까지 구하세요.
print(df_students.groupby(["학년", "반"])["국어"].mean().round(2))
# 학년  반
# 1   A    76.8
#     B    78.8
#     C    66.0
#     D    59.4
# 2   A    64.6
#     B    81.4
#     C    84.6
#     D    72.0
# 3   A    68.6
#     B    81.4
#     C    73.0
#     D    69.8


# [문제 5] 각 학년의 영어 점수 평균을 소수점 둘째 자리까지 구하세요.
print(df_students.groupby("학년")["영어"].mean().round(2))
# 학년
# 1    64.80
# 2    73.35
# 3    69.90

# [문제 6] 학교 전체의 수학 점수 평균을 소수점 둘째 자리까지 구하세요.
print(df_students["수학"].mean().round(2))  # 68.95
