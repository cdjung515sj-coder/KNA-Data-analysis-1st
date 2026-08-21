# -*- coding: utf-8 -*-
"""
[08] ffill / bfill - 시계열 결측 대체

ffill()
= 바로 앞의 정상값으로 채움

bfill()
= 뒤쪽 정상값을 앞으로 당겨 채움

예:
73, NaN, NaN, 75
ffill()
-> 73, 73, 73, 75

중요
ffill/bfill은 "순서가 의미 있는 데이터"에서 사용.
설비 센서 시계열에서 자주 활용.

주의 1
시간 순서로 정렬 후 사용.

주의 2
결측이 너무 길게 이어지면
같은 값이 계속 복사되어 부자연스러울 수 있음.

주의 3
서로 다른 설비 데이터가 섞여 있으면
다른 설비 값으로 채워질 수 있으므로 그룹 구분 필요.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "측정시각": ["10:03", "10:01", "10:02", "10:04"],
    "온도": [75, 73, np.nan, np.nan]
})

print("정렬 전")
print(df)

df = df.sort_values("측정시각")
df["온도"] = df["온도"].ffill().bfill()

print("\n정렬 + ffill/bfill 후")
print(df)
