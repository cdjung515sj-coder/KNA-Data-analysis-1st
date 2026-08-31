# while 특정 조건(횟수 x)이 False 될 때 까지 반복해야 하는 경우 사용


# ⚠️ 무한루프 유의

# count = 1
# while count <=3:
#     print(count)
# while문은 조건이 거짓이 되는 플래그를 꼭 세워야 함.

# ⚠️ 위 코드는 무한 루프이므로 돌리면 멈취잇
# 🖱️무한루프 강제 종료 : ctrl + c

# while 문 사용 체크리스트
# 1. 반복 전 변수(시작값) 존재하는가?
# 2. 반복을 하다가 언젠가 False가 될 수 있는 종료 조건을 포함하는가?
# 3. 변수가 거짓 방향으로 값이 변경되는가?


# ♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️

# count = 1  # 1번

# while count <= 3:  # 2번
#     # count = 0  # 반복문 안에 count 변수를 계속 0으로 재할당해서 무한루프에 빠짐 ㅜㅜ
#     print(count)
#     count += 1

# count = 1  # 1번

# while count >= 1:  # 2번
#     # count = 0  # 반복문 안에 count 변수를 계속 0으로 재할당해서 무한루프에 빠짐 ㅜㅜ
#     print(count)
#     count += 1  # 3번
#     # 끝도 없이 True 방법이 없엉.. 무한 루프 ㅜㅜ

# ♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️♾️

for i in range(1, 7):
    if i % 2 == 0:
        continue  # 이번 회차 건너뜀
    print(i)

# break
# 반복을 그만 돌고 싶을 떄

# ex1) [1,1,3,3,2,1,1,1,]
# 위 리스트를 돌면서 10 이상이 되면 중단하고 싶을때

# ex2) 사용자 입력값을 누적하다가 누적값이 총 15를 넘으면
# 종료하고 싶을때
# break 사용 시 즉시 for 문을 나감

input_sum = 0

while True:  # 조건만 보면 무한반복하는 코드
    user_input = int(input("값을 입력하세요. 값의 누적이 15를 넘으면 종료합니다. :"))
    input_sum += user_input  # 누적값 업데이트

    if input_sum > 15:  # 종료 트리거
        print(f"누적 합계 : {input_sum} 입력을 종료합니다.")
        break  # 누적 합계가 15를 넘으면 반복 종료
print("break를 통해 while문을 나가면 이후 코드가 실행됨")

# 사용자 입력값을 확인만 하고 저장할 필요가 없는 경우
while True:
    # 변수 x는 반복을 돌 때마다 재할당되기 때문에 휘발되지만
    x = input("입력 (종료는 q를 입력하세요) :")
    # 현재 입력값이 뭔지는 확인할 수 있음
    if x == "q":
        break
    print(f"입력받을 값 : {x}")
print(f"입력을 종료합니다.")


n = int(input("횟수 : "))

for i in range(n):
    v = int(input("측정값 : "))
    if v > 80:
        print("이상 발생")
        print("가동 횟수 : ", n)
        break
    else:
        print("정상상태")

# =================================

# 최댓값 찾기
first = int(input("1번째 입력값 : "))

# 첫 번째 입력값은 자동으로 최댓값이 됨 (비교할 다른 값이 없기 때문)
max_value = first

# for 문을 사용해서 사용자 입력을 4번 받고
# 입력 받은 값 중에서 가장 큰 값을 출력

for i in range(4):
    v = int(input(f"{i + 1} 번째 입력: "))

    # max_value 에는 현 시점 최댓값이 들어있어
    # v에는 방금 사용자가 입력한 값이 들어있어
    # max_value와 v의 값을 비교해 더 큰 값을 max_value에 재할당
    if v > max_value:
        max_value = v
print(f"최댓값 : {max_value}")  # for 반복문 종료 후 최종 최댓값 출력


first = int(input("1번째 입력값 : "))
max_value = first
for i in range(4):
    v = int(input(f"{i + 2} 번째 입력: "))
    # 위에서 1번째 입력을 받고, i는 0 부터 시작하기 때문에 2를 더해서 출력

    # max_value 에는 현 시점 최댓값이 들어있어
    # v에는 방금 사용자가 입력한 값이 들어있어
    # max_value와 v의 값을 비교해 더 큰 값을 max_value에 재할당
    if v > max_value:
        max_value = v
print(f"최댓값 : {max_value}")  # for 반복문 종료 후 최종 최댓값 출력



#  흐름 표를 보고 코드 작성
total = 0

for i in range(3):
    v = int(input(f"{i+1} 회차 값 :"))
    if v > 5:
        total += v
        print("참")
    else:
        print("거짓")
print(f"합계 : {total}")


list = [4,7,6]

for i in range(len(list)):
    print(list[i])