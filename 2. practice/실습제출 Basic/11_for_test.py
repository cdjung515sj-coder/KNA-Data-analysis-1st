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


print("\n=== 369 게임 출력 ===")
bounds = str(input("입력: "))
bounds_len = len(bounds)  # 몇자리수인지 확인하기 위함

l = []  # 빈 리스트
count_369 = 0
for num in range(1, int(bounds) + 1):

    str_num = str(num)
    len_num = len(str_num)

    for j in range(0, len(str_num)):
        if (  # 각 인덱스 자리수 3, 6, 9 포함 확인
            str_num[j] == "3" or str_num[j] == "6" or str_num[j] == "9"
        ):
            count_369 += 1

    if count_369 > 0:
        l.append("👏🏻" * count_369)
    else:
        l.append(num)

    count_369 = 0


print(f"369 결과: {l}")


# 안녕의 인덱스 출력
# 이를 위해서는 값을 비교하기 위해 모든 리스트의 값이 필요
# 그리고 그 값의 인덱스를 알아야 출력
list = ["안녕", "hi", "hi", "안녕", "hi", "안녕"]

# 리스트의 모든 요소에 접근을 해야하는 경우
# python이 반복문에서 이를 쉽게 할 수 있도록
# enumerate라는 내장 함수 제공
# enumerate은 리스트의 모든 요소를 앞에서부터 순서대로 하나씩 찝어가며 접근함
# 접근해서 각자의 인덱스와 그 값을 뽑아줌 ---> 그래서 돌려주는 값은 2개가 돼!
# 값을 두 개 받으니 우리도 변수를 2개 준비하면 각 변수에 값이 쏙쏙 드가겠죠?
# 돌려주는 순서는 << 인덱스, 값 >>
# 그렇기 때문에 우리는 enumerate를 사용할 떄
# for 뒤에 변수를 두 개 전달함.

for index, value in enumerate(list):
    print(f"for index, value in enumerate(list) : {value}")

list_len = int(len(list))
for i in range(len(list_len)):
    print(f"for i in range(len(list)) : {list[i]}")

# 위 두가지는 동일한 작동을 함