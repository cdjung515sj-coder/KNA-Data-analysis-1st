# 공장 - 공정 - 설비 - 일련번호 - 계측값
tag = "PL1-SNT-FAN-01-VIB"

parts = tag.split("-")
print(parts)  # ['PL1', 'SNT', 'FAN', '01', 'VIB']

# - 기준으로 나눈 결과 문자열을 변수에 따로 저장
plant = parts[0]  # 공장
process = parts[1]  # 공정
equip = parts[2]  # 설비
unit_no = parts[3]  # 일련번호
measure = parts[4]  # 측정항목

print(plant, process, equip, unit_no, measure)  # PL1 SNT FAN 01 VIB


# 공정 데이터 규칙
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

# 전로를 출력하려면?
print(PROCESS_KR["BOF"])  # 오타나 없으면 오류가 발생함

# 없는 태그 가져오는 것 방지
print(
    PROCESS_KR.get("BOF", "미등록")
)  # 없는 태그를 가져오는 것을 방지하기 위해 get 함수를 사용하는 것이 좋음


# 계측항목 규칙표
MEASER_KR = {
    "VIB": "진동",
    "CUR": "전류",
    "TMP": "온도",
    "PRS": "압력",
    "FLW": "유량",
    "SPD": "속도",
    "LVL": "레벨",
}

# 압력 값을 알고싶음
print(MEASER_KR.get("PRS", "미등록"))

# CSV 데이터를 읽어 어떤 형태로 있는지 알아보자

import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")

# (행 개수, 열 개수) 값을 알고 싶음
print(df.shape)  # (24,4)

print(df.columns.tolist())  # ['tag', 'unit', 'sample_value', 'note']

# 공정별로 몇 개의 태그가 있는지 세어보자
# 고로
# 냉간압연
