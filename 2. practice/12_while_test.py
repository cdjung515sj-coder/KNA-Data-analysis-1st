# 실습 1. while로 목표값 도달까지 반복하기
goal = 7
user_input = int(input("1~10 사이의 정답을 입력해주세요 :"))

while user_input != goal:
    user_input = int(input("1~10 사이의 정답을 입력해주세요 :"))

print("정답~")


# 실습 up down 게임
# 1~50 중 하나의 숫자를 정답으로 저장
# 사용자의 입력값 기준으로 정답이 up인지 down인지 출력
# 정답이 나오면 " 정답입니다 " + " 게임 종료 "되었다고 출력

while True:
    count = int(input("1~50까지의 숫자를 입력해주세요 : "))
    # 1. 범위를 벗어난 경우 예외 처리
    if count < 1 or count > 50:
        print("1~50까지의 숫자를 입력해 주세요.")
    # 2. 정답을 맞힌 경우 (게임 종료)
    elif count == 33:
        print("정답입니다~")
        print("게임이 종료되었습니다.")
        break  # 반복문을 탈출하여 게임을 끝냅니다.
    # 3. 입력값이 33보다 작은 경우
    elif count < 33:
        print("Up")
    # 4. 입력값이 33보다 큰 경우
    else:
        print("Down")


# 실습 2. 플래그로 조건 만족 값 검색하기

found = False
n = int(input("횟수 : "))

for i in range(n):
    v = int(input("측정값 : "))
    if v > 80:
        found = True
        break
if found:
    print("found")
else:
    print("None")

# 실습 조건에 맞는 값만 출력하기
temps = [10, 20, 30, 40, 50, 60, 70]
for i in temps:
    if i >= 30:
        print(f"고온 : {i}")

# 두 조건을 모두 만족하는 값 고르기
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60]
for i in hours:
    if i >= 5 and i <= 10:
        print(i)

# 조건에 맞는 값만 골라 평균 구하기
temps = [1, 2, 3, 4, 5, 6, 7, 10, 20, 30, 40, 50, 60, 70, 80]
total = 0
count = 0

for i in temps:
    if i > 30:
        total += i
        count += 1
        print(f"count: {count}, temp = {total}")
print(f"고온 평균:{total/count}")
