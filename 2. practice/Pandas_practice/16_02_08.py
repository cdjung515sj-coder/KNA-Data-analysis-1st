# 실습 8. drop_duplicates로 중복 제거
# 목표
# 완전 중복 제거와 기준 컬럼 지정 제거를 비교
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# 단계
# · drop_duplicates로 완전 중복 행 제거
print(f"원본 행 수: {len(df)}")

df_onlyone = df.drop_duplicates()
print(f"완전 중복 제거 후 행 수: {len(df_onlyone)}")
print(f"남은 중복 개수: {df_onlyone.duplicated().sum()}")


# · 제거 후 행 수와 남은 중복 개수 확인
df_onlyone_shot = df.drop_duplicates(subset=["샷"], keep="last")
print(f"subset 기준 중복 제거 후 행 수: {len(df_onlyone_shot)}")

# · subset으로 특정 컬럼만 기준 삼아 제거


# 예상 결과
# 202행 → 200행, 남은 중복 0, subset 기준도 200행
