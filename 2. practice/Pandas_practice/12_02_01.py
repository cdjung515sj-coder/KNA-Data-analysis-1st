# 실습 1. head, tail로 디지털 시노 살펴보기
import pandas as pd

# 다음 코드로부터 시작하세요
df = pd.read_csv("data/12_metro_digital.csv")

# 위 코드가 정상 시행되어 shape가 나오는지 부터 확인해보시고
# 적절한 숫자들의 줄을 정해서 .head()와 .tail()을 출력하세요.

# head와 tail 출력에서 NaN 위치가 보이는지도 확인해봅시다.

print(f"shape : {df.shape}")  # (120, 4)
print(f"상위 5개 행 : {df.head()}")
print(f"하위 5개 행 : {df.tail()}")

print(f"상위 10개 행 : {df.head(10)}")
print(f"하위 10개 행 : {df.tail(10)}")


# 1. head로 봤을 떄 열이 많아 가운데가 "..." 생략되는가?
""" 생략되지 않고 모두 보임"""

# 2. NaN이 보이는 열을 2-3개 찾기
""" 현재 출력 값에서는 보이지 않음"""

# 3. tail로 마지막 행의 인덱스 번호
""" 마지막 행의 인덱스는 199 """