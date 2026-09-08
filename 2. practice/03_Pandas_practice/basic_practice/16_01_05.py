# 실습 5. quantile로 Q1·Q2·Q3
# 목표
# 사분위수를 구하고 Q2가 중앙값과 같은지 확인
import pandas as pd

df_diecasting = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
# 단계
# · 25% 지점 값을 quantile로 구해 Q1 확인
quantile = df_diecasting["사이클타임"].quantile(0.25)
print(f"Q1 : {quantile}")  # 20.800

# · 50% 지점 값이 중앙값과 같은지 확인
print(f"중앙값 : {df_diecasting['사이클타임'].median()}")  # 22.600
print(f"Q2 : {df_diecasting['사이클타임'].quantile(0.50)}")  # 22.600

# · 75% 지점 값을 구해 가운데 절반 범위 파악
print(f"Q3 : {df_diecasting['사이클타임'].quantile(0.75)}")  # 35.925

# 예상 결과
# 실린더압력 Q1 215.75·Q2 218·Q3 265
