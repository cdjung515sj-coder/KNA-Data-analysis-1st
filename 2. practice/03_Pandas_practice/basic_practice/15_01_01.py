# 설비센서에서 진짜 결측과 위장 결측을 코드로 세기
# 실습 1. 눈으로 결측 찾기
# 목표
# 진짜 결측(NaN)과 위장 결측을 코드로 세어 확인
import pandas as pd

df_log = pd.read_csv("data/15_00_Injection_log.csv", encoding="utf-8")
print(df_log.describe())

# 단계
# · 설비 센서 데이터를 불러와 isna로 컬럼별 NaN 개수 세기
print(df_log.isna())
#      측정시각    사출기   배럴온도   사출압력  스크루속도    누적샷   불량여부
# 0   False  False  False  False  False  False  False
# 1   False  False  False  False  False  False  False
# 2   False  False   True  False  False  False  False
# 3   False  False  False  False  False  False  False
# 4   False  False  False  False  False  False  False
# 5   False  False  False  False  False  False  False
# 6   False  False  False   True  False  False  False
# 7   False   True  False  False  False  False  False
# 8   False  False  False  False  False  False  False
# 9   False  False  False  False  False  False  False
# 10  False  False  False  False  False  False  False
# 11  False  False  False  False  False  False  False
# 12  False  False   True  False  False  False  False
# 13  False  False  False  False  False  False  False
# 14  False  False  False  False  False  False  False
# 15  False  False  False  False   True  False  False

print(df_log.isna().sum())
# 측정시각     0
# 사출기      1
# 배럴온도     2
# 사출압력     1
# 스크루속도    1
# 누적샷      0
# 불량여부     0


# · 조건 필터링으로 압력 0, 진동 -999 같은 위장 결측 개수 세기
print((df_log["사출압력"] == 0.0).sum())  # 2
print((df_log["스크루속도"] == -999).sum())  # 2

# · 진짜 결측과 위장 결측을 나눠 비교

# 예상 결과
# NaN 4개(온도2·압력1·진동1), 위장 압력0 2개·진동-999 2개
