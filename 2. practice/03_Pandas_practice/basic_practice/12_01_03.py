# 실습 3. 한글, 구분자 깨짐 옵션 다루기

# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=";"이면

# import pandas as pd

# df = pd.read_csv("data/12_metro_compressor_semicolon.csv")
# print(df.shape)  # (200, 1) 200행 1열
# # 왜 여기 1개 밖에 없다고 뜨지? 보통 컬럼이 최소 2개 이상임. 하나만 있다? 이상함을 인지하고 함 봐
# # 확인하는 방법은 head로 확인해

# print(df.head(4))


# # 구분자를 바꿔 보기 쉽게 만들자!
# df = pd.read_csv("data/12_metro_compressor_semicolon.csv", sep=";", encoding="utf-8")
# print(df.shape)
# print(df.head(4))

# ====================================================================================
import os
import pandas as pd

filepath = os.path.join("data", "12_metro_compressor_semicolon.csv")

try:
    df_broken = pd.read_csv(
        "data/12_metro_compressor_semicolon.csv", sep=";", encoding="utf-8"
    )
    print("   Shape:", df_broken.shape)
    print(df_broken.head(4))
except Exception as e:
    print("에러 발생:", e)

try:
    df_clean = pd.read_csv(filepath, sep=";", encoding="cp949")

    print("sep=';', encoding='cp949' 적용 후 데이터 크기:")
    print("   Shape:", df_clean.shape)  # (200, 7) -> 정상 분리 완료
    print(df_clean.head(5))

except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {filepath}")
except UnicodeDecodeError:
    print("인코딩 방식이 맞지 않습니다. 'utf-8' 또는 'euc-kr'로 변경해 주세요.")


