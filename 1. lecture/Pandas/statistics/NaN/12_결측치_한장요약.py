# -*- coding: utf-8 -*-
"""
[12] 결측치 한 장 요약

[확인]
df.isna()
-> 어디가 비었나?

df.isna().sum()
-> 몇 개 비었나?

df.isna().mean() * 100
-> 몇 % 비었나?

[삭제]
df.dropna()
-> 결측 있는 행 삭제

df.dropna(axis=1)
-> 결측 있는 열 삭제

df.dropna(how="all")
-> 전부 결측인 행만 삭제

df.dropna(thresh=N)
-> 정상값 N개 이상인 행 유지

df.dropna(subset=["A"])
-> A컬럼 결측을 기준으로 행 삭제

[대체]
fillna(mean)
-> 수치형 + 고른 분포

fillna(median)
-> 수치형 + 이상치/치우침

fillna(mode)
-> 범주형

ffill()/bfill()
-> 시간 순서 데이터

[판단]
결측 일부 행 집중
-> 행 삭제 후보

특정 컬럼에 결측 집중
-> 열 삭제 후보

가벼운 결측
-> 대체 후보

Target 결측
-> 해당 행 제거 우선 고려

[마지막]
shape + isna().sum().sum()
-> 처리 결과 재검증
"""

print("결측치 핵심 한 장 요약")
