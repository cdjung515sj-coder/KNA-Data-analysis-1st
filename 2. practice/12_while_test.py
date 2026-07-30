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