# -*- coding: utf-8 -*-
"""
[10] 결측치 처리 전체 흐름

가장 중요한 순서
확인 → 판단 → 처리 → 재확인

1. 불러오기
2. head(), info(), describe() 확인
3. isna().sum()으로 개수 확인
4. isna().mean()*100으로 비율 확인
5. 위장 결측 확인
6. 삭제/대체 판단
7. dropna()/fillna()/ffill()/bfill() 처리
8. shape + isna().sum().sum() 재확인
9. 새 파일로 저장

★ 결측 발견 즉시 dropna() 하지 말기.
먼저 어디에 얼마나 있는지 확인.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "온도": [30, np.nan, 32, 33],
    "압력": [100, 101, np.nan, 102],
    "불량여부": ["정상", "불량", "정상", np.nan]
})

# 1) 확인
print("원본 크기:", df.shape)
print("\n결측 개수")
print(df.isna().sum())

print("\n결측 비율(%)")
print((df.isna().mean() * 100).round(1))

# 2) 판단 + 처리
# Target 결측 행 제거
df = df.dropna(subset=["불량여부"])

# 입력값 결측은 중앙값으로 대체 예시
df["온도"] = df["온도"].fillna(df["온도"].median())
df["압력"] = df["압력"].fillna(df["압력"].median())

# 3) 재확인
print("\n처리 후 크기:", df.shape)
print("전체 결측 개수:", df.isna().sum().sum())
print(df)
