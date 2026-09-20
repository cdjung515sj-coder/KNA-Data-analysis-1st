"""Build the learning notebooks with a uniform code/concept/usage/alternatives format."""

from pathlib import Path
import json

ROOT = Path(__file__).parent


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.strip().splitlines(keepends=True)}


def code(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
            "source": text.strip().splitlines(keepends=True)}


def section(title, concept, usage, snippet, choices):
    return [md(f"## {title}\n\n**코드 → 코드 개념**: {concept}\n\n**코드 사용법**: {usage}"),
            code(snippet), md(f"**같은 결과를 얻는 방법과 선택 이유**\n\n{choices}")]


def write(name, title, intro, sections, source):
    cells = [md(f"# {title}\n\n{intro}\n\n> 위에서 아래로 실행하세요. 예제 데이터는 노트북 안에서 만듭니다. 코드 셀 아래의 출력으로 결과를 확인하고, 실제 데이터에서는 열 이름·단위·기간을 먼저 확인하세요.")]
    for item in sections:
        cells += section(*item)
    cells.append(md(f"## 원본 학습 자료\n\n{source}"))
    book = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 4}
    (ROOT / name).write_text(json.dumps(book, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


write("01_python_basics.ipynb", "01 · Python 기본 문법과 자료형",
      "출력 → 변수 → 자료형 → 문자열 → 컬렉션 순서로 읽습니다. 같은 결과를 만드는 문법을 비교해 이후 라이브러리 코드도 해석할 수 있게 합니다.", [
    ("출력과 변수", "`print`는 값을 보여 주고 `=`는 값을 이름에 저장한다. `==`는 같은지 비교한다.", "값을 바꾼 뒤 아래 셀을 다시 실행해 출력과 불리언 결과를 비교한다.",
     '''machine = "A-01"
temperature = 78.5
print(machine, temperature)
print(f"{machine}: {temperature:.1f} °C")
print(temperature == 78.5, type(temperature))''',
     "- `print(machine, temperature)`는 빠른 점검에 편하다. `f\"...\"`는 단위와 소수 자리까지 표시하는 보고 문구에 좋다.\n- `type()`은 계산 결과가 문자열인지 숫자인지 헷갈릴 때 확인한다. `78.5`와 `\"78.5\"`는 다르다."),
    ("연산자와 형 변환", "`/`는 실수 나눗셈, `//`는 몫, `%`는 나머지다. `int`·`float`는 자료형을 바꾼다.", "문자열로 읽은 센서 값을 숫자로 바꾼 뒤 평균을 낸다.",
     '''raw = ["70", "80", "90"]
numbers = [float(x) for x in raw]
print(sum(numbers) / len(numbers))
print(7 / 2, 7 // 2, 7 % 2)
print(2 ** 3, 10 >= 8)''',
     "- `float(x)`는 소수가 있는 측정값에, `int(x)`는 정수 코드에 쓴다. 숫자가 아닌 문자열은 오류가 나므로 실제 파일에는 변환 실패 처리도 필요하다.\n- 평균을 직접 계산하는 방식은 원리를 보기에 좋고, Pandas의 `.mean()`은 표의 결측을 처리하며 열별 집계에 편하다."),
    ("문자열", "문자열은 순서가 있는 문자들의 모음이다. 인덱스·슬라이스·메서드로 가공한다.", "태그의 양끝 공백을 없애고 구분자로 분리한다.",
     '''tag = "  LINE-A-TEMP  "
clean = tag.strip()
print(clean, clean.lower(), clean.split("-"))
print(clean[:4], clean.replace("TEMP", "VIB"))''',
     "- `strip()`은 양끝 공백만 제거한다. 중간 공백까지 없애려면 `replace()`를 쓰되 식별자의 의미를 바꾸지 않는지 본다.\n- `split('-')`은 단순 구분자에 적합하다. 형식이 여러 가지면 규칙 검증이나 정규표현식이 필요하다."),
    ("리스트와 슬라이싱", "리스트는 순서가 있고 수정 가능하다. `a:b`는 a부터 b 직전까지 선택한다.", "측정값 추가·정렬·부분 선택을 비교한다.",
     '''values = [75, 70, 90]
values.append(80)
print(values[0], values[-1], values[1:3])
print(sorted(values), values)  # 원본 보존
values.sort()                  # 원본 변경
print(values)''',
     "- `sorted(values)`는 새 목록이 필요할 때, `values.sort()`는 원본을 바꿔도 될 때 쓴다. `sort()`의 반환값은 `None`이다.\n- `values[1:3]`과 `values[:2]`는 같은 결과가 될 수 있지만 전자는 시작·끝 위치를 명시하고 후자는 맨 앞부터라는 의도를 드러낸다."),
    ("튜플·집합·딕셔너리", "튜플은 고정된 순서, 집합은 중복 없는 원소, 딕셔너리는 키와 값의 대응이다.", "설비 코드와 측정값을 목적에 맞는 자료형에 담는다.",
     '''pair = ("A", 80)
machines = ["A", "B", "A"]
record = {"machine": "A", "temperature": 80}
print(pair[0], set(machines), record["temperature"])
print(list(dict.fromkeys(machines)))  # 처음 등장한 순서대로 중복 제거''',
     "- `set(machines)`는 중복을 없애지만 순서를 보존해야 하는 출력에는 적합하지 않다. `dict.fromkeys`는 처음 등장 순서를 유지한다.\n- 이름으로 값을 찾는 데이터는 딕셔너리, 고정된 두 값의 묶음은 튜플이 자연스럽다."),
    ("입력과 예외", "`input()`은 문자열을 돌려준다. `try/except`는 변환 실패를 처리한다.", "아래 함수에 정상 입력과 잘못된 입력을 각각 넣어 본다.",
     '''def parse_temperature(text):
    try:
        return float(text.strip())
    except ValueError:
        return None

print(parse_temperature(" 82.5 "), parse_temperature("error"))''',
     "- 작은 함수로 분리하면 대화형 `input()` 없이도 테스트할 수 있다. 직접 `float(input())`을 쓰면 간단하지만 잘못된 입력에 실행이 멈춘다.\n- 실패를 `None`으로 돌려주면 0°C와 결측을 구분할 수 있다."),
], "[`1. lecture/00_basic`](../1.%20lecture/00_basic), [`4. Summary/01_basic`](../4.%20Summary/01_basic)")


write("02_control_functions_io.ipynb", "02 · 조건문, 반복문, 함수, 파일",
      "같은 계산을 직접 반복, 컴프리헨션, 내장 함수, Pandas 중 어느 방식으로 표현할지 판단하는 기초입니다.", [
    ("조건문", "`if/elif/else`는 위에서부터 검사해 처음 맞는 분기를 실행한다.", "진동값을 세 수준으로 분류한다.",
     '''vibration = 3.4
if vibration >= 4.0:
    state = "danger"
elif vibration >= 3.0:
    state = "watch"
else:
    state = "normal"
print(state)
print("high" if vibration >= 3.0 else "low")''',
     "- 여러 단계면 `if/elif/else`가 읽기 쉽다. 두 결과 중 하나를 한 줄에서 선택하면 조건부 표현식이 간결하다.\n- `>= 4.0`을 먼저 검사해야 4 이상이 `watch`로 분류되지 않는다. 기준값은 설비 규격에 맞춰 정한다."),
    ("반복과 누적", "`for`는 각 값을 순회하고 `sum`은 합계를 계산한다.", "같은 초과 건수를 두 방식으로 얻는다.",
     '''values = [2.1, 3.5, 4.2, 2.8]
count = 0
for value in values:
    if value >= 3.0:
        count += 1
count2 = sum(value >= 3.0 for value in values)
print(count, count2)
assert count == count2''',
     "- `for`와 누적 변수는 계산 과정을 추적하거나 복잡한 조건을 넣을 때 좋다. `sum(조건 for ...)`는 단순 건수 계산에 좋다.\n- 표 데이터에서는 `(df['vibration'] >= 3).sum()`이 행별 연산을 한 번에 처리한다."),
    ("while, break, continue", "`while`은 조건이 참인 동안 반복한다. `break`는 종료, `continue`는 다음 회차로 이동한다.", "처음으로 위험 기준을 넘는 위치를 찾는다.",
     '''values = [None, 2.1, 3.5, 4.2]
position = 0
while position < len(values):
    value = values[position]
    position += 1
    if value is None:
        continue
    if value >= 4.0:
        break
print(position - 1, value)''',
     "- 인덱스를 직접 조절해야 할 때 `while`을 쓴다. 단순 순회는 `for index, value in enumerate(values)`가 종료 조건을 잊을 위험이 적다.\n- 검색 결과가 없을 수 있으면 반복 종료 후 별도 상태를 확인해야 한다."),
    ("함수, 매개변수, 반환", "함수는 반복되는 규칙을 이름으로 묶고 `return`으로 계산 결과를 돌려준다.", "비어 있는 입력을 처리하는 비율 함수를 만들고 재사용한다.",
     '''def exceedance_rate(values, threshold=3.0):
    valid = [x for x in values if x is not None]
    if not valid:
        return None
    return sum(x >= threshold for x in valid) / len(valid)

print(exceedance_rate([2.1, 3.5, None, 4.2]))
print(exceedance_rate([2.1, 3.5], threshold=4.0))''',
     "- 기본값은 자주 쓰는 기준을 제공하고 호출 시 바꿀 수 있다. 고정 기준을 함수 내부에 박아 두면 설비마다 적용하기 어렵다.\n- `print`는 보여 주기만 하고, `return`은 이후 계산에 재사용할 값을 만든다."),
    ("모듈과 파일 입출력", "`import`는 표준 라이브러리 기능을 가져온다. `with open`은 파일을 자동으로 닫는다.", "먼저 메모리 안의 파일로 쓰기·읽기를 연습한다. 실제 파일에는 `Path`를 쓴다.",
     '''from io import StringIO
from pathlib import Path

buffer = StringIO()
buffer.write("A,2.1\\nB,3.4\\n")
buffer.seek(0)
print(buffer.read().splitlines())
print(Path("data") / "notes.txt")''',
     "- `StringIO`는 파일을 만들지 않고 읽기·쓰기를 연습하거나 테스트할 때 좋다. 실제 작은 텍스트 파일은 `Path('notes.txt').write_text(text, encoding='utf-8')`와 `read_text(...)`로 처리한다. 큰 파일은 `with open(...)`으로 줄마다 읽는다.\n- 표 형태 CSV는 문자열 분리보다 `pd.read_csv`가 따옴표·결측·열 이름 처리를 잘한다."),
], "[`1. lecture/00_basic`](../1.%20lecture/00_basic), [`4. Summary/02_condition_loop`](../4.%20Summary/02_condition_loop)")


write("03_numpy_arrays.ipynb", "03 · NumPy 배열과 계산",
      "Python 목록에서 NumPy 배열로 넘어가며 인덱싱, 배열 생성, 모양, 축, 통계를 비교합니다.", [
    ("배열 만들기", "`np.array`는 기존 값을, `arange`는 간격 기준, `linspace`는 개수 기준으로 만든다.", "배열의 값·모양·자료형을 확인한다.",
     '''import numpy as np
a = np.array([2.0, 3.0, 4.0])
print(a, a.shape, a.ndim, a.size, a.dtype)
print(np.arange(0, 10, 2))
print(np.linspace(0, 8, 5))
print(np.zeros((2, 3)), np.ones((2, 2)))''',
     "- 정해진 간격이면 `arange`, 시작과 끝을 포함해 정해진 점 개수가 필요하면 `linspace`가 명확하다. 부동소수 간격은 `arange`의 끝점이 예상과 달라질 수 있다.\n- 빈 데이터 구조를 준비할 때 `zeros/ones`를 쓴다."),
    ("리스트와 배열 연산", "NumPy 산술은 원소별로 적용된다. Python 리스트의 `+`는 연결이다.", "같은 두 배 값을 반복문·컴프리헨션·배열로 만든다.",
     '''values = [2, 3, 4]
loop = []
for x in values:
    loop.append(x * 2)
comp = [x * 2 for x in values]
array = (np.array(values) * 2).tolist()
print(loop, comp, array)
assert loop == comp == array''',
     "- 소규모 일반 객체는 반복문이 유연하다. 숫자 대량 계산은 NumPy 벡터 연산이 간결하다.\n- `values * 2`는 `[2,3,4,2,3,4]`가 되므로 수치 계산과 혼동하지 않는다."),
    ("인덱싱과 슬라이싱", "`a[start:stop]`은 끝 위치 직전까지, 2차원 배열은 `[행, 열]`로 선택한다.", "센서 표의 첫 열과 마지막 두 행을 선택한다.",
     '''sensor = np.array([[70, 2.1], [75, 2.4], [82, 3.8]])
print(sensor[0, 1], sensor[:, 0], sensor[-2:, :])
print(sensor.reshape(1, 6).shape)''',
     "- `sensor[:, 0]`은 1차원 결과, `sensor[:, 0:1]`은 2차원 결과다. 후속 함수가 요구하는 모양에 따라 고른다.\n- `reshape`는 원소 수가 같을 때만 가능하며 데이터의 뜻까지 바꾸지는 않는다."),
    ("불리언 선택", "비교 연산은 참·거짓 마스크를 만들고, 마스크로 행을 선택한다.", "온도가 75 이상인 행을 찾는다.",
     '''mask = sensor[:, 0] >= 75
print(mask)
print(sensor[mask])
print(sensor[(sensor[:, 0] >= 75) & (sensor[:, 1] < 3)])''',
     "- NumPy에서 조건 결합은 `&`, `|`를 쓰고 각 비교를 괄호로 묶는다. Python의 `and/or`는 배열 전체의 진릿값을 결정할 수 없다.\n- 표에 열 이름이 있으면 Pandas의 `df.loc[...]`가 의미를 읽기 쉽다."),
    ("축과 통계", "`axis=0`은 행을 모아 열별 값, `axis=1`은 열을 모아 행별 값을 만든다.", "열별 평균·최댓값과 결측을 무시한 평균을 구한다.",
     '''print(sensor.mean(axis=0), sensor.max(axis=0))
with_missing = np.array([2.1, np.nan, 3.8])
print(np.mean(with_missing), np.nanmean(with_missing))
print(np.std([1, 2, 3], ddof=0), np.std([1, 2, 3], ddof=1))''',
     "- `np.mean`은 결측이 있으면 `nan`을 낸다. `np.nanmean`은 결측을 제외한다. 제외된 건수를 함께 기록한다.\n- `ddof=0`은 모집단 표준편차, `ddof=1`은 표본 표준편차다. Pandas `.std()` 기본값은 `ddof=1`이므로 비교 시 맞춘다."),
    ("브로드캐스팅과 표준화", "모양이 맞으면 작은 배열이 큰 배열의 각 행에 적용된다.", "서로 다른 단위의 센서 열을 열별로 표준화한다.",
     '''mean = sensor.mean(axis=0)
std = sensor.std(axis=0)
z = (sensor - mean) / std
print(z.round(2))
print(np.where(sensor[:, 1] >= 3.0, "watch", "normal"))''',
     "- `np.where`는 배열 전체를 두 결과로 나눌 때 좋다. 복잡한 여러 단계 조건은 `np.select`나 Pandas 분류 열이 읽기 쉽다.\n- 표준편차가 0인 열은 나눌 수 없다. 실제 분석에서는 상수 열을 먼저 확인한다."),
], "[`1. lecture/01_Numpy`](../1.%20lecture/01_Numpy), [`4. Summary/06_Numpy/Numpy.md`](../4.%20Summary/06_Numpy/Numpy.md)")


write("04_pandas_essentials.ipynb", "04 · Pandas 표 탐색과 선택",
      "열 이름으로 데이터를 읽고, 행과 열을 선택하고, 같은 결과를 만드는 표현을 비교합니다.", [
    ("표 만들기와 읽기", "DataFrame은 열 이름과 행 인덱스를 가진 2차원 표다.", "이 노트북의 예제 표를 만들고 기본 구조를 점검한다.",
     '''import pandas as pd
df = pd.DataFrame({
    "machine": ["A", "A", "B", "B", "B"],
    "cycle": [1, 2, 1, 2, 3],
    "temperature": [72, 83, 75, 80, 85],
    "vibration": [2.1, 3.5, 2.4, 2.9, 4.1],
})
print(df.head(), df.tail(2))
print(df.shape, df.columns.tolist(), df.dtypes)
df.info()
print(df.describe(include="all"))''',
     "- 실제 CSV는 `pd.read_csv('file.csv')`로 읽는다. `head`는 행 예시, `info`는 자료형과 비결측 수, `describe`는 분포를 본다. 서로 대체 관계가 아니라 다른 질문에 답한다.\n- `describe()`는 기본적으로 숫자 열만, `include='all'`은 문자 열도 요약한다."),
    ("Series와 DataFrame, loc와 iloc", "한 열 선택은 Series, 여러 열 선택은 DataFrame이다. `loc`는 라벨, `iloc`는 위치다.", "각 표현의 결과 형태를 비교한다.",
     '''print(type(df["temperature"]), type(df[["temperature"]]))
print(df.loc[df["machine"] == "A", ["cycle", "temperature"]])
print(df.iloc[:2, 1:3])
print(df["temperature"].iloc[0], df.loc[0, "temperature"])''',
     "- 이름을 알고 있으면 `loc`가 열의 의미를 보여 준다. 위치로 처음 n행·n열을 살필 때 `iloc`가 편하다. 인덱스가 0,1,2가 아니면 `loc[0]`과 `iloc[0]`은 다른 행일 수 있다.\n- 한 열이어도 2차원 입력이 필요한 모델에는 `df[['temperature']]`을 쓴다."),
    ("조건 필터링의 여러 표현", "불리언 Series는 각 행을 남길지 결정한다.", "75~85℃이고 설비 B인 행을 세 방식으로 찾는다.",
     '''a = df.loc[(df["temperature"] >= 75) & (df["temperature"] <= 85) & (df["machine"] == "B")]
b = df.loc[df["temperature"].between(75, 85) & df["machine"].isin(["B"])]
c = df.query("75 <= temperature <= 85 and machine == 'B'")
print(a, b, c, sep="\\n")
assert a.equals(b) and b.equals(c)''',
     "- `between`은 닫힌 구간을 간단히 표현하고 `isin`은 여러 값 중 하나를 고를 때 좋다.\n- `query`는 식이 길 때 읽기 쉽지만 공백·특수문자가 있는 열 이름은 백틱 처리해야 한다. 변수와 열 이름이 섞이면 `loc`가 더 분명하다."),
    ("정렬과 복사", "`sort_values`는 행 순서를 바꾼 새 표를 만든다. `.copy()`는 독립된 결과를 만든다.", "필터링한 행에 경고 열을 추가한다.",
     '''selected = df.loc[df["vibration"] >= 3].copy()
selected["warning"] = True
print(selected.sort_values(["machine", "vibration"], ascending=[True, False]))
print("원본 열:", df.columns.tolist())''',
     "- 원본이 필요하면 새 변수에 정렬 결과를 담는다. `inplace=True`보다 결과를 할당하는 방식이 데이터 흐름을 따라가기 쉽다.\n- 필터 결과에 값을 대입할 때 `.copy()`를 쓰거나 `df.loc[mask, 'warning'] = ...`로 원본에 직접 대입한다."),
    ("값 빈도와 구간화", "`value_counts`는 범주별 빈도를, `cut`은 연속값을 구간으로 바꾼다.", "설비 빈도와 진동 등급을 확인한다.",
     '''print(df["machine"].value_counts())
print(df["machine"].value_counts(normalize=True))
df["vibration_band"] = pd.cut(df["vibration"], bins=[0, 3, 4, float("inf")], labels=["normal", "watch", "danger"])
print(df[["vibration", "vibration_band"]])''',
     "- `normalize=True`는 건수 대신 비율을 준다. 설비마다 측정 건수가 다르면 비율과 건수를 같이 본다.\n- `pd.cut`은 미리 정한 물리적 기준에, `pd.qcut`은 데이터의 분위수로 비슷한 건수의 구간을 만들 때 쓴다. `cut` 경계의 포함 방향도 확인한다."),
], "[`1. lecture/02_Pandas/basic`](../1.%20lecture/02_Pandas/basic), [`4. Summary/07_Pandas`](../4.%20Summary/07_Pandas)")


write("05_pandas_group_stats.ipynb", "05 · Pandas 집계, 변환, 통계",
      "빈도·평균·분산·상관관계를 직접 계산과 Pandas 코드로 비교합니다.", [
    ("그룹별 건수", "`groupby`는 같은 키의 행을 묶는다. `size`는 행 수, `count`는 비결측 값 수다.", "결측이 있는 표에서 차이를 확인한다.",
     '''import pandas as pd
import numpy as np
df = pd.DataFrame({"machine": ["A", "A", "B", "B", "B"],
                   "vibration": [2.1, np.nan, 2.4, 2.9, 4.1],
                   "temperature": [72, 83, 75, 80, 85]})
print(df.groupby("machine").size())
print(df.groupby("machine")["vibration"].count())
print(df["machine"].value_counts())''',
     "- `value_counts`는 한 열의 빈도를 가장 빨리 본다. 여러 집계와 합쳐야 하면 `groupby().agg()`가 좋다.\n- 결측이 있으면 `size`와 `count`가 달라진다. 평균을 보고할 때 유효 표본 수도 함께 적는다."),
    ("그룹 요약과 여러 방법", "`agg`는 그룹별 결과를 한 행으로 축약하고 여러 통계를 동시에 구한다.", "직접 반복과 `groupby` 결과를 비교한다.",
     '''manual = {}
for name in df["machine"].unique():
    manual[name] = df.loc[df["machine"] == name, "temperature"].mean()
summary = df.groupby("machine").agg(n=("temperature", "size"),
                                     mean_temp=("temperature", "mean"),
                                     median_vibration=("vibration", "median"))
print(manual)
print(summary)
assert all(np.isclose(summary.loc[k, "mean_temp"], v) for k, v in manual.items())''',
     "- 반복문은 원리를 이해하거나 그룹마다 매우 다른 처리를 할 때 좋다. 같은 계산을 모든 그룹에 적용할 때 `groupby`가 간결하고 누락 위험이 적다.\n- 평균은 극단값에 민감하고 중앙값은 덜 민감하다. 둘을 함께 보면 치우침을 알 수 있다."),
    ("agg, transform, apply", "`agg`는 그룹을 줄이고 `transform`은 원래 행 수를 유지한다.", "각 행에 자기 설비의 평균과 편차를 붙인다.",
     '''df["machine_mean"] = df.groupby("machine")["temperature"].transform("mean")
df["deviation"] = df["temperature"] - df["machine_mean"]
print(df)
print(df.groupby("machine")["temperature"].apply(lambda s: s.max() - s.min()))''',
     "- 그룹 요약 표가 필요하면 `agg`, 각 행에 그룹 통계를 붙이면 `transform`을 쓴다.\n- `apply`는 내장 집계로 표현하기 어려운 사용자 정의 계산에 쓴다. 단순 평균·최대에는 내장 메서드가 의도도 분명하고 보통 더 빠르다."),
    ("분산·표준편차·사분위", "분산은 평균에서 떨어진 정도의 제곱 평균, 표준편차는 원래 단위의 변동성이다.", "표본 표준편차와 분위수를 확인한다.",
     '''x = df["temperature"]
print(x.mean(), x.median(), x.var(), x.std())
print(x.quantile([0.25, 0.5, 0.75]))
print(x.describe())''',
     "- `describe`는 한 번에 여러 통계를 살필 때 좋고, `.quantile()`은 특정 분위수만 정확히 계산할 때 쓴다.\n- Pandas 분산·표준편차 기본값은 `ddof=1`이다. NumPy 기본값과 다르므로 비교할 때 맞춘다."),
    ("상관계수와 해석", "Pearson 상관계수는 두 수치의 선형 동행 정도를 나타낸다.", "결측이 있는 열 쌍의 상관을 구한다.",
     '''print(df[["temperature", "vibration"]].corr())
print(df["temperature"].corr(df["vibration"]))
print(df[["temperature", "vibration"]].corr(method="spearman"))''',
     "- `.corr()` 행렬은 여러 센서를 한 번에 훑기 좋고, 두 Series의 `.corr()`는 특정 관계만 볼 때 좋다.\n- Pearson은 선형 관계, Spearman은 순위 기반 단조 관계를 본다. 상관은 원인을 증명하지 않으며 표본 수와 시간 추세를 함께 확인한다."),
], "[`1. lecture/02_Pandas/basic`](../1.%20lecture/02_Pandas/basic), [`1. lecture/02_Pandas/statistics`](../1.%20lecture/02_Pandas/statistics)")


write("06_data_cleaning.ipynb", "06 · 데이터 전처리",
      "원본 보존 → 품질 점검 → 변환 → 처리 전후 검증 순서로 결측, 중복, 이상치를 다룹니다.", [
    ("결측 찾기", "`isna`는 실제 결측을 찾는다. 빈 문자열·특수 숫자는 자동으로 결측이 아니다.", "열별 개수·비율과 위장된 결측을 확인한다.",
     '''import pandas as pd
import numpy as np
raw = pd.DataFrame({"machine": ["A", "A", "A", "B", "B"],
                    "time": [1, 2, 2, 1, 2],
                    "vibration": [2.1, "", "", -999, 15.0]})
print(raw.isna().sum())
raw["vibration"] = pd.to_numeric(raw["vibration"].replace({"": np.nan, -999: np.nan}), errors="coerce")
print(raw.isna().sum(), raw.isna().mean())''',
     "- `replace`는 알려진 오류 코드를 결측으로 바꾼다. `to_numeric(errors='coerce')`는 변환할 수 없는 모든 값을 결측으로 바꾸므로 무엇이 바뀌었는지 점검한다.\n- CSV 읽기 단계에서 `pd.read_csv(..., na_values=['', -999])`를 쓰면 같은 의도를 입력 시점에 반영할 수 있다."),
    ("행과 열 결측 점검", "`isna().sum(axis=1)`은 행마다, `isna().sum()`은 열마다 결측을 센다.", "삭제 후보 행과 필수 열 결측을 찾는다.",
     '''print(raw.isna().sum(axis=1))
print(raw.loc[raw["vibration"].isna()])
print(raw.dropna(subset=["vibration"]))
print(raw.dropna(thresh=3))''',
     "- `dropna(subset=...)`는 필수 열이 없는 행만 제거한다. `thresh=3`은 비결측 값이 3개 이상인 행을 남긴다. 전체 `dropna()`는 필요 없는 열의 결측 때문에 행을 과하게 없앨 수 있다.\n- 삭제 전후 건수와 설비별 분포를 비교한다."),
    ("중복 정의와 제거", "`duplicated`는 완전히 같은 행 또는 지정 키의 중복을 표시한다.", "설비·시간 조합의 중복을 확인하고 한 행만 남긴다.",
     '''print(raw.duplicated().sum())
print(raw.duplicated(["machine", "time"], keep=False))
dedup = raw.drop_duplicates(["machine", "time"], keep="first").copy()
print(len(raw), len(dedup))''',
     "- 전체 행 중복은 재수집된 복사본일 수 있고, 키 중복은 같은 시각의 재측정일 수 있다. 먼저 업무상 키를 정한다.\n- `keep='first'`는 현재 순서 기준이다. 수집 시각이나 품질 플래그가 있다면 먼저 정렬한다."),
    ("결측 대체의 여러 방법", "평균·중앙값·그룹별 중앙값·앞 값 채우기는 서로 다른 가정이다.", "전역 대체와 설비별 대체를 비교한다.",
     '''clean = dedup.copy()
clean["global_median"] = clean["vibration"].fillna(clean["vibration"].median())
clean["group_median"] = clean.groupby("machine")["vibration"].transform(lambda s: s.fillna(s.median()))
print(clean)
print(clean["group_median"].isna().sum())''',
     "- 평균은 대칭 분포에, 중앙값은 극단값이 있을 때 상대적으로 견고하다. 설비별 기준이 다르면 그룹별 대체가 자연스럽다.\n- 그룹 전체가 결측이면 그룹 중앙값도 결측이다. 임의의 0으로 채우지 말고 대체 규칙과 플래그를 정한다."),
    ("IQR 이상치 후보", "Q1과 Q3 사이 폭인 IQR을 이용해 검토할 범위를 만든다.", "상한·하한을 계산하고 후보를 표시한다.",
     '''x = pd.Series([2.1, 2.4, 2.8, 3.0, 3.2, 3.5, 15.0])
q1, q3 = x.quantile([0.25, 0.75])
lower, upper = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
mask = x.lt(lower) | x.gt(upper)
print(lower, upper, x[mask].tolist())
print(x.clip(lower=lower, upper=upper).tolist())''',
     "- `mask`는 원본을 보존하며 후보를 표시한다. `clip`은 값을 경계로 바꾸므로 실제 고장 급등을 숨길 수 있다.\n- IQR은 분포 기준이고 설비 안전 한계는 물리 기준이다. 원인 확인 전 자동 삭제하지 않는다."),
], "[`1. lecture/02_Pandas/statistics/NaN`](../1.%20lecture/02_Pandas/statistics/NaN), [`4. Summary/07_Pandas`](../4.%20Summary/07_Pandas)")


write("07_quality_analysis.ipynb", "07 · 데이터 품질과 설비 이상 분석",
      "품질 점검은 결측·중복·범위·시간 간격을 확인하는 단계입니다. Z-score와 변화 탐지는 그 다음에 적용합니다.", [
    ("품질 요약표", "품질 문제는 비율과 건수로 함께 기록해야 비교할 수 있다.", "간단한 센서 표에서 누락·중복·범위 위반을 센다.",
     '''import pandas as pd
import numpy as np
df = pd.DataFrame({"machine": ["A", "A", "A", "B", "B"],
                   "cycle": [1, 2, 2, 1, 2],
                   "vibration": [2.1, np.nan, np.nan, 2.5, 12.0]})
report = pd.Series({"rows": len(df),
                    "missing_vibration": df["vibration"].isna().sum(),
                    "duplicate_keys": df.duplicated(["machine", "cycle"]).sum(),
                    "outside_range": df["vibration"].gt(10).sum()})
print(report)
print("missing rate", df["vibration"].isna().mean())''',
     "- 건수는 작업량, 비율은 다른 기간·설비와의 비교에 좋다. 둘 다 보고한다.\n- `>10` 같은 범위는 장비 사양에 근거해야 한다. 통계적 이상치와 물리적으로 불가능한 값은 별도로 기록한다."),
    ("Z-score 두 방법", "Z-score는 평균에서의 거리를 표준편차 단위로 나타낸다.", "NumPy 수식과 Pandas 수식으로 같은 값을 계산한다.",
     '''x = pd.Series([2.0, 2.2, 2.4, 2.6, 2.8])
z_numpy = (x.to_numpy() - x.mean()) / x.std(ddof=0)
z_pandas = (x - x.mean()) / x.std(ddof=0)
print(z_numpy.round(2), z_pandas.round(2).tolist())
assert np.allclose(z_numpy, z_pandas)''',
     "- NumPy 배열은 수치 연산만 필요한 경우, Pandas Series는 행 인덱스를 유지하며 원본에 붙일 때 편하다.\n- `ddof`를 같게 지정해야 결과가 같다. 표본 표준편차와 모집단 표준편차의 차이도 기록한다."),
    ("설비별 기준과 강건한 점수", "설비마다 정상 수준이 다르면 전체 평균으로 표준화하면 오탐이 생긴다.", "그룹별 Z-score와 중앙값 기반 편차를 비교한다.",
     '''sample = pd.DataFrame({"machine": ["A"] * 4 + ["B"] * 4,
                        "vibration": [2.0, 2.1, 2.2, 3.5, 8.0, 8.1, 8.2, 9.5]})
group = sample.groupby("machine")["vibration"]
sample["z"] = group.transform(lambda s: (s - s.mean()) / s.std(ddof=0))
sample["from_median"] = group.transform(lambda s: s - s.median())
print(sample)''',
     "- 설비별 Z-score는 각 설비의 상대적 변화를 볼 때 좋다. 물리적으로 동일한 절대 한계를 적용해야 한다면 원래 단위의 기준도 유지한다.\n- 중앙값 기반 편차는 극단값 영향이 작지만 단위가 원래 값 그대로다. 정상 기준 기간을 먼저 고르는 것이 핵심이다."),
    ("혼동행렬과 품질 지표", "탐지 결과는 맞춘 수뿐 아니라 놓친 고장과 오경보를 나눠 평가한다.", "TP, FP, FN, TN과 정밀도·재현율을 직접 계산한다.",
     '''actual = np.array([0, 0, 1, 1, 1, 0])
pred = np.array([0, 1, 1, 0, 1, 0])
tp = ((actual == 1) & (pred == 1)).sum()
fp = ((actual == 0) & (pred == 1)).sum()
fn = ((actual == 1) & (pred == 0)).sum()
tn = ((actual == 0) & (pred == 0)).sum()
precision = tp / (tp + fp) if tp + fp else 0
recall = tp / (tp + fn) if tp + fn else 0
print(tp, fp, fn, tn, precision, recall)''',
     "- 정밀도는 경보 중 실제 고장의 비율, 재현율은 실제 고장 중 잡은 비율이다. 고장을 놓치는 비용이 크면 재현율을 중요하게 본다.\n- 정상 데이터가 많으면 정확도만 높아도 탐지가 쓸모없을 수 있다. 실제 운영에서는 경보당 점검 부담도 함께 본다."),
], "[`2. practice/06_Z-score`](../2.%20practice/06_Z-score), [`2. practice/07_domain_Predictive_Maintenance`](../2.%20practice/07_domain_Predictive_Maintenance), [`1. lecture/03_domain/steel_study_notes_final/code`](../1.%20lecture/03_domain/steel_study_notes_final/code)")


write("08_visualization.ipynb", "08 · Matplotlib과 Seaborn 시각화",
      "그래프를 예쁘게 만드는 것보다 질문에 맞는 그래프를 고르고 축·단위·표본 수를 정확히 보여 주는 데 집중합니다.", [
    ("그림과 축", "Figure는 전체 그림, Axes는 각 그래프의 좌표 영역이다.", "설비별 온도 추세를 같은 축에 그린다.",
     '''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame({"machine": ["A"] * 4 + ["B"] * 4,
                   "cycle": [1, 2, 3, 4] * 2,
                   "temperature": [70, 72, 75, 80, 69, 71, 74, 76],
                   "vibration": [2.0, 2.1, 2.5, 3.2, 1.8, 2.0, 2.2, 2.4]})
fig, ax = plt.subplots(figsize=(7, 3))
for name, part in df.groupby("machine"):
    ax.plot(part["cycle"], part["temperature"], marker="o", label=name)
ax.set(xlabel="Cycle", ylabel="Temperature (°C)", title="Temperature trend")
ax.legend(); ax.grid(alpha=0.3); fig.tight_layout(); plt.show()''',
     "- `plt.plot(...)`는 빠른 한 장에 편하다. `fig, ax = plt.subplots()`는 여러 그래프·축을 명확하게 제어할 때 좋다.\n- 시계열은 먼저 시간순 정렬한다. 선은 관측 사이가 이어진다는 느낌을 주므로 드문 관측이면 점도 함께 표시한다."),
    ("분포: 히스토그램과 상자그림", "히스토그램은 빈도 분포, 상자그림은 그룹의 중앙값과 사분위 범위를 보여 준다.", "같은 진동값을 두 관점으로 그린다.",
     '''fig, axes = plt.subplots(1, 2, figsize=(9, 3))
sns.histplot(data=df, x="vibration", bins=5, ax=axes[0])
sns.boxplot(data=df, x="machine", y="vibration", ax=axes[1])
fig.tight_layout(); plt.show()''',
     "- `plt.hist(df['vibration'])`는 배열만 있을 때 간단하다. `sns.histplot(data=df, x='vibration')`는 열 이름·범주 색을 붙이기 쉽다.\n- `bins`에 따라 모양이 달라 보일 수 있다. 상자그림의 수염 밖 점은 검토 후보이지 자동 삭제 대상이 아니다."),
    ("건수와 평균의 차이", "막대 높이가 건수인지 평균인지 구분해야 한다.", "설비별 행 수와 평균 진동을 나란히 그린다.",
     '''fig, axes = plt.subplots(1, 2, figsize=(9, 3))
sns.countplot(data=df, x="machine", ax=axes[0])
sns.barplot(data=df, x="machine", y="vibration", errorbar=None, ax=axes[1])
axes[0].set_title("Count"); axes[1].set_title("Mean vibration")
fig.tight_layout(); plt.show()''',
     "- `countplot`은 행 수를 센다. `barplot`은 기본적으로 평균을 계산한다. 이름이 비슷해도 값이 다르다.\n- 이미 집계된 표가 있다면 `ax.bar(summary.index, summary['mean'])`로 막대 높이를 명시하는 편이 안전하다."),
    ("산점도와 상관행렬", "산점도는 개별 관측의 모양, 상관행렬은 수치 관계의 요약을 보여 준다.", "두 센서의 관계를 점과 색으로 확인한다.",
     '''fig, axes = plt.subplots(1, 2, figsize=(9, 3))
sns.scatterplot(data=df, x="temperature", y="vibration", hue="machine", ax=axes[0])
corr = df[["temperature", "vibration"]].corr()
sns.heatmap(corr, annot=True, vmin=-1, vmax=1, cmap="coolwarm", ax=axes[1])
fig.tight_layout(); plt.show()''',
     "- `plt.scatter(x, y)`는 단순 두 배열에 편하다. `sns.scatterplot`은 `hue`로 설비별 패턴을 보기 좋다.\n- 상관행렬의 큰 값은 관계 후보일 뿐이다. 시간 추세나 설비 차이를 분리해 보고 인과관계로 단정하지 않는다."),
    ("저장과 표시", "`savefig`는 그림을 저장하고 `show`는 화면에 표시한다.", "메모리 버퍼에 PNG를 저장해 생성 여부를 확인한다.",
     '''from io import BytesIO
fig, ax = plt.subplots(figsize=(4, 2))
ax.plot([1, 2, 3], [2, 3, 4])
fig.tight_layout()
buffer = BytesIO()
fig.savefig(buffer, format="png", dpi=150, bbox_inches="tight")
print("PNG bytes:", len(buffer.getvalue()))
plt.close(fig)''',
     "- 실제 파일에는 `fig.savefig('trend.png', dpi=150, bbox_inches='tight')`를 `show()` 전에 호출한다. 메모리 버퍼는 디스크 파일 없이 저장 코드를 검증할 때 좋다.\n- 한글 글꼴은 실행 환경마다 다르므로 원본의 글꼴 설정 노트북을 참고한다."),
], "[`4. Summary/08_matplotlib`](../4.%20Summary/08_matplotlib), [`1. lecture/02_Pandas/matplotlib`](../1.%20lecture/02_Pandas/matplotlib)")


write("09_time_series.ipynb", "09 · 시계열 전처리와 추세·변동 분석",
      "시각, 주기, 결측 간격을 먼저 확인한 뒤 이동 통계와 변화량을 계산합니다.", [
    ("시간형 변환과 정렬", "문자열은 시간 연산 전에 `datetime`으로 바꿔야 한다.", "설비별 시간순 표를 만든다.",
     '''import pandas as pd
import numpy as np
raw = pd.DataFrame({"machine": ["A"] * 5,
                    "timestamp": ["2026-09-01 09:00:00", "2026-09-01 09:00:10", "2026-09-01 09:00:30", "2026-09-01 09:00:40", "2026-09-01 09:00:50"],
                    "vibration": [2.0, 2.2, 2.4, 3.1, 3.6]})
raw["timestamp"] = pd.to_datetime(raw["timestamp"], errors="coerce")
ts = raw.sort_values(["machine", "timestamp"]).set_index("timestamp")
print(ts.index.dtype, ts.head())''',
     "- 날짜 형식이 일정하면 `format=`을 지정해 예상 밖 형식을 잡는다. `errors='coerce'`는 실패값을 `NaT`로 바꾸므로 건수를 확인한다.\n- 실제 설비 ID가 여러 개면 설비별로 분리하거나 `groupby` 후 이동 통계를 계산한다."),
    ("간격 확인: asfreq와 resample", "`asfreq`는 시간격자를 만들고, `resample`은 구간 안의 관측을 집계한다.", "10초 결측과 30초 평균을 확인한다.",
     '''interval = ts.index.to_series().diff().dt.total_seconds()
grid = ts["vibration"].asfreq("10s")
half_minute = ts["vibration"].resample("30s").agg(["mean", "max", "count"])
print(interval, grid, half_minute, sep="\\n")''',
     "- 단순히 빠진 시각을 표시하려면 `asfreq`를 쓴다. 여러 측정값을 시간 구간별로 요약하려면 `resample`을 쓴다. 둘을 같은 것으로 보면 안 된다.\n- 평균은 급등을 숨기므로 최대와 건수도 같이 본다."),
    ("결측 채우기: 이전 값과 시간 보간", "`ffill`은 직전 값 유지, `interpolate(method='time')`은 양끝 값 사이를 시간에 따라 추정한다.", "한 칸만 채우고 어떤 위치를 채웠는지 기록한다.",
     '''forward = grid.ffill(limit=1)
linear_time = grid.interpolate(method="time", limit=1, limit_area="inside")
imputed = grid.isna() & linear_time.notna()
print(pd.DataFrame({"raw": grid, "ffill": forward, "time_interpolate": linear_time, "imputed": imputed}))''',
     "- 상태가 다음 측정까지 유지된다고 볼 때 `ffill`을 쓴다. 연속 물리량이 부드럽게 변한다고 볼 때 시간 보간을 고려한다.\n- 운전 중지·정비·긴 결측 구간은 채우면 실제 이벤트가 사라질 수 있다. 채운 값은 플래그로 남긴다."),
    ("이동평균과 이동표준편차", "이동평균은 국소 추세, 이동표준편차는 국소 변동성을 보여 준다.", "행 개수 창과 시간 길이 창을 비교한다.",
     '''ts["ma3"] = ts["vibration"].rolling(3, min_periods=3).mean()
ts["std3"] = ts["vibration"].rolling(3, min_periods=3).std()
ts["ma30s"] = ts["vibration"].rolling("30s").mean()
print(ts)''',
     "- `rolling(3)`은 최근 3개 관측, `rolling('30s')`는 최근 30초다. 측정 간격이 불규칙하면 두 결과가 달라진다.\n- `min_periods`를 작게 하면 초기 값도 나오지만 표본 수가 적어 비교가 불안정하다."),
    ("차분, 변화율, 설비 상태", "`diff`는 이전 값과의 차이, `pct_change`는 상대 변화율이다.", "진동의 급변 후보를 찾는다.",
     '''ts["diff"] = ts["vibration"].diff()
ts["pct"] = ts["vibration"].pct_change()
ts["jump"] = ts["diff"].abs() >= 0.5
print(ts[["vibration", "diff", "pct", "jump"]])''',
     "- 절대 변화량이 중요하면 `diff`, 단위와 기준값이 다른 설비를 비교하면 `pct_change`가 유용하다. 직전 값이 0에 가깝다면 변화율이 폭발하므로 주의한다.\n- 급변 기준은 정상 기간의 변화량 분포와 정비 이력을 함께 보고 정한다."),
], "[`4. Summary/08_matplotlib/03_TimeSeries_Data.ipynb`](../4.%20Summary/08_matplotlib/03_TimeSeries_Data.ipynb), [`04_TimeSeries_Preprocessing.ipynb`](../4.%20Summary/08_matplotlib/04_TimeSeries_Preprocessing.ipynb), [`05_Equipment_State_Analysis.ipynb`](../4.%20Summary/08_matplotlib/05_Equipment_State_Analysis.ipynb)")


write("10_duckdb_sql.ipynb", "10 · DuckDB와 SQL 조회",
      "Pandas로 작성한 결과와 SQL 결과를 비교하면서 조회, 필터, 집계, 조건 분류, 조인의 의미를 익힙니다. 이 노트북은 `duckdb` 패키지가 필요합니다.", [
    ("DataFrame 등록과 SELECT", "SQL의 `SELECT`는 열, `FROM`은 데이터 원천, `LIMIT`는 출력 행 수를 정한다.", "Pandas 표를 DuckDB에 등록해 조회한다.",
     '''import pandas as pd
import duckdb
df = pd.DataFrame({"machine": ["A", "A", "B", "B"],
                   "cycle": [1, 2, 1, 2], "vibration": [2.1, 3.5, 2.4, 4.1]})
con = duckdb.connect()
con.register("measurements", df)
print(con.execute("SELECT machine, vibration FROM measurements LIMIT 3").df())
print(df[["machine", "vibration"]].head(3))''',
     "- 이미 Python 표가 있으면 `register`로 SQL에서 사용한다. 파일에서 필요한 일부만 읽을 때는 `read_csv_auto('file.csv')`를 SQL의 `FROM`에 넣는다.\n- `LIMIT 3`은 처음 세 행을 보여 주지만 순서가 보장되어야 하면 `ORDER BY`를 추가한다."),
    ("WHERE와 ORDER BY", "`WHERE`는 집계 전 행을 거르고 `ORDER BY`는 결과를 정렬한다.", "진동 3 이상을 내림차순으로 뽑는다.",
     '''sql = con.execute("SELECT * FROM measurements WHERE vibration >= 3 ORDER BY vibration DESC").df()
pd_result = df.loc[df["vibration"] >= 3].sort_values("vibration", ascending=False).reset_index(drop=True)
print(sql, pd_result, sep="\\n")''',
     "- SQL은 파일·DB에서 필요한 행과 열만 먼저 줄이기 좋다. Pandas는 Python에서 후속 계산·그래프를 이어가기 좋다.\n- SQL `NULL` 비교는 `= NULL`이 아니라 `IS NULL` 또는 `IS NOT NULL`을 쓴다."),
    ("GROUP BY와 HAVING", "`GROUP BY`는 그룹 통계, `HAVING`은 집계 후 그룹 조건이다.", "설비별 측정 건수와 평균을 비교한다.",
     '''sql = con.execute("""
SELECT machine, COUNT(*) AS n, AVG(vibration) AS mean_vibration
FROM measurements
GROUP BY machine
HAVING COUNT(*) >= 2
ORDER BY machine
""").df()
pd_result = df.groupby("machine", as_index=False).agg(n=("vibration", "size"), mean_vibration=("vibration", "mean"))
print(sql, pd_result, sep="\\n")''',
     "- 행 조건은 `WHERE`, 그룹 통계 조건은 `HAVING`에 둔다. Pandas에서는 `groupby().agg()` 후 결과를 필터한다.\n- `COUNT(*)`는 전체 행 수, `COUNT(vibration)`은 비결측 건수다. `AVG`는 결측을 제외한다."),
    ("CASE WHEN과 Pandas 분류", "`CASE WHEN`은 SQL에서 조건에 따라 새 값을 만든다.", "위험 라벨을 SQL과 Pandas에서 만든다.",
     '''sql = con.execute("""
SELECT machine, cycle, vibration,
       CASE WHEN vibration >= 4 THEN 'danger'
            WHEN vibration >= 3 THEN 'watch'
            ELSE 'normal' END AS state
FROM measurements ORDER BY machine, cycle
""").df()
pd_result = df.assign(state=df["vibration"].map(lambda x: "danger" if x >= 4 else "watch" if x >= 3 else "normal"))
print(sql, pd_result, sep="\\n")''',
     "- 분류 규칙이 조회 결과의 일부면 SQL `CASE`가 자연스럽다. Python에서 규칙을 함수로 재사용할 때는 Pandas `map`·`np.select`를 쓴다.\n- 조건 순서가 중요하다. `>=3`을 먼저 쓰면 4 이상의 값도 `watch`가 된다."),
    ("JOIN과 키 검증", "조인은 공통 키로 두 표를 연결한다. 키 중복은 예상보다 많은 행을 만든다.", "설비 메타데이터를 붙이고 행 수를 확인한다.",
     '''master = pd.DataFrame({"machine": ["A", "B"], "line": ["L1", "L2"]})
con.register("master", master)
joined = con.execute("""
SELECT m.machine, m.cycle, m.vibration, s.line
FROM measurements AS m LEFT JOIN master AS s USING (machine)
ORDER BY m.machine, m.cycle
""").df()
print(joined)
assert len(joined) == len(df)
assert not master["machine"].duplicated().any()''',
     "- `LEFT JOIN`은 왼쪽 센서 행을 보존하고, `INNER JOIN`은 양쪽에 키가 있는 행만 남긴다.\n- Pandas `merge(..., how='left', validate='many_to_one')`는 관계를 명시적으로 검증할 때 편하다. SQL 결과도 조인 전후 행 수와 키 유일성을 확인한다."),
], "[`2. practice/08_DuckDB`](../2.%20practice/08_DuckDB)")


write("11_predictive_maintenance.ipynb", "11 · 설비 이상 탐지와 고장 예측",
      "원본 실습의 Z-score, Isolation Forest, 분류 모델, RUL 개념을 한 흐름으로 비교합니다. 이 노트북은 `scikit-learn`이 필요합니다. 예제는 계산 연습용이며 실제 설비의 안전 기준이 아닙니다.", [
    ("정상 기준과 Z-score", "정상 구간에서 평균·표준편차를 학습하고 이후 값과 비교한다.", "정상 기준을 고정해 새 측정값의 점수를 계산한다.",
     '''import numpy as np
import pandas as pd
normal = pd.Series([2.0, 2.1, 2.2, 2.3, 2.4])
future = pd.Series([2.3, 2.7, 3.5])
center, scale = normal.mean(), normal.std(ddof=0)
z = (future - center) / scale
print(center, scale, z.round(2))''',
     "- 정상 기간만 기준에 넣어야 미래 이상이 평균·표준편차를 왜곡하지 않는다.\n- Z-score는 단일 센서의 단순 기준에 좋다. 여러 센서가 함께 변하는 패턴은 다변량 모델을 고려한다. 기준값이 0이면 계산할 수 없다."),
    ("Isolation Forest", "Isolation Forest는 라벨 없이 다변량 관측에서 상대적으로 고립된 점을 찾는다.", "정상에 가까운 학습 표본으로 모델을 맞추고 새 값에 점수를 낸다.",
     '''from sklearn.ensemble import IsolationForest
train = pd.DataFrame({"rms": [2.0, 2.1, 2.2, 2.3, 2.4, 2.2, 2.1],
                      "temperature": [70, 71, 72, 73, 74, 71, 72]})
new = pd.DataFrame({"rms": [2.2, 5.0], "temperature": [72, 95]})
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(train)
print(model.predict(new))  # 1: 정상 측, -1: 이상 측
print(model.decision_function(new))''',
     "- `predict`는 간단한 라벨, `decision_function`은 상대적 점수다. 점수와 원본 센서값을 같이 봐야 해석 가능하다.\n- `contamination`은 예상 이상 비율과 연결되므로 경보량을 검증한다. 학습 데이터에 고장이 많이 섞이면 기준이 흐려진다."),
    ("분할과 정보 누출", "학습 데이터와 평가 데이터는 시간·설비 단위로 분리해야 실제 미래 예측에 가깝다.", "같은 설비의 미래 측정을 평가 집합으로 둔다.",
     '''sequence = pd.DataFrame({"cycle": range(1, 11), "sensor": [2.0, 2.1, 2.0, 2.2, 2.3, 2.5, 2.8, 3.0, 3.3, 3.7]})
train_part = sequence.loc[sequence["cycle"] <= 6]
test_part = sequence.loc[sequence["cycle"] > 6]
print(train_part["cycle"].tolist(), test_part["cycle"].tolist())''',
     "- 무작위 `train_test_split`은 독립된 행이라면 편하지만 같은 설비의 인접 시점이 양쪽에 섞이면 평가가 과하게 좋아질 수 있다.\n- 다른 설비로 일반화할 목표라면 설비 ID별 분리, 같은 설비의 미래를 예측할 목표라면 시간순 분리를 쓴다. 스케일러와 결측 대체도 학습 집합에서만 `fit`한다."),
    ("지도학습 분류", "고장 라벨이 있으면 `fit(X, y)`로 입력과 정답의 관계를 학습한다.", "작은 예제에서 확률과 분류 결과를 확인한다.",
     '''from sklearn.ensemble import RandomForestClassifier
X_train = pd.DataFrame({"rms": [1.8, 2.0, 2.1, 2.3, 3.8, 4.0, 4.2, 4.5],
                        "temperature": [68, 70, 72, 74, 85, 88, 90, 92]})
y_train = pd.Series([0, 0, 0, 0, 1, 1, 1, 1])
clf = RandomForestClassifier(n_estimators=50, random_state=42)
clf.fit(X_train, y_train)
X_new = pd.DataFrame({"rms": [2.2, 4.1], "temperature": [73, 89]})
print(clf.predict(X_new), clf.predict_proba(X_new))''',
     "- `predict`는 클래스, `predict_proba`는 클래스별 추정 확률이다. 경보 비용에 맞춰 확률 기준을 조정할 수 있다.\n- 지도학습은 신뢰할 만한 고장 라벨이 있을 때 유리하다. 라벨이 부족하면 이상 탐지나 규칙 기반 점검을 먼저 고려한다."),
    ("RUL과 평가", "RUL은 남은 유효 수명이다. 현재 cycle에서 실제 고장 cycle까지의 차이로 만들 수 있다.", "간단한 RUL 라벨과 혼동행렬을 확인한다.",
     '''from sklearn.metrics import confusion_matrix, classification_report
life = pd.DataFrame({"unit": [1, 1, 1, 2, 2], "cycle": [1, 2, 3, 1, 2]})
life["failure_cycle"] = life.groupby("unit")["cycle"].transform("max")
life["RUL"] = life["failure_cycle"] - life["cycle"]
print(life)
actual = [0, 0, 1, 1]
predicted = [0, 1, 1, 0]
print(confusion_matrix(actual, predicted))
print(classification_report(actual, predicted, zero_division=0))''',
     "- 실제 run-to-failure 데이터에서만 그룹 최대 cycle을 고장 시점으로 볼 수 있다. 중도 종료된 설비의 마지막 관측 시점은 고장 시점이 아니다.\n- 혼동행렬은 놓친 고장(FN)과 오경보(FP)를 분리한다. RUL 예측 자체는 회귀 문제이므로 MAE 같은 수명 오차도 평가한다."),
], "[`2. practice/06_Z-score`](../2.%20practice/06_Z-score), [`2. practice/07_domain_Predictive_Maintenance`](../2.%20practice/07_domain_Predictive_Maintenance)")
