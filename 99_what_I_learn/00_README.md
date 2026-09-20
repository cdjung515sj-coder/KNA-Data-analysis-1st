# 배운 코드: 개념 · 사용법 · 여러 풀이

원본 강의·실습·요약 자료를 바탕으로 **처음부터 다시 만든 실행형 노트북**입니다. 위에서 아래로 실행하면 작은 예제의 입력과 출력이 이어집니다. 각 절은 **코드 → 코드 개념 → 사용법 → 같은 결과의 다른 방법과 선택 이유** 순서로 구성했습니다.

| 순서 | 노트북 | 찾을 내용 |
|---|---|---|
| 01 | [Python 기본 문법과 자료형](01_python_basics.ipynb) | 출력, 변수, 연산자, 문자열, 리스트·튜플·집합·딕셔너리, 입력·예외 |
| 02 | [조건문·반복문·함수·파일](02_control_functions_io.ipynb) | `if`, `for`, `while`, `break`, `continue`, `def`, 파일 입출력 |
| 03 | [NumPy 배열과 계산](03_numpy_arrays.ipynb) | 배열 생성, 인덱싱, 슬라이싱, 불리언 마스크, 축, 브로드캐스팅 |
| 04 | [Pandas 표 탐색과 선택](04_pandas_essentials.ipynb) | `read_csv`, `head`, `info`, `loc`, `iloc`, 필터, 정렬, 구간화 |
| 05 | [Pandas 집계와 통계](05_pandas_group_stats.ipynb) | `value_counts`, `groupby`, `agg`, `transform`, `apply`, 분산, 상관 |
| 06 | [데이터 전처리](06_data_cleaning.ipynb) | 위장된 결측, 삭제·대체, 중복, IQR 이상치 |
| 07 | [데이터 품질과 설비 이상](07_quality_analysis.ipynb) | 품질 요약, Z-score, 설비별 기준, 정밀도·재현율 |
| 08 | [시각화](08_visualization.ipynb) | Matplotlib, Seaborn, 추세·분포·그룹 비교·관계 그래프 |
| 09 | [시계열 분석](09_time_series.ipynb) | 시간 변환, `asfreq`, `resample`, 보간, 이동 통계, 변화량 |
| 10 | [DuckDB와 SQL](10_duckdb_sql.ipynb) | `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `CASE`, `JOIN` |
| 11 | [설비 이상 탐지와 고장 예측](11_predictive_maintenance.ipynb) | Z-score, Isolation Forest, Random Forest, RUL, 정보 누출 |

## 같은 값을 여러 방법으로 구하는 이유

예를 들어 **설비별 평균**은 반복문, Pandas `groupby`, SQL `GROUP BY`로 구할 수 있습니다. 결과가 같아도 입력 규모와 후속 작업에 따라 선택이 달라집니다.

```python
# 계산 흐름을 직접 배우거나 그룹별 특수 처리가 필요할 때
result = {name: part["temperature"].mean() for name, part in df.groupby("machine")}

# 표에서 같은 계산을 모든 그룹에 반복하고 후속 분석할 때
result = df.groupby("machine")["temperature"].mean()
```

SQL은 큰 파일에서 필요한 행·열만 조회하거나 DB와 연결할 때 편합니다. 각 노트북에는 이런 선택 기준을 코드 옆에 적었습니다.

## 학습 순서와 실행

1. 01~05에서 Python과 표 계산을 익힙니다.
2. 06~09에서 실제 센서 데이터의 품질·전처리·시각화·시계열을 다룹니다.
3. 10~11에서 SQL 조회와 고장 예측으로 확장합니다.

노트북은 예제 데이터를 내부에서 만듭니다. 01~09는 Python·NumPy·Pandas·Matplotlib·Seaborn, 10은 DuckDB, 11은 scikit-learn이 필요합니다. 실제 파일을 쓰려면 현재 작업 폴더와 데이터 사전의 열 이름·단위를 확인하세요. 노트북 끝에 관련 원본 자료 링크가 있습니다.

## 범위

이 자료는 현재 저장소의 코드 중 자주 재사용되는 핵심 패턴을 학습용으로 재구성한 것입니다. 원본의 모든 실습 데이터를 그대로 복제하지 않고, 코드가 왜 그 결과를 내는지와 언제 다른 방법을 고를지에 집중했습니다. 새 내용을 추가할 때는 [build_notebooks.py](build_notebooks.py)를 수정한 뒤 실행하면 노트북을 다시 생성할 수 있습니다.
