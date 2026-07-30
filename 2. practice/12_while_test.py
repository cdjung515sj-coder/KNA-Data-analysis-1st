# 실습 1. while로 목표값 도달까지 반복하기
goal = 7
user_input = int(input("1~10 사이의 정답을 입력해주세요 :"))

while user_input != goal:
    user_input = int(input("1~10 사이의 정답을 입력해주세요 :"))

print("정답~")
