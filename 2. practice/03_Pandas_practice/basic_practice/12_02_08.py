# 실습 8. 압축기와 디지털 신호 구조 비교
# data/12_metro_compressor.csv
# data/12_metro_digital.csv
# shape, info, describe 활용

import pandas as pd

df_metro_compressor = pd.read_csv("data/12_metro_compressor.csv")
print(df_metro_compressor.shape)
print(df_metro_compressor.info())
print(df_metro_compressor.describe())

df_metro_digital = pd.read_csv("data/12_metro_digital.csv")
print(df_metro_digital.shape)
print(df_metro_digital.info())
print(df_metro_digital.describe())


# 2. info() 결과 기반 결측치 및 상태 차이 분석

"""df_metro_compressor (압축기 데이터):
  총 200행 중 오일온도 열에서 결측치 1개(199 non-null) 존재.
  연속형 수치(압력, 온도, 전류 등) 데이터가 주를 이룸.
- df_metro_digital (디지털 신호 데이터):

  총 120행으로 결측치는 없으나(모두 120 non-null), 저압스위치 열의 모든 값이 0(std=0)임.
  0/1 형태의 디지털 상태값(스위치/타워 온오프 등)으로 이루어져 있음."""


# 3. 데이터 분석 가능 여부 및 전처리 필요성 판단
"""
- df_metro_compressor (압축기 데이터): [바로 분석 가능]
  * 오일온도 결측치 1개를 단순 대체/제거 후 즉시 통계 분석, 이상치 탐지, 시계열 경향성 분석에 활용 가능.

- df_metro_digital (디지털 신호 데이터): [추가 정리 필요]
  * 모든 수치가 0인 '저압스위치' 컬럼처럼 변동성이 없는 열은 분석적 가치가 없어 제거 대상임.
  * 0과 1로 구성된 범주형 디지털 신호 특성상 단독 통계량(describe)보다는 압축기 데이터와 시각(측정시각)을 기준으로 병합(Merge)하는 전처리 정리가 필수적임.
"""
