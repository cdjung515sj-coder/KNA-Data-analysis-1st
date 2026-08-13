# 실습 3. 공정 센서 열 골라내기

# 주조 로그 파일 불러오기
# 13_diecasting_shot.csv 파일 열기
import pandas as pd

df_diecasting_shot = pd.read_csv("data/13_diecasting_shot.csv")

print(df_diecasting_shot.columns)
# Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급'], dtype='str')


# 한 센서 열을 Series로 선택
# '형체력' 선택
print(df_diecasting_shot["형체력"].info())  # <class 'pandas.Series'>


# 여러 feature 열을 DataFrame으로 선택해서 형태 확인
# df[['형체력','실린더압력','주조압력']].shape 출력

print(df_diecasting_shot[["형체력", "실린더압력", "주조압력"]].info())
print(df_diecasting_shot[["형체력", "실린더압력", "주조압력"]].shape)  # (200, 3)
