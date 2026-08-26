import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
print(df.head(3))


## df.duplicated() : 데이터프레임 내에서 완벽하게 내용이 겹쳐서 존재하는 중복 행 여부를 불리언 시리즈로 반환
# 데이터를 받자마자 duplicated().sum() — 짧지만 강력한 점검

print(df.duplicated())  # True/Flase의 Boolean Serise.
print(df[df.duplicated()])  # "완전"중복된 row들만 df로 추려냄
#       샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 200   8  215.0  1038.0   20.9   11.0  258.0   0  -> 2건
# 201  89  235.0  1137.0   22.7   13.0  261.0   0  -> 2건


# 중복 개수 확인하기
print(
    df.duplicated().sum()
)  # 중복 개수 확인 # 2 row들이 중복으로 더 존재함 (먼저 확인 row 제외)
print(
    len(df)
)  # 202 : 전체가 202개 row로 2개 중복 뺴면 순수하게 200개가 한 줄씩 안 겹치고 존재


print(df.duplicated(keep=False).sum())  #


## drop_duplicates() : 중복 제거
print(len(df.drop_duplicates()))  # 200

# .reset).index(drop=True) : 중복을 지운 후 듬성듬성 깨져버린 원래의 일련번호 인덱스를 0부터 시작하는 촘촘한 정수로 새로 깔끔하게 정렬시켜줌
print(len(df.drop_duplicates().reset_index(drop=True)))  # 200

# 인덱스(Index) 자체의 개수를 구하는 방법
print(len(df.drop_duplicates().reset_index(drop=True).index))

# 부분중복 사례 제거 : "샷","실린더압력", "주조압력" 컬럼만 중복되면 제거 대상
print(
    len(
        df.drop_duplicates(subset=["샷", "실린더압력", "주조압력"]).reset_index(
            drop=True
        )
    )
)
