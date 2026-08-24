# 실습 7. 여러 컬럼의 가운데 절반 폭 비교
# 목표
# 세 컬럼의 가운데 절반 폭(Q3-Q1)을 비교 : Q1, Q2, Q3 , quantile()
import pandas as pd

df_diecasting = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# 단계
# · 세 컬럼의 사분위수를 한 번에 구하기 - 실린더압력, 사이클타임, 비스킷두께
df_q = df_diecasting[["실린더압력", "사이클타임", "비스킷두께"]].quantile([0.25, 0.50, 0.75])
print(df_q)
#        실린더압력   사이클타임  비스킷두께
# 0.25  215.75  20.800   11.0
# 0.50  218.00  22.600   13.0
# 0.75  265.00  35.925   17.0

# · 각 컬럼의 75% 값에서 25% 값을 빼 가운데 절반 폭 계산
# df_q에서 0.75가 index label로 되어있는 row -> df_q.loc[0.75]
iqr = df_q.loc[0.75] - df_q.loc[0.25]
print(iqr)

# · 폭이 좁은 안정 컬럼과 넓은 의심 컬럼 구분
min_val = iqr.min()
max_val = iqr.max()

# 2. 조건문(if)으로 어떤 컬럼인지 비교하여 출력
for col in iqr.index:
    if iqr[col] == min_val:
        print(f"안정 컬럼 : {col} (폭: {iqr[col]:.2f})")
    elif iqr[col] == max_val:
        print(f"의심 컬럼 : {col} (폭: {iqr[col]:.2f})")

# 예상 결과
# 폭 실린더압력 49.25·사이클타임 15.12·비스킷두께 6
