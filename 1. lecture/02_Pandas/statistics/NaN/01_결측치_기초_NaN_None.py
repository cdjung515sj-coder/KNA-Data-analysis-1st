# -*- coding: utf-8 -*-
"""
[01] 결측치 기초 - NaN / None

핵심
- 결측치(Missing Value) = 원래 값이 있어야 하는데 값이 없는 상태
- Pandas에서는 주로 NaN으로 보임
- None도 Pandas에서 결측으로 인식할 수 있음

중요
0과 NaN은 다름
0   = 실제 값이 0
NaN = 값 자체가 없음

주의
- NaN을 0으로 무조건 바꾸면 안 됨
- 예: 온도 NaN -> 0으로 채우면 "온도 0도"라는 잘못된 정보가 됨
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "온도": [30, 35, np.nan, 40],
    "상태": ["정상", None, "정상", "정상"]
})

print(df)
print("\n결측 확인:")
print(df.isna())
