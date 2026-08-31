# -*- coding: utf-8 -*-
"""
[06] dropna 정밀 옵션 - subset / thresh

1) subset
df.dropna(subset=["불량여부"])

뜻
- 전체 컬럼을 보지 않고
- 지정한 컬럼의 결측만 기준으로 행 삭제

활용
- Target(정답) 컬럼
- 중요한 센서 컬럼

2) thresh
df.dropna(thresh=3)

뜻
- "정상값이 최소 3개 이상" 있는 행만 유지

매우 중요
thresh는 "결측 개수"가 아님.
thresh = 살아 있는 값의 최소 개수

주의
thresh=3
= 결측 3개면 삭제 ❌
= 정상값 3개 이상이면 유지 ⭕
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "온도": [30, np.nan, 35, 36],
    "압력": [100, 101, np.nan, 102],
    "진동": [2.1, np.nan, np.nan, 2.3],
    "불량여부": ["정상", "불량", np.nan, "정상"]
})

print("원본")
print(df)

print("\n1) 불량여부가 결측인 행만 삭제")
print(df.dropna(subset=["불량여부"]))

print("\n2) 정상값이 3개 이상인 행만 유지")
print(df.dropna(thresh=3))
