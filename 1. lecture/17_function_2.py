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


