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


# =========================================================================================

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

STAGE_KR = {
    "SNT": "상공정",
    "CKO": "상공정",
    "BF": "상공정",
    "BOF": "상공정",
    "CCM": "하공정",
    "HSM": "하공정",
    "CRM": "하공정",
    "UTL": "유틸리티",
}

print("전체 행수 :", len(df))

# 새로운 컬럼 만들기
df[["plant", "process", "equip", "unit_no", "measure"]] = df["tag"].str.split(
    "-", expand=True
)

print(df.head(3))
#     tag  unit  sample_value            note plant process equip unit_no measure
# 0  PL1-SNT-FAN-01-VIB  mm/s           2.8      소결 주배풍기 진동   PL1     SNT   FAN      01     VIB
# 1  PL1-SNT-FAN-01-CUR     A         412.5      소결 주배풍기 전류   PL1     SNT   FAN      01     CUR
# 2  PL1-SNT-CNV-02-SPD   m/s           1.6  소결광 이송 컨베이어 속도   PL1     SNT   CNV      02     SPD

df["process_kr"] = df["process"].map(PROCESS_KR).fillna("미등록")
df["measure_kr"] = df["measure"].map(MEASER_KR).fillna("미등록")

print(df.head(3))

# 상공정 하공정 STAGE 컬럼 추가
df["stage"] = df["process"].map(STAGE_KR).fillna("미등록")

print(df.head(3))

# 상공정, 하공정 항목별 개수
process_count = df.groupby("stage")
print(process_count.size())
# stage
# 상공정     11
# 유틸리티     3
# 하공정     10

# 계측 항목별 개수
measure_count = df.groupby("measure_kr").size()
print(measure_count)
# measure_kr
# 속도    1
# 압력    5
# 온도    6
# 유량    3
# 전류    5
# 진동    4

print(measure_count.sort_values(ascending=False))
# measure_kr
# 온도    6
# 압력    5
# 전류    5
# 진동    4
# 유량    3
# 속도    1

print(measure_count.sort_values(ascending=False, kind="stable")) # kind="stable" 옵션을 추가하면 ㄱ,ㄴ,ㄷ 순서가 아닌 정해둔 순서로 나옴

print(measure_count.idxmax(), measure_count.max())


# ============================================================================
<실습1>

import pandas as pd

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
MEASURE_KR = {
    "VIB": "진동",
    "CUR": "전류",
    "TMP": "온도",
    "PRS": "압력",
    "FLW": "유량",
    "SPD": "속도",
    "LVL": "레벨",
}

# 공정별 하공정, 상공정 분류
STAGE_KR = {
    "SNT": "상공정",
    "CKO": "상공정",
    "BF": "상공정",
    "BOF": "상공정",
    "CCM": "상공정",
    "HSM": "하공정",
    "CRM": "하공정",
    "UTL": "유틸리티",
}

# 데이터 읽기
df = pd.read_csv("01-01_철강_공정_개관_설비태그.csv")
print("전체 행수:", len(df)) # 24

# dataframe 에 태그에 포함되어있는 정보 컬럼을 추가하기
# df의 tag를 '-' 기준으로 잘라서 각 컬럼에 순서대로 저장
df[["plant", "process","equip", "unit_no", "measure"]] = df["tag"].str.split("-", expand=True)

print(df.head())

# map을 통해서 딕셔너리의 키와 (process, measure) 연결
df["process_kr"]=df["process"].map(PROCESS_KR).fillna("미등록")
df["measure_kr"]=df["measure"].map(MEASURE_KR).fillna("미등록")

print(df.head())

# (문제 1번) 상공정, 하공정과 관련된 stage 컬럼 추가 
df["stage"]=df["process"].map(STAGE_KR).fillna("미등록")
print(df.head())

# groupby: stage 별로 같은 값을 가진 행끼리 묶고
# size: 개수세기
print(df.groupby("stage").size())
'''
stage
상공정     14
유틸리티     3
하공정      7
'''

# (문제 3번) 계측항목별 태그개수와 가장 많이 등장하는 물리량(계측항목) 출력해보기
measure_a=df.groupby("measure_kr").size().sort_values(ascending=False, kind="stable")

#idxmax(): 시리즈나 데이터프레임에서 최대값을 가진 인덱스를 반환
print(measure_a.idxmax())

###### sort_values()의 kind옵션 - 어떤 정렬 알고리즘 사용할지 지정
# stable: 값이 같은 경우 기존 순서를 유지하는 정렬 (안정 정렬)
# quicksort: 퀵정렬 사용하여 정렬 
# mergesort: 병합정렬 사용하여 정렬 
# heapsort: 힙정렬 사용하여 정렬
measure_b=df.groupby("measure_kr").size()
print(measure_b) # 정렬X
print('-------')

print(measure_a) # 정렬O