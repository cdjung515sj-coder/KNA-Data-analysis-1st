# 실습 7. duplicated로 중복 찾기와 개수
# 목표
# 완전 중복 행을 찾고 keep 옵션에 따른 개수 비교
# 단계
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# · duplicated로 중복 행 여부를 참·거짓으로 표시
print(df.duplicated().sum()) # 2

# · sum으로 중복 개수 세고 중복 행 직접 확인
print(df[df.duplicated()])
#       샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 200   8  215.0  1038.0   20.9   11.0  258.0   0
# 201  89  235.0  1137.0   22.7   13.0  261.0   0


# · keep을 거짓으로 두면 겹친 행이 모두 표시되는 것 확인
print(df.duplicated(keep=False).sum()) # 4 : 겹친 행을 원본까지 모두 표시

# 예상 결과
# 완전 중복 2건, keep을 끄면 겹친 행 4건 표시
