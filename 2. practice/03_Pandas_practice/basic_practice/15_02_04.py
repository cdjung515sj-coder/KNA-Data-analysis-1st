# 삭제 방식별 남는 행 수와 손실률을 표로 비교
# 실습 4. 삭제 손실 비교
import pandas as pd

df_imp_2 = pd.read_csv("data/15_02_Injection_Molding_process.csv", encoding="utf-8")
df_imp_2.info()

# 목표
# 삭제 방식별 남는 행 수와 손실률을 표로 비교


# 단계
# · 원본·행삭제·thresh 각 방식의 남는 행 수 구하기
# thresh를 사용하면 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기
# -> 40% 이상 NaN으로 채워진 컬럼 목록

# 방식 1) 고급 기술로 DF 이해도와 경험 숙련도가 올라야 쉽게 사용할 수 있음
비교 = pd.DataFrame(
    {
        "방식": ["원본", "행삭제", "thresh20"],
        "행": [len(df_imp_2), len(df_imp_2.dropna()), len(df_imp_2.dropna(thresh=20))],
    }
)

print(비교)
#          방식          행
# 0        원본         250
# 1       행삭제         76
# 2      thresh20       162

비교["손실률"] = ((1 - 비교["행"] / len(df_imp_2)) * 100).round(1)

print(비교)
#          방식    행   손실률
# 0        원본  250   0.0
# 1       행삭제   76  69.6
# 2  thresh20  162  35.2

# 방식 2) 방식별 삭제 후 남은 행 수 구하기
# 원본 : 삭제 전 전체 행 수
original_rows = len(df_imp_2)
# 행삭제(dropna) 를 사용하여 결측치 1개라도 있으면 행 전부 삭제
rows_dropna = len(df_imp_2.dropna())
# thresh20 : 값이 최소 20개 이상 있는 행 남기기
rows_thresh = len(df_imp_2.dropna(thresh=20))

# 손실률 계산
loss_original = round(((1 - original_rows / len(df_imp_2)) * 100), 1)
loss_dropna = round(((1 - rows_dropna / len(df_imp_2)) * 100), 1)
loss_thresh = round(((1 - rows_thresh / len(df_imp_2)) * 100), 1)

# · 방식과 행 수를 하나의 표로 모으기
result = pd.DataFrame(
    {
        "방식": ["원본", "행삭제", "thresh20"],
        "행": [original_rows, rows_dropna, rows_thresh],
        "손실률": [loss_original, loss_dropna, loss_thresh],
    }
)


# · 원본 대비 손실률을 백분율로 계산해 나란히 보기
print(result)

#          방식    행   손실률
# 0        원본  250   0.0
# 1       행삭제   76  69.6
# 2  thresh20  162  35.2

# 예상 결과
# 행삭제 손실 약 69.6%, thresh 손실 약 35.2%
