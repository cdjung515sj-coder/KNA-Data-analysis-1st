# 실습 1. range로 숫자 흐름 출력하기
n = int(input("마지막 숫자 N :"))
print("=== 1 ~ N 까지 출력 ===")
for i in range(1, n + 1):
    print(i)
print("=== 0 ~ N 까지 짝수 출력 ===")
for i in range(0, n + 1, 2):
    print(i)
print("=== 0제외 ~ N 까지 짝수 출력 ===")
for i in range(2, n + 1, 2):
    print(i)
print("=== N ~ 1 까지 역순 출력 ===")
for i in range(n, 0, -1):
    print(i)

# 실습. 3의 배수 출력하기
# 사용자에게 범위를 입력받아 3의 배수 숫자인 경우 출력하기
# 예)
# 사용자 입력값 : 20
# 출력값: 3, 6, 9, 13, 16, 19
# for 문, if문, 나머지연산자
# i % 3 == 0
print(3 % 3)  # 0
print(4 % 3)  # 1
print(5 % 3)  # 2
print(6 % 3)  # 0

n = int(input("범위를 입력해 주세요 :"))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(f"입력한 1~{n}사이의 3의 배수 출력 : {i}")
    elif i % 5 == 0:
        print(f"입력한 1~{n}사이의 5의 배수 출력 : {i}")
        # 15와 같이 3의 배수이면서 5의 배수인 경우는 3의 배수라고만 출력

num = int(input("사용자 입력값 : "))

for i in range(1, num + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print(i)
