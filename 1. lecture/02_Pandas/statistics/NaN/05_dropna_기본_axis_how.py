# -*- coding: utf-8 -*-
"""
[05] dropna 기본 - axis / how

dropna()
= 결측이 있는 행 또는 열을 제거

기본
df.dropna()
-> 결측이 하나라도 있는 "행 전체" 삭제

axis
axis=0 -> 행 삭제
axis=1 -> 열 삭제

how
how="any" -> 하나라도 결측이면 삭제 (기본값)
how="all" -> 전부 결측일 때만 삭제

중요
dropna()는 NaN 칸 하나만 없애는 것이 아니라
그 행/열 전체를 없앨 수 있음.

주의
결측이 여러 컬럼에 흩어져 있으면
기본 dropna()로 데이터가 크게 줄어들 수 있음.

원본 보존 권장:
clean = df.dropna()
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "온도": [30, np.nan, 35],
    "압력": [100, 101, np.nan],
    "진동": [2.1, 2.2, 2.3]
})

print("원본")
print(df)

print("\n1) 결측 있는 행 삭제")
print(df.dropna())

print("\n2) 결측 있는 열 삭제")
print(df.dropna(axis=1))

print("\n3) 전부 결측인 행만 삭제")
print(df.dropna(how="all"))
