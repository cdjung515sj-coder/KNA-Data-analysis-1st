# 실습 10. 다른 현장(용접) 이상치·중복 종합 정제 (난이도 ⭐⭐⭐⭐ )
# 목표
# IQR 탐색부터 정제 데이터 저장까지 한 흐름으로
import pandas as pd

wf = pd.read_csv("data/16_welding.csv", encoding="utf-8")
tA = "통전전류"

# - 실무 용접 설비의 "통전전류" 컬럼에 IQR 규칙을 적용하여 이상 전류 경계선을 구하고, 약 14.8%의 불량 전류 샷을 정상범위로 보정(clip) 하는 정제 파이프라인입니다.
# - 그와 함께 중복 측정된 로그들을 제거하고 인덱스를 새롭게 정리하여 깨끗해진 최종 데이터를 "cleaned_welding.csv" 파일로 저장함으로써 전처리 과정을


# 단계
# · 용접 통전전류의 IQR 경계로 이상치 개수·비율 확인
q1, q3 = wf[tA].quantile(0.25), wf[tA].quantile(0.75)
lower, higher = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
m = (wf[tA] < lower) | (wf[tA] > higher)
print(int(m.sum()), round(m.mean() * 100, 1))  # 24건(14.8%)

# · clip으로 이상치를 보정하고 중복을 제거·정리
wf[tA] = wf[tA].clip(lower=lower, upper=higher)
wf = wf.drop_duplicates().reset_index(drop=True)

print(len(wf))

# · 정제한 데이터를 파일로 저장
wf.to_csv("data/cleaned_welding.csv", index=False, encoding="utf-8")

# 예상 결과
# 용접 통전전류 이상치 24건(14.8%), 보정·중복 제거 후 저장
