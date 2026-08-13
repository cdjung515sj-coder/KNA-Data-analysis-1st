# 실습 4. loc와 iloc로 행 선택하기
# 라벨 기준 loc와 번호 기준 iloc로 행 선택, 범위 차이 확인
import pandas as pd

df_diecasting_small = pd.read_csv("data/13_diecasting_small.csv")

# · loc로 라벨 기준 단일 행 선택
print(df_diecasting_small.loc[0, "품질등급"])  # 양품

# · iloc로 번호 기준 단일 행 선택
# df.iloc[0] -> 특정 row number인 row의 Serise 추출
# ..['품질등급'] -> 해당 Serise에서 '품질등급' 컬럼의 내용만 추출
print(df_diecasting_small.iloc[0]["품질등급"])  # 양품

# · 범위 선택으로 loc 끝 포함·iloc 끝 제외 차이 확인
# 다음 두 줄의 결과는 각각 어떻게 나타나는지
# 두 결과는 동일한지 아니면 다른지를 주석으로 달아주세요
print(len(df_diecasting_small.loc[0:2]))  # 3
print(len(df_diecasting_small.iloc[0:2]))  # 2

""" loc는 끝 라벨(2)을 '포함'하므로 인덱스 0, 1, 2 행을 가져옴 -> 출력값: 3 """
""" iloc는 끝 번호(2)를 '제외'하므로 위치 0, 1 행을 가져옴 -> 출력값: 2 """
