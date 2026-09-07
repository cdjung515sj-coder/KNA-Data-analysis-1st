"""
철강 설비 태그 분해 예제
- 태그를 다섯 요소로 분해
- 공정 코드를 한글명으로 매핑
- 상공정/하공정/유틸리티로 분류
- 공정별 태그 개수를 집계

강의 개념 연결:
01-01 철강 공정 개관 - 설비 태그 읽기
"""

import pandas as pd


# 실제 실습에서는 pd.read_csv("태그파일.csv")로 바꿔 사용하면 됩니다.
tags = pd.DataFrame(
    {
        "tag": [
            "PL1-SNT-FAN-01-VIB",
            "PL1-SNT-FAN-01-CUR",
            "PL1-BF-BLW-01-VIB",
            "PL1-BF-BLW-01-CUR",
            "PL1-CCM-PMP-02-PRS",
            "PL1-HRM-MTR-01-CUR",
            "PL1-HRM-MTR-01-VIB",
            "PL1-UTL-PMP-01-PRS",
            "PL1-XXX-FAN-01-VIB",  # 미등록 코드 예시
        ],
        "unit": ["mm/s", "A", "mm/s", "A", "bar", "A", "mm/s", "bar", "mm/s"],
    }
)

# 1) 하이픈 기준으로 다섯 마디 분해
split_cols = tags["tag"].str.split("-", expand=True)
split_cols.columns = ["plant", "process", "equipment", "unit_no", "measure"]

tags = pd.concat([tags, split_cols], axis=1)

# 2) 공정 코드 → 한글 공정명
process_map = {
    "SNT": "소결",
    "BF": "고로",
    "BOF": "제강",
    "CCM": "연주",
    "HRM": "열간압연",
    "CRM": "냉간압연",
    "UTL": "유틸리티",
}

tags["process_name"] = tags["process"].map(process_map).fillna("미등록")

# 3) 상공정/하공정/유틸리티 분류
stage_map = {
    "SNT": "상공정",
    "BF": "상공정",
    "BOF": "상공정",
    "CCM": "상공정",
    "HRM": "하공정",
    "CRM": "하공정",
    "UTL": "유틸리티",
}

tags["stage"] = tags["process"].map(stage_map).fillna("미등록")

print("=== 태그 분해 결과 ===")
print(tags)

print("\n=== 공정별 태그 개수 ===")
print(tags.groupby("process_name").size().sort_values(ascending=False))

print("\n=== 계측 항목별 개수 ===")
print(tags.groupby("measure").size().sort_values(ascending=False))

print("\n=== 분해 이상/미등록 확인 ===")
print(tags[tags["stage"] == "미등록"])
