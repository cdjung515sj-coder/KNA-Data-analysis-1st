# 실습 3. 위장 결측 사냥
# 목표
# 위장 결측을 조건과 na_values로 진짜 결측으로 전환
import pandas as pd

df_log = pd.read_csv("data/15_00_Injection_log.csv", encoding="utf-8")

# 단계
# · 위장 결측이 있는 열을 조건 필터링으로 추출해 확인
print((df_log["스크루속도"] == -999).sum())  # 2
print((df_log["배럴온도"] == 999).sum())  # 1

# · na_values로 위장값을 결측으로 인식해 다시 불러오기
df_log = pd.read_csv(
    "data/15_00_Injection_log.csv", encoding="utf-8", na_values=[-999, 999]
)

print((df_log["스크루속도"] == -999).sum())  # 0
print((df_log["배럴온도"] == 999).sum())  # 0


# · 변환 전후 결측 개수를 비교
# 스크루속도는 2 -> 0, 배럴온도는 1 -> 0 개수가 달라짐

# 예상 결과
# 변환 후 NaN 5개→8개 (진동 -999·온도 999 포함
