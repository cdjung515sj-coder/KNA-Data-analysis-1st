# 인사말 출력 함수 간단 버전
def say_hello():
    print("안녕하세요")


say_hello()


# 인사말 출력 함수 친근 버전
# 뻘짓 코드를 보여주면 다음에 안하겠죠? 좋은 코드 도출까지 보여줄게! 뻘짓하지마1
def say_hello_ned():
    print("안녕하세요, Ned")


def say_hello_tuna():
    print("안녕하세요, Tuna")


say_hello_ned()
say_hello_tuna()

# 인사할 대상이 많아진다고 위 함수들을 더 만드는건 에바참치꽁치;;;;
# 해결책은 하나의 함수에서 저 다양성을 다 대응해주는 것
# 그것이 바로 함수의 매개변수 활용💡💡

# 그때그때 다른 점만 바꿔 출력하고 싶은거잖아


def say_hi(name):
    print(f"반갑습니다, {name}")


say_hi("Ned")
say_hi("jinny")
say_hi("Layla")
say_hi("Tuna")
# say_hi(input("이름을 입력해주세요 :"))
# 우왕 신기해

# 예제코드 : 특정 장비 이름을 알려주면 해당 장비의 체크를 시작 알림


def check(name):
    print(f"{name} 점검을 시작합니다")


check("압축기A")
check("펌프A")


# 매개변수가 2개 이상인 예제 -덧셈
def calc_sum(number_1, number_2):
    # number_1 = 1
    # number_2 = 2
    total = number_1 + number_2
    print(f"{number_1} + {number_2} = {total}")


calc_sum(1, 2)


# 매개변수가 2개 이상인 예제 - 장비 이름과 온도 정보 출력
def report(name, temp):
    # name = "압축기A"
    # temp = 75.3
    print(f"{name}의 온도는 {temp}도입니다.")


report("압축기A", 75.3)
report("펌프B", 85.2)

# 엉뚱하게 호출해봅시다
report(35.2, "보일러C")
# 첫번째 매개변수는 무조건 name이 되고,
# 두번째 매개변수는 무조건 temp가 되니까
# 원하지 않는 결과가 나올 수도 있다

# 매개변수가 부족하거나 더 있으면?
# report("압축기A", 75.3, "가동중")  # TypeError 발생 - 변수가 다르자나 !
# TypeError: report() takes 2 positional arguments but 3 were given
# report("펌프B")
# TypeError: report() missing 1 required positional argument: 'temp'

# 따라서 매개변수도 중요하고 순서도 중요해

# 기워드 인자 없이 호출
report("펌프B", 85.2)
report(85.2, "펌프B")  # 이 경우는 문제 발생

# 💡💡 키워드 인자 사용해 호출
#        : 순서 바꿔 호출해 생기는 문제 근본 차단
report(name="펌프A", temp=37.4)
report(temp=37.4, name="펌프A")

# ==============================================================
print(" ---------------- 반환값을 변수에 담기 ------------")


# 안좋은 코드 예시
def add():
    print("1 + 1 = 2")


add()


# ==
# 좋은 코드 예시
def add():
    print("1 + 1 = 2")
    return


add()


# --


def add():
    a = 1
    b = 2
    total = a + b
    return  # 이러면 사라짐


print("1 + 2 = 3")  # 이렇게 출력하고 싶음

result = add()
print(f"1 + 2 = {result}")  # 1 + 2 = None


# --


def add():
    a = 1
    b = 2
    total = a + b
    return total  # ---------------- 이렇게 쓴다면 ?!


result = add()
print(f"1 + 2 = {result}")  # 1 + 2 = 3


# --


def add(a, b):
    total = a + b
    return total


print(add(1, 2))
print(add(12, 25))
print(add(32, 25))
print(add(323, 225))

# 여러번 같은 결과 호출해야한다면
# 차라리 변수에 담아서 쓰세요
result = add(1, 2)
print(result + 1)
print(result + 2)
print(result + 3)


# ------------------------------------
print(" 평균 내는 함수 만들기========")


def calc_average():
    return 4.0


def calc_average(a, b):
    return (a + b) / 2


avg = calc_average(75.3, 88.0)
print(f"평균 온도: {avg}")


print("000")


# 여러 값을 한 번에 반환하기
# 다음의 함수는 배열을 받아서 그 안의 최소값과 최대값을 동시에 return 한다.
def calc_min_max(values):
    minimum = min(values)  # 배열 안의 최소값을 찾아 minimum에 담기
    maximum = max(values)  # 배열 안에 최대값을 찾아 maximum에 담기
    return minimum, maximum


target_list = [1, 2, 3, 4, 5, 6]
result = calc_min_max(target_list)
print(result)  # 튜플인 것들을 확인

# 반환값을 언패킹으로 받기
# 함수의 결과를 받는 순간에 결과 튜플의 내용을 풀어서 개별 변수에 담아 사용하기
result_min, result_max = calc_min_max(target_list)
print("최소값 : " + str(result_min))
print("최대값 : " + str(result_max))

# return 반환값이 없는 함수를 호출해놓고
# 결과를 어디에 담겠냐고 하면, 담기는 값은 None이라고


def say_greet():
    print("만나서 반값습니다")
    return


greet = say_greet
print(greet)  # None


# ----------------------------------------
# 지금까지 배우 내용을 활용해서
# 재미있는 함수 만들기 예제

import random

groups = ["에스파", "하트2하트", "리센느", "태연", "엔믹스"]

# 랜덤 뽑기!
my_group = random.choice(groups)
print(my_group)


def get_random_group():
    groups = [
        {"이름": "에스파", "리더": "카리나"},
        {"이름": "엔믹스", "리더": "해원"},
        {"이름": "리센느", "리더": "원희"},
    ]

    my_group = random.choice(groups)

    return my_group.get("이름"), my_group.get("리더")


group_name, group_leader = get_random_group()
print(f"{group_name}의 리더는 {group_leader}입니다")


# ----------------------------
# 3-4인과 함께 코드를 만드시오. 가봤거나, 가보고 싶은 여행지 정보를 모아보자 (최소 5개 이상)
# 함수를 호출하면 랜덤으로 해당 여행지의 국가이름과 수도
# "환영합니다! --- 나라의 수도 --- 입니다!" 출력


import random

travel_destinations = [
    {"국가": "대한민국", "수도": "서울"},
    {"국가": "일본", "수도": "도쿄"},
    {"국가": "러시아", "수도": "모스크바"},
    {"국가": "프랑스", "수도": "파리"},  # '유럽' 대신 프랑스로 설정
    {"국가": "미국", "수도": "워싱턴 D.C."},
]


def recommend_travel():
    selected_place = random.choice(travel_destinations)
    country = selected_place["국가"]
    capital = selected_place["수도"]
    print(f"환영합니다! {country} 나라의 수도 {capital} 입니다!")


recommend_travel()
recommend_travel()
recommend_travel()
recommend_travel()
recommend_travel()
recommend_travel()
recommend_travel()
