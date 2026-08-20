# value counts 기본 코드

import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()

#  7   result  120 non-null    str    => 범주형임을 알 수 있음

print(df.head())
#   냉각기상태 운전부하 밸브상태    온도     진동      압력  냉각효율 result
# 0    고장  고부하   정상  35.6  0.577  160.67  39.6     정상
# 1    고장  저부하   정상  47.5  0.604  158.65  17.6     정상
# 2    고장  저부하   정상  50.7  0.640  157.76  18.7     정상
# 3    고장  저부하   정상  51.7  0.635  157.54  19.6     정상
# 4    고장  저부하   정상  52.4  0.635  157.36  21.1     정상

df_old = df[df["냉각기상태"] == "고장"]  # 냉각기상태가 고장인 데이터만 추출함
print(f"고장 데이터 수: {len(df_old)}")  # 고장 데이터 수: 40
# 하지만 이 방식으로 모든 상태를 112 찾아서 통계내는 것은 비효율적임
# '고장' 외에도 모든 경우를 한 번에 모아서 경우마다 빈도를 나타내는 갯수를 찾는 것이 좋음
# value_counts 메소드를 사용하면 이렇게 가능


# 냉각기상태별 사이클 건수 세기
print(df["냉각기상태"].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40


# results 컬럼의 정상/고장 건수 세기
print(f"=== results 컬렴 정상/고장 건수 세기 === \n {df["result"].value_counts()}")
#  result
# 정상    67
# 고장    53


# 케이스마다 갯수 말고 비율로 알아보기
# 정규화 (normalize)
print(f"=== 정규화 (normalize) ===\n {df["result"].value_counts(normalize=True)}")
#  result
# 정상    0.558333
# 고장    0.441667h


# 정규화 비율 결과를 위와 같이 쓰기보다는 round 처리로 반올림 할 때가 많다
print(f"=== round 정규화 ===\n {df["result"].value_counts(normalize=True).round(3)}")
#  result
# 정상    0.558
# 고장    0.442
