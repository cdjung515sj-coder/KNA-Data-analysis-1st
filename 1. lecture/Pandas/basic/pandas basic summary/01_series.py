# ============================================
# Pandas Series 정리
# 순서:
# 1. Series 개념
# 2. Series 만들기
# 3. index 구조
# 4. 속성
# 5. 원소 선택
# 6. Series 객체를 만드는 특수한 방법
# 7. Series 활용
# ============================================

import pandas as pd
import numpy as np


# ============================================
# 1. Series 개념
# ============================================

# Series
# - Pandas의 1차원 자료구조
# - 각 값(value)에 index가 붙어 있음
# - 구조: index + value

s = pd.Series([10, 20, 30])

print("기본 Series")
print(s)

# 출력 형태
# 0    10
# 1    20
# 2    30
# dtype: int64


# ============================================
# 2. Series 만들기
# ============================================

# pd.Series()를 사용해 Series 객체 생성

s1 = pd.Series([10, 20, 30])

print("\n리스트로 Series 만들기")
print(s1)


# index를 직접 지정할 수도 있음

s2 = pd.Series(
    [78, 82, 91],
    index=["모터", "펌프", "밸브"]
)

print("\nindex를 지정한 Series")
print(s2)


# ============================================
# 3. Series의 index 구조
# ============================================

# Series는 index와 value로 구성됨

# index       value
# 모터   ->    78
# 펌프   ->    82
# 밸브   ->    91

# index를 지정하지 않으면
# 0, 1, 2, ... 형태의 기본 index가 자동 생성됨

s3 = pd.Series([100, 200, 300])

print("\n기본 index")
print(s3)


# 직접 index 지정

s4 = pd.Series(
    [100, 200, 300],
    index=["A", "B", "C"]
)

print("\n사용자 지정 index")
print(s4)


# ============================================
# 4. Series 속성
# ============================================

s = pd.Series(
    [78, 82, 91],
    index=["모터", "펌프", "밸브"]
)

print("\nSeries 속성")

print("index:", s.index)      # index 확인
print("values:", s.values)    # 실제 값 확인
print("dtype:", s.dtype)      # 데이터 자료형
print("size:", s.size)        # 원소 개수
print("shape:", s.shape)      # 크기

# 주의
# 속성(attribute)은 ()를 붙이지 않음

# s.size      # O
# s.size()    # X


# ============================================
# 5. Series 원소 선택
# ============================================

s = pd.Series(
    [78, 82, 91],
    index=["모터", "펌프", "밸브"]
)

# loc
# -> index 이름으로 선택

print("\nloc으로 선택")
print(s.loc["모터"])


# iloc
# -> 위치 번호로 선택

print("\niloc으로 선택")
print(s.iloc[0])


# 여러 원소 선택

print("\n여러 index 선택")
print(s.loc[["모터", "밸브"]])


# 위치 범위 선택

print("\n위치 범위 선택")
print(s.iloc[0:2])


# 핵심
# loc  -> index 이름
# iloc -> 위치 번호


# ============================================
# 6. Series 객체를 만드는 특수한 방법
# ============================================

# --------------------------------------------
# 6-1. 딕셔너리로 만들기
# --------------------------------------------

data = {
    "모터": 78,
    "펌프": 82,
    "밸브": 91
}

s_dict = pd.Series(data)

print("\n딕셔너리로 Series 만들기")
print(s_dict)

# dictionary key   -> Series index
# dictionary value -> Series value


# --------------------------------------------
# 6-2. 하나의 값으로 여러 원소 만들기
# --------------------------------------------

s_scalar = pd.Series(
    10,
    index=["A", "B", "C"]
)

print("\n하나의 값으로 여러 원소 만들기")
print(s_scalar)

# 결과
# A    10
# B    10
# C    10


# --------------------------------------------
# 6-3. NumPy 배열로 만들기
# --------------------------------------------

arr = np.array([10, 20, 30])

s_numpy = pd.Series(arr)

print("\nNumPy 배열로 Series 만들기")
print(s_numpy)


# ============================================
# 7. Series 활용
# ============================================

# 실제 Pandas에서는
# DataFrame에서 열 하나를 선택했을 때
# Series를 가장 자주 만나게 됨

df = pd.DataFrame({
    "설비": ["A", "B", "C", "D"],
    "온도": [65, 78, 85, 92],
    "압력": [10, 15, 18, 21]
})

print("\nDataFrame")
print(df)


# --------------------------------------------
# 7-1. DataFrame의 한 열 선택
# --------------------------------------------

temp = df["온도"]

print("\n온도 Series")
print(temp)

# df["온도"]
# -> Series

# df[["온도"]]
# -> DataFrame


# --------------------------------------------
# 7-2. 기본 통계
# --------------------------------------------

print("\n온도 평균:", temp.mean())
print("온도 최댓값:", temp.max())
print("온도 최솟값:", temp.min())
print("온도 합계:", temp.sum())
print("온도 개수:", temp.count())


# --------------------------------------------
# 7-3. 조건 만들기
# --------------------------------------------

condition = temp >= 80

print("\n80도 이상 조건")
print(condition)

# Series에 조건을 적용하면
# True / False로 이루어진 Boolean Series가 만들어짐


# --------------------------------------------
# 7-4. Boolean Series로 필터링
# --------------------------------------------

result = df[condition]

print("\n80도 이상 데이터")
print(result)


# ============================================
# 최종 핵심 정리
# ============================================

# Series
# -> index + value로 이루어진 1차원 자료구조

# pd.Series()
# -> Series 생성

# s.index
# -> index 확인

# s.values
# -> 실제 값 확인

# s.dtype
# -> 자료형 확인

# s.size
# -> 원소 개수

# s.shape
# -> 크기

# s.loc["이름"]
# -> index 이름으로 선택

# s.iloc[0]
# -> 위치 번호로 선택

# df["온도"]
# -> DataFrame에서 열 하나 선택
# -> 결과는 Series

# df["온도"] >= 80
# -> Boolean Series

# df[df["온도"] >= 80]
# -> 조건을 만족하는 행 필터링