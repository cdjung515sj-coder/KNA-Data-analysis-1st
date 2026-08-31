import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

q1 = df["사이클타임"].quantile(0.25)
q3 = df["사이클타임"].quantile(0.75)

print(f"Q1 : {q1} , Q3 : {q3}")
# Q1 : 20.8 , Q3 : 35.925

iqr = q3 - q1

print("IQR : ", iqr)
# IQR :  15.124999999999996

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print("하한선 :", lower, "/ 상한선 :", upper)

# 상한선과 하한선을 이용해서 필터링할 조건을 만들 수 있다.
# 상한선~하한선 안쪽 : 정상범위로 판단
# 상한선과 하한선 바깥 : 이상치 판단

mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)
print(f"이상치 여부 목록 : {mask}")
print(f"이상치 개수 : {mask.sum}")
print(f"이상치 데이터 크기 : {df[mask].shape}")
print(f"정상 범위 데이터 크기 : {df[~mask].shape}")

df_clean = df[~mask]  # 이상치 제거
print(df_clean.shape)
print(f"전체 {len(df)}, 이상치 제거된 값 {len(df_clean)}")
print(df_clean["사이클타임"])


mask_ok = (df["사이클타임"] >= lower) & (df["사이클타임"] <= upper)
print(f"정상 범위 개수 : {mask_ok.sum()}개")
print(f"정상 범위 데이터 크기 : {df[mask_ok].shape}")  # 이 경우는 결측치를 제외함


# 이상치 개수와 비율
print(mask.sum())
print(round(mask.mean() * 100, 1))


# 경계값으로 보정하기
# cilp(lower, upper) 보정 : 하한보다 작으면 하한값, 상한보다 크면 상한값으로 강제 평탄화(Windsorizing)합니다.
#                           이때 lower, upper 값은 모두 하한선에 대한 값입니다.
df["사이클타임_clipped"] = df["사이클타임"].clip(lower=lower, upper=upper)
print(df["사이클타임_clipped"].agg(["min", "max", "mean", "std"]))

# 결측치로 바꿔 채우기
# - mask(조건) + fillna(중앙갑): 이상치를 일단 빈칸(NaN)으로 강제 변환한 뒤, 중앙값으로 부드럽게 채워 넣어 수치 왜곡을 줄인다.
s_masked = df["사이클타임"].mask(mask)
s_masked.info()
print(s_masked.head())
print(s_masked.isna().sum())  # 20개

s_fixed = s_masked.fillna(s_masked.median()) # 왜 중앙값으로 채우나? : 평균은 이상치에 
s_fixed.info()
print(s_fixed.head())
print(s_fixed.isna().sum())  # 0개

