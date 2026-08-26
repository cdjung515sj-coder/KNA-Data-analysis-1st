import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

q1 = df["사이클타임"].quantile(0.25)
q3 = df["사이클타임"].quantile(0.75)

print(f"Q1 : {q1} , Q3 : {q3}")
# Q1 : 20.8 , Q3 : 35.925

iqr = q3 - q1

print("IQR : ", iqr)
# IQR :  15.124999999999996

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print("하한선 :", lower, "/ 상한선 :", upper)
