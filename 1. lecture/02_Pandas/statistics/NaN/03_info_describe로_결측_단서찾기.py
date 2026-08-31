# -*- coding: utf-8 -*-
"""
[03] info(), describe()로 결측 단서 찾기

df.info()
- 전체 행 수
- 컬럼명
- non-null count
- dtype 확인

예:
전체 250행인데 non-null 216
-> 결측 34개

df.describe()
- count : 결측 제외한 값 개수
- mean  : 평균
- std   : 표준편차
- min   : 최솟값
- max   : 최댓값

중요
min=-999, max=9999처럼 비현실적인 값이 있으면
위장 결측 또는 이상값을 의심.

주의
head() 앞부분에 NaN이 안 보인다고
전체 데이터에 결측이 없다고 판단하면 안 됨.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "온도": [30, 31, np.nan, 33, 34],
    "진동": [2.1, 2.3, -999, 2.2, 2.4]
})

print(df.head())
print()
df.info()

print("\n기초 통계")
print(df.describe())
