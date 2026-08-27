# # 실습 2. 임계값 넘는 설비 골라내기
# # 목표
# # 실제 제조 데이터에서 위험 임계값을 넘는 설비 추출
import pandas as pd

df_diecasting_small = pd.read_csv("data/13_diecasting_small.csv")
df_diecasting_small.info()  # <class 'pandas.DataFrame'> 데이터 값 출력됨

# # 단계
# # · 비스킷두께 열에 비교 연산자로 임계값 기준 조건 생성
condition = df_diecasting_small["비스킷두께"] >= 16
condition.info()
print(len(condition))  # 5개 출력됨
print(condition.head(3))


# # · 조건을 대괄호에 넣어 임계값 초과 설비만 추출
df_sub = df_diecasting_small[df_diecasting_small["비스킷두께"] >= 16]
df_sub.info()
print(len(df_sub))  # 5개 출력됨
print(df_sub)  # 2,12,17,22,27 주의 출력

# # · 결과에서 샷와 비스킷두께 열만 골라 확인
print(df_diecasting_small[["샷", "비스킷두께"]])

# # 예상 결과
# # 비스킷두께 16 이상 40건, 샷·비스킷두께 목록 출력
print(df_sub[["샷","비스킷두께"]])


# import pandas as pd

# df = pd.read_csv("data/13_diecasting_small.csv")
# df.info()  # <class 'pandas.DataFrame'>

# # 1. df['비스킷두께'] -> 시리즈 추출
# # 2. 추출된 시리즈 내용들이 16이상이면 True, 아니면 False -> Boolean Serise
# # 3. Boolean Serise와 비교해서 df 내용중에 True와 겹치는 행들을 추출 -> df_sub

# condition = df[df["비스킷두께"] >= 16]
# condition.info()
# print(len(condition))  #  5 개
# print(condition.head(3))
# #      샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# # 2    3  215.0  1040.0   20.7   21.0  253.0   주의
# # 12  13  265.0   596.0   33.9   19.0  354.0   주의
# # 17  18  265.0   596.0   33.7   19.0  357.0   주의

# # 위 내용이 너무 많은 컬럼을 보여주니, 샷과 비스킷도께 컬럼만 골라서 보여준다면?
# print(condition["샷"].head(3))
# print(condition["비스킷두께"].head(3))

# # 위처럼 두 컬럼을 각각 가져와 출력하면 보기 편하니
# print(condition[["샷", "비스킷두께"]].head(3))
# #      샷  비스킷두께
# # 2    3   21.0
# # 12  13   19.0
# # 17  18   19.0
