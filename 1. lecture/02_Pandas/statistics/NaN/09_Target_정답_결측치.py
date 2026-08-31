# -*- coding: utf-8 -*-
"""
[09] Target(정답) 결측치는 따로 생각

입력값(X)
예:
온도, 압력, 진동

-> 상황에 따라 평균/중앙값/앞값 등으로 대체 가능

정답(Target, y)
예:
불량여부

-> 추측으로 채우면 가짜 정답을 모델에게 가르칠 수 있음.

핵심
정답(Target)이 결측인 행은
대체보다 해당 행 제거를 우선 고려.

활용
df.dropna(subset=["불량여부"])
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "온도": [30, 31, 32, 33],
    "진동": [2.1, np.nan, 2.3, 2.4],
    "불량여부": ["정상", "불량", np.nan, "정상"]
})

print("원본")
print(df)

clean = df.dropna(subset=["불량여부"])

print("\nTarget 결측 행 제거 후")
print(clean)
