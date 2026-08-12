# 실습 2. 설비 센서 CSV 불러오기
import pandas as pd

# 12_metro_compressor.csv
# 200행 7열- 인덱스 3번 행 오일온도가 NaN

df_sensor = pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8")
print(df_sensor.head(10))
print(df_sensor.shape)  # (200, 7)

# pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8") 이렇게만 하면 안됨.
# 꼭 df으로 시작하는 변수에 담아서 해줘


