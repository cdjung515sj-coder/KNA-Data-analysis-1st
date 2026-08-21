# -*- coding: utf-8 -*-
"""
[02] 결측치 확인 - isna(), sum(), mean()

가장 중요하게 기억
df.isna()              -> 결측 위치
df.isna().sum()        -> 결측 개수
df.isna().mean()       -> 결측 비율
df.isna().mean() * 100 -> 결측 비율(%)

원리
True  = 1
False = 0

그래서 sum() -> True 개수 = 결측 개수
mean() -> True 비율 = 결측 비율

주의
df.isna()만 출력하면 "위치"를 보는 것.
개수를 보려면 반드시 .sum()을 붙임.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "온도": [30, np.nan, 35, np.nan],
    "진동": [0.5, 0.6, np.nan, 0.7]
})

print("1) 결측 위치")
print(df.isna())

print("\n2) 컬럼별 결측 개수")
print(df.isna().sum())

print("\n3) 컬럼별 결측 비율(%)")
print((df.isna().mean() * 100).round(1))

print("\n4) 전체 결측 개수")
print(df.isna().sum().sum())
