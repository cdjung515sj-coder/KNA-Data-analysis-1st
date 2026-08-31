import pandas as pd

df = pd.read_csv(
    "data/15_01_InjectionMolding_process.csv", encoding="utf-8", na_values=[-999, 999]
)
# na_values로 위장 결측 인식
# 처음부터 정리 · 다 불러온 뒤 일일이 바꾸는 것보다 간편, 실수도 적음
# 컬럼별 지정 · 컬럼마다 다른 값을 결측으로 지정 가능
# 주의 · 0처럼 정상값일 수도 있는 걸 무턱대고 넣으면 멀쩡한 0까지 사라짐

print(df.shape)
df.info()
print(df.describe())


print(f"=== isna() === \n {df.isna().sum()}")
print(f"=== notna() ===  \n {df.notna().sum()}")

# 각 컬럼별 NaN 개수를 계싼한 Serise를 대상으로 다시 합산 시키면
# => 전체 NaN 개수를 알 수 있음
print(df.isna().sum().sum())  # 475
