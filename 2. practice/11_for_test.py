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
