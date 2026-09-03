import pandas as pd

df = pd.DataFrame({"점수": [80, 55, 90]})

print(df)


def isPass(row, name, temp):
    if row["점수"] >= 60:
        return name + "합격" + temp
    else:
        return "불합격"


# df.apply() DataFrame의 모든 행, 열 기준으로 함수를 적용할 수 있도록 하는 매서드
# apply(func, axis=축 종류, ... func의 인자들 전달)
# 축 종류 0(열 방향 함수 적용), 1(행 방향 함수 적용)

df["결과"] = df.apply(isPass, axis=1, name="user ", temp="!!")

print(df)
