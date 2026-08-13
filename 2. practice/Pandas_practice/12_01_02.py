# # 실습 2. 설비 센서 CSV 불러오기
# import pandas as pd

# # 12_metro_compressor.csv
# # 200행 7열- 인덱스 3번 행 오일온도가 NaN

# df_sensor = pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8")
# print(df_sensor.head(10))
# print(df_sensor.shape)  # (200, 7)

# # pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8") 이렇게만 하면 안됨.
# # 꼭 df으로 시작하는 변수에 담아서 해줘


import os
import pandas as pd

filepath = os.path.join("data", "12_metro_compressor.csv")

try:
    df_metro_compressor = pd.read_csv(filepath)

    print("데이터 크기(Shape) : ", df_metro_compressor.shape)
    print(df_metro_compressor.head(5))

except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다.: {filepath}")
