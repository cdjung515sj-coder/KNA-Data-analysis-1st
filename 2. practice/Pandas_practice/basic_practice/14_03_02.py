# 실습 2. 강한 상관 쌍 찾기
import pandas as pd

# 목표
# 상관 행렬에서 절댓값이 큰 센서 쌍을 자동으로 추출
df_hydraulic_qc = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8")
df_hydraulic_qc.info()

# 단계
# · 여러 지표 열로 상관 행렬을 만들기
# "%2d"는 10진수(decimal)를 두자리로 만들어 포함시키라는 뜻
feat = ["지표%02d" % i for i in range(1, 11)]
print(feat)

# feat = [f'지표{i:02d}' for i in range(1, 11)]

# 상관계수 계산
cm = df_hydraulic_qc[feat].corr().round(3)
print(cm)


# · 이중 반복으로 대각선을 제외한 각 쌍의 상관계수 확인
# 위 cm 자료에서 0.4 이상의 상관관계가 크다 판단되는 경우를 뽑아오기
for i in range(len(cm.columns)):
    print(f"{i}번째 컬럼 이름 {cm.columns[i]}")  # 0번째 컬럼 이름 지표01

    # i + 1번부터 챙겨 비교해야, 대각선 중심의 반대편을 중복 비교하지 않게 할 수 있다
    for j in range(i + 1, len(cm.columns)):

        c = cm.iloc[i, j]

        # print(f"{i}번째 컬럼 {cm.columns[i]}과 비교할 {cm.columns[j]} : {c}")
        # 8번째 컬럼 지표09과 비교할 지표10 : -0.951

        # abs로 - 부호 없는 절대값 만들기
        if abs(c) > 0.4:
            print(
                f"{i}번째 컬럼 {cm.columns[i]}과 비교할 {cm.columns[j]} : {c} -> 강한 상관계수"
            )

        # 바로 출력하지 말고 별도의 배열을 만들어 해다 배열에 결과를 추가하고
        # 반복문이 끝나면 바깥에서 출력 처리 및 가장 큰 값도 찾고, 강한쌍이 몇개인지도 출력해보자

# · 절댓값이 기준 이상인 쌍만 모아 큰 순서로 정렬


# 예상 결과
# 절댓값 0.4 이상 쌍 3개 출력 (07-08 -0.969 최대)
