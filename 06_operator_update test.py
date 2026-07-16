print("====== 실습 1 : 사칙연산 계산기 ======")

a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a // b)
print(a**b)
print(a % b)


print("====== 실습 2 : 평균과 도형 계산======")

a, b, c = 10, 20, 30
print("평균 =", (a + b + c) / 3)
변 = 40
print("넓이 =", (변**2))
print("부피 =", a * b * c)


print("====== 실습 3 : 비교 연산 출력======")

print(15 == 15)  # True
print(
    "안녕" != "안녕하세요"
)  # True (= 앞에 !가 있어 부정 => 다르다가 맞기 때문에 True)
print(1 > 15)  # False
print(15 < 16)  # True
print(25 >= 10)  # True
print(25 <= 10)  # False (10은 25보다 작기 때문에 틀림. True 하려면 >=로 바꿔야함.)

print("====== 실습 4 : 정상범위, 다중센서 판정 ======")

temp = 85
온도_정상 = 60 <= temp and temp <= 90
press = 5
압력_정상 = 3 <= press and press <= 7

print(온도_정상)
print(압력_정상)
print(온도_정상 and 압력_정상)  # 온도, 압력 정상

stock = 100  # 재고 100 개
stock += 50  # 입고 50 개
print(stock)  # 150 개 입고 됨

print("====== 실습 5 : 복합 할당으로 재고 추적, 기초 ======")
stock -= 30  # 출고 30 개
print(stock)  # 현재 120 개
stock += 5  # 반품 5개
print(stock)  # 현재 125 개

T = 500  # 총 500 개
Df = 23  # 불량품 23 개
print((Df / T) * 100, "%")  # 불량률 4.6 %

print("====== 실습 6 : 설비 지표 계산, 실전 ======")
run_h = 21  # 가동시간 21시간
total_h = 24  # 전체 가동시간
print((run_h / total_h) * 100, "%")  # 가동률 87.5 %
복
print("====== 실습 7 : 시간 변환, 상자 포장, 도전 ======")
total_m = 500  # 총 가동 (분)
print(total_m // 60)  # 8 시간
print(total_m % 60)  # 20 분
print(total_m // 60, "시간", total_m % 60, "분")  # 8 시간 20 분
