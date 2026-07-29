# 반복문은 동일한 작업을 특정 횟수만큼 반복해야할 때
# 코드를 길게 쓰지 않고 반복시킬

### for 변수 in range(횟수):  ###
#   반복시킬 코드 (들여쓰기 한 칸 필수)
# 같은 코드를 복사 붙여넣기로 여러 번 작성하는 대신
# "N번 실행하라"는 의미

# i 를 가장 많이 씀 (index)

for i in range(3):
    print("안녕하제!")  # range에 전달한 인자 3만큼 3 번 반복
    # for문 안에서 i를 쓰지 않아도 됨. (단순 반복) -> 목적이 "3번 반복"일 때

# 0 부터 10까지 숫자 자체가 필요하거나 출력할 때
for i in range(11):
    print(i)
    # i는 증강값을 지정하지 않는 이상 반복할 때 마다
    # 자동으로 +1을 적용됨.

# 0 ~ 10까지 짝수만 필요할 떄
for i in range(0, 11, 2):  # range(시작, 끝, 증가값)
    print(i)  # 반복할 때 마다 i가 2씩 자동으로 증가

# 1 ~ 10까지 홀수만 출력
for i in range(1, 11, 2):  # range(시작, 끝, 증가값)
    print(i)

# 역순으로 출력
for i in range(10, 0, -1):
    print(i)

# 10부터 1까지 짝수만 역순으로 출력
for i in range(10, 0, -2):
    print(i)

for i in range(0, 10, -2):
    print(i)
    # 동작 안함. 시작값인 0에서 -2를 했을 때 끝 값이 포함되지 않아서 그대로 반복문 종료


# "끝" 값의 의미
for i in range(11):
    print(i)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10  => 총 11번 출력

for i in range(0, 11, 3):
    print(i)  # 0, 3 ,6, 9 => 총 4번
    # range 함수에 전달한 두 번째 인자인 끝 값 11은 반복 횟수가 아님
    # 반복을 수행할 범위


# 누적변수
total = 0

for i in range(1, 6):
    total += i  # 기존 값에 i를 더해 재할당
    # total = total + 1
print("합계:", total)  # 1 + 2 + 3 + 4 + 5 = 15

# for문 안에 누적변수 선언 시 total = 0
# 누적 변수 초기화 => 범위에서 계속 0으로 돌아가서 결국 마지막 번호 값이 출력됨.
for i in range(1, 6):
    total2 = 0  # 반복을 돌 때마다 새롭게 변수에 값이 0으로 할당이 됨
    print("total2 = 0 시 total2에 할당된 값 :", total2)
    print("현재 i의 값 :", i)
    total2 += i
    print("total2 += i 후의 total2에 할당된 값 :", i)
print("합계:", total2)  # 가장 마지막 i인 5가 출력이 되는 것 !!

# 번외
if 3 == 3:
    hi = "안녕"
print(hi)  # 안녕
# python에서는 if 문 안의 변수도 어디서든 호출 가능한 변수로 선언됨.

# 1~15 사이의 4의 배수만 누적
total3 = 0
for i in range(1, 16):
    print(f"i 범위 : {i}")
    if i % 4 == 0:
        print(f"범위 안의 4의 배수 값 : {i}")
        total3 += i
        print(f"total3 값 누적 : {total3}")
print(f"1~15 사이의 4의 배수만 누적 결과 : {total3}")  # 4 + 8 + 12 = 24

# 개수 세기 패턴
count = 0
for i in range(1, 11):  # 범위는 1~10
    if i > 5:  # 5보다 큰 i 값은? 6,7,8,9,10
        count += 1  # 만족시 증가됨
print(f"5보다 큰 숫자는 몇개? : {count}")


# # enumerate(): 낱낱이 세다라는 의미
# 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받았을 때, 인덱스와 값을 포함하여 리턴
# for문과 함께 자주 사용됨
# 인덱스와 값을 동시에 접근하면서 루프를 돌리고 싶을 때 사용
temps = [33, 23, 45, 32, 28]

for t in enumerate(temps):
    print(t)
    # (0, 33)
    # (1, 23)
    # (2, 45)
    # (3, 32)
    # (4, 28)
# 범위를 지정하지 않아도 enumerate()에 전달한 리스드의 모든 요소 순환
# 문제는 형식이 (인덱스, 해당 인덱스 요소 값)로 출력
# enumerate를 사용할 떄는 변수를 2개 전달


for idx, t in enumerate(temps):
    print(f"idx: {idx}, t: {t}")
    # idx: 0, t: 33
    # idx: 1, t: 23
    # idx: 2, t: 45
    # idx: 3, t: 32
    # idx: 4, t: 28


for a, b in enumerate(temps):
    print(f"a: {a}, b: {b}")
    # a: 0, b: 33 
    # a: 1, b: 23 
    # a: 2, b: 45 
    # a: 3, b: 32 
    # a: 4, b: 28

# for idx , t in enumerate(temps):
# 위와 같이 2개의 변수를 전달하면
# enumerate가 temps 리스트를 순회하면서
# 반환해준 (인덱스, 해당인덱스의 값)을 
# 각자 idx에 인덱스 값을 할당, t에 해당 인덱스의 값을 할당
# 두 개의 값을 바로 사용할 수 있게 해줌

for idx, t in enumerate(temps):
    print(f"현재 인덱스: {idx}")
    print(f"{idx}인덱스의 값: {t}")
    print(f"{idx+1}번째 반복 끝")

# i와 idx 차이는?
# i는 지금 내가 시작하는 위치를 알려주는 친구

for dan in range(2, 20): # 바깥: 2단부터 19단까지
    print(f"=== {dan}단 ===") # <--- 각 단이 시작하기 전에 단 제목 출력
    for su in range(1, 10): # 안쪽: 1부터 9까지 곱하기
        print(dan, "×", su, "=", dan * su)
    print("---") # 한 단 끝마다 구분선