# -*- coding: utf-8 -*-
"""
[07] fillna - 평균 / 중앙값 / 최빈값

fillna()
= 결측값을 다른 값으로 채움

수치형
- 고른 분포            -> 평균 mean()
- 치우침 / 이상치 존재 -> 중앙값 median()

범주형
- 최빈값 mode()

중요
평균과 중앙값을 둘 다 구해 비교하면 판단하기 쉬움.

평균과 중앙값이 비슷
-> 평균 대체 고려

차이가 큼
-> 치우침/이상치 의심
-> 중앙값 대체 고려

주의
센서값 결측을 무조건 0으로 채우지 말 것.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "온도": [30, 31, np.nan, 33, 34],
    "진동": [1, 2, 3, 4, 100],
    "제품유형": ["L", "L", np.nan, "M", "L"]
})

print("온도 평균:", df["온도"].mean())
print("온도 중앙값:", df["온도"].median())

# 평균 대체
df["온도"] = df["온도"].fillna(df["온도"].mean())

# 범주형 최빈값 대체
top = df["제품유형"].mode()[0]
df["제품유형"] = df["제품유형"].fillna(top)

print("\n처리 후")
print(df)
