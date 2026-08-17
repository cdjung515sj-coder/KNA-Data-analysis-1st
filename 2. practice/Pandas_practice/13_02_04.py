# 실습 4. 부정·목록·범위 조건
# 목표
# 부정·목록 매칭·범위 조건을 각각 적용

import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
df.info()

# 단계
# · 물결 기호로 고장이 아닌 설비만 뒤집어 추출
print(df.head())
print(df.tail())
print(df[df["품질등급"] == "불량"].head())
print(len(df[df["품질등급"] == "불량"]))

# 그렇다면 '불량'이 아닌 것은?
print(df[~(df["품질등급"] == "불량")].head())
print(len(df[~(df["품질등급"] == "불량")]))

# · isin으로 품질등급이 특정 목록에 속하는 행 추출
print(df[(df["품질등급"] == "양품") | (df["품질등급"] == "주의")].head())
print(len(df[(df["품질등급"] == "양품") | (df["품질등급"] == "주의")]))

print(df[df["품질등급"].isin(["양품", "주의"])].head())
print(
    len(df[df["품질등급"].isin(["양품", "주의"])]),
)


# · between으로 실린더압력가 지정 범위에 든 행 추출
print(df[df["실린더압력"].between(210, 230)].head())
print(len(df[df["실린더압력"].between(210, 230)])) # 89

# 그 외의 것들이 200 -89 = 111개 나오는지 확인하기
print(
    len(df[~(df["실린더압력"].between(210, 230))]) # 111
)  ## 조건에 ~ 칠 것. 중요 매우매우 중요 !!!
# 예상 결과
# 순서대로 192건·94건·108건 출력
