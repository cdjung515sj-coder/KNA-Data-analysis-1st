# 실습 1. 설비 태그에서 공정 위치 추론
# 24개 태그를 읽어 공정과 상하공정 구분을 판정한 표 작성
# CASE A : 공정별로 묶어 태그가 가장 많은 공정 확인
# CASE B : 계측 항목별로 묶어 가장 많은 물리량 확인
import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")

PROCESS_KR = {
    "SNT": "소결",
    "CKO": "코크스",
    "BF": "고로",
    "BOF": "전로",
    "CCM": "연주",
    "HSM": "열간압연",
    "CRM": "냉간압연",
    "UTL": "유틸리티",
}

# 계측항목
MEASER_KR = {
    "VIB": "진동",
    "CUR": "전류",
    "TMP": "온도",
    "PRS": "압력",
    "FLW": "유량",
    "SPD": "속도",
    "LVL": "레벨",
}

split_cols = df["tag"].str.split("-", expand=True)
df["process"] = split_cols[1]
df["process_kr"] = df["process"].map(PROCESS_KR)


def get_process(tag):
    up_process = ["SNT", "CKO", "BF", "BOF"]
    down_process = ["CCM", "HSM", "CRM", "UTL"]

    if tag in up_process:
        return "상공정"
    elif tag in down_process:
        return "하공정"
    else:
        return "기타"


df["공정구분"] = df["process"].apply(get_process)

print(df[["tag", "process", "process_kr", "공정구분"]])

print("\n=== 공정구분 항목별 개수 ===")
print(df["공정구분"].value_counts())


df["measure"] = split_cols[4]
df["measure_kr"] = df["measure"].map(MEASER_KR)

measure_count = df.groupby("measure_kr").size().sort_values(ascending=False)

print("\n=== 계측 항목별 개수 ===")
print(measure_count)

print("\n=== 가장 많은 물리량 ===")
print(measure_count.idxmax(), measure_count.max())
