# 실습 1. CSV 불러오기 워밍업

# import pandas as pd
# import os

# # 목표 : 작은 설비 데이터를 CSV로 만들고 메모장 · 엑셀에서 비교
# try:
#     filepath = os.path.join("data", "12_metro_small.csv")
#     df_metro_small = pd.read_csv(
#         filepath
#     )  # df : data frame  # _ 뒤에 덧붙여줘서 이름을 짓는 것도 좋은 습관!

#     print(
#         df_metro_small.shape
#     )  # (30, 7) # 30개의 행(row)와 7개의 열(column)이라는 뜻 !
#     print(df_metro_small.head())
#     print(df_metro_small.head(1))
#     # 첫 줄만 뽑아 온건데 데이터 인덱스로부터 row 하나를 뽑아옴. 맨 윗줄을 같이 출려해주기 때문에 print문으로 쉽게 확인 가능
#     # 데이터 분석가가 힘들어해서 같이 출력해줌. ## 측정시각  압축압력  배출압력  저장압력  오일온도  모터전류 가동상태 ##
#     print(df_metro_small.head(2))

# except FileExistsError:
#     print(f"파일이 없습니다 : {filepath}")


# --------------------------------------------------------

import os
import pandas as pd

filepath = os.path.join("data", "12_metro_small.csv")

try:
    df_metro_small = pd.read_csv(filepath)

    print(df_metro_small.shape)  # (30, 7) -> 30행 7열
    print(df_metro_small.head())
    print(df_metro_small.head(1))
    print(df_metro_small.head(2))

except FileNotFoundError:  # FileExistsError -> FileNotFoundError로 수정
    print(f"파일이 없습니다 : {filepath}")

