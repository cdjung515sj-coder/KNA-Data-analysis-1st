# 실습 8. 압축기와 디지털 신호 구조 비교
# data/12_metro_compressor.csv
# data/12_metro_digital.csv
# shape, info, describe 활용

import pandas as pd

df_metro_compressor = pd.read_csv("data/12_metro_compressor.csv")
print(df_metro_compressor.shape)
print(df_metro_compressor.info())
print(df_metro_compressor.describe())

df_metro_digital = pd.read_csv("data/12_metro_digital.csv")
print(df_metro_digital.shape)
print(df_metro_digital.info())
print(df_metro_digital.describe())
