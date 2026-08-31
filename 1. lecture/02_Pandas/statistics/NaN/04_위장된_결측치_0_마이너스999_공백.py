# -*- coding: utf-8 -*-
"""
[04] 위장된 결측치

진짜 결측
- NaN
- None

위장 결측 예
- 0
- -999
- 999
- 9999
- ""
- "   "

중요
Pandas는 -999를 "진짜 숫자"로 계산할 수 있음.
그래서 평균/표준편차가 망가질 수 있음.

주의
0은 무조건 결측이 아님.
예:
가동 중 압력 0 -> 위장 결측 의심
정지 설비 속도 0 -> 정상값 가능

결국 "데이터 의미"를 보고 판단해야 함.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "압력": [100, 102, 0, 101],
    "진동": [2.1, -999, 2.4, 2.2],
    "설비명": ["A", "B", "   ", "D"]
})

print("원본")
print(df)

print("\n-999를 NaN으로 변환")
df["진동"] = df["진동"].replace(-999, np.nan)
print(df)

# CSV를 불러올 때부터 결측으로 인식시키는 방법
# df = pd.read_csv(
#     "data.csv",
#     na_values=[-999, 999]
# )

# 주의: 0을 무조건 na_values에 넣지 말 것.
