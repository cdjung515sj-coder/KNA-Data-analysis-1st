# [환경 설정] 한글 폰트 설정 및 필수 라이브러리 로드
# macOS, Windows, Linux, Google Colab 환경에 맞춰 한글 깨짐 없이 동작하도록 자동 감지 설정합니다.

import platform
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np

try:
    import seaborn as sns
except ImportError:
    pass

# 운영체제(OS)별 한글 폰트 자동 설정
system_name = platform.system()
if system_name == "Darwin":  # macOS
    plt.rcParams["font.family"] = "AppleGothic"
    plt.rcParams["font.sans-serif"] = [
        "AppleGothic",
        "Apple SD Gothic Neo",
        "NanumGothic",
        "DejaVu Sans",
    ]
elif system_name == "Windows":  # Windows
    plt.rcParams["font.family"] = "Malgun Gothic"
    plt.rcParams["font.sans-serif"] = ["Malgun Gothic", "NanumGothic", "DejaVu Sans"]
else:  # Linux / Google Colab
    try:
        nanum_fonts = [f.name for f in fm.fontManager.ttflist if "Nanum" in f.name]
        if nanum_fonts:
            plt.rcParams["font.family"] = nanum_fonts[0]
        else:
            import subprocess

            subprocess.run(
                ["apt-get", "install", "-y", "fonts-nanum"],
                check=False,
                stdout=subprocess.DEVNULL,
            )
            fm.fontManager.addfont("/usr/share/fonts/truetype/nanum/NanumGothic.ttf")
            plt.rcParams["font.family"] = "NanumGothic"
    except Exception:
        pass
    plt.rcParams["font.sans-serif"] = ["NanumGothic", "DejaVu Sans"]

# 마이너스 기호 깨짐 방지 및 Seaborn 폰트 동기화
plt.rcParams["axes.unicode_minus"] = False
try:
    if "sns" in locals():
        sns.set_theme(style="whitegrid", font=plt.rcParams["font.family"])
except Exception:
    pass

print(f'✅ 환경 설정 완료! 현재 적용된 폰트: {plt.rcParams["font.family"]}')


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/04-03_이상의_정의_진동데이터_130_260903_Question_1.csv")

print(df.head())
print(df.info())
print(df.columns)

run_df = df[df["가동여부"] == 1].copy()


# [2] 그래프 1 — 시간에 따른 진동 변화

plt.figure(figsize=(12, 5))

plt.plot(run_df["일자"], run_df["진동RMS"])

# 고정 임계치
plt.axhline(y=4.5, linestyle="--", label="고정 임계치 4.5 mm/s")

plt.xlabel("일자")
plt.ylabel("진동RMS")
plt.title("시간에 따른 진동RMS 변화")
plt.legend()
plt.grid()

plt.show()

# [3] 그래프 2 — 부하율과 진동RMS의 관계
normal_df = df[(df["가동여부"] == 1) & (df["일자"] < 80)].copy()

plt.figure(figsize=(5, 5))

plt.scatter(normal_df["부하율"], normal_df["진동RMS"])

plt.xlabel("부하율")
plt.ylabel("진동RMS")
plt.title("부하율과 진동RMS 관계")
plt.grid()

plt.show()

# [4] 정상 기준 숫자로 확인하기 — Python 사용
count = len(normal_df)

mean = normal_df["진동RMS"].mean()
std = normal_df["진동RMS"].std()

stat_threshold = mean + 3 * std

print()
print("정상 후보 데이터 수:", count)
print("진동RMS 평균:", round(mean, 2))
print("진동RMS 표준편차:", round(std, 2))
print("통계 임계치:", round(stat_threshold, 2))


# 강사님 ver.

# - 가동여부가 1인 행만 사용
# - x축 : 일자
# - y축 : 진동RMS
# - 선 그래프
# - 4.5 mm/s 위치에 수평 임계선 추가

op_status = df[df["가동여부"] == 1]

# 선그래프
plt.plot(op_status["일자"], op_status["진동RMS"])
plt.axhline(y=4.5, linestyle="--", color="red")