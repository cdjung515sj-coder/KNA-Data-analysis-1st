# 01. 함수의 개념과 구조
# print 함수
print("안녕하세요")

first_name = "jinny"
middle_name = "su"
last_name = "jung"
print(first_name)
print(last_name)
print(first_name, middle_name, last_name)
print(f"{first_name}{last_name}")

# 위와 같이 똑같은 print를 호출에도
# 다양한 방법의 호출이 가능함
# 그 원리를 알기 위해 우리가 직접 함수를 만들 수 있어야 함

# 함수 이름만 보고 어떤 기능을하는지 유추하는 그런 이름을 짓는게 중요해요
# 함수 이름 지을때 가장 많이 고민하셈. 명사로 지어요

# 에러(Error)의 종류
# 1. 실행 중 오류 (Runtime Error) - 작동 중단됨
# 2. 논리적 오류 - 작동은 잘 되는데, 결과적으론 문제가 있어 고쳐야함
#   : 우리는 함수 이름에 걸맞는 동작만 잘 되도록 만들어야함
# 함수 이름에 걸맞는 동작을 하도록 이름 잘 지어봐~ 작명도 능력이야~ 한잔해~


# 간단한 인사메세지 보여주기 함수를 만들어보자!
# : 의 의미 - ":" 으로 끝나는 줄의 뜻은 " 이 다음 줄부터 들여쓴 내용은 한 묶음"
def say_hello():
    print("안녕하세요")  # 안나와


# 위에서 만든 함수는 이렇게 호출해야만 실행됩니다!
say_hello()  #  요로코롬 함수를 바로 넣어준다면? print를 쓰지 않아도 되죠?
print(say_hello())  # None으로 출력


my_number = 27


# 함수 안에서 벌어지는 일들을 만들어보자
def show_number():
    # print(f"함수 시작: {my_number}")
    # UnboundLocalError: cannot access local variable 'my_number' where it is not associated with a value
    my_number = 515
    print(f"함수 종료: {my_number}")


# 위 함수를 실행해보자
show_number()

# 여기서도 my_number 값을 정해보자
# 아랫줄의 my_number는 show_number함수 안의 my_number와 다른 존재
my_number = 27  # 위 515값과 다르다
show_number()

# 그래서 함수 안의 my_number 데이터가 영향을 끼치는 범위를 전문용어로 "스코프(scope)" 라고 부른다

# 함수는 호출되기 전에 정의() 만들어져야 된다.

# show_title() # NameError 발생
# 함수를 def로 만들기 전에 먼저 부르면 NameError가 발생합니다. 항상 def로 만든 뒤에 호출해야 합니다.


def show_title():
    print("함수 배우기")


show_title()


# 함수가 호출되면 그 안의 코드는 매번 새롭게 시작된다
def show_counter():
    # count = count + 1 # 기존 count라는 존재는 모른다고 error
    count = 0
    print(count)
    # 이 함수가 종료되면 count를 포함한 이 함수 안의 데이터는 모두 사라짐


show_counter()
show_counter()
show_counter()

# 각 함수의 이름은 이름에 걸맞는 역할만 해줘야 한다


def show_students():
    print("학생: 짱구")
    print("학생: 맹구")
    print("학생: 철수")
    print("학생: 유리")
    print("학생: 훈이")
    # print("선생님: 채성아") # 기능적으로 잘 돌아가나,
    # show_students()라는 이름을 보면 이 코드를 읽는 사람(또는 미래의 나)은 "아, 이 함수를 쓰면 학생 목록만 나오겠구나!" 하고 예상합니다.
    # 그런데 예상치 못하게 선생님 이름까지 함께 나오면, 함수가 자신의 이름과 다른 일(선생님 출력)까지 같이 하고 있는 셈이 됩니다.


def show_teacher():
    print("선생님: 채성아")


show_students()
show_teacher()
# 이렇게 두개로 나눠서 해주는게 좋아


# 이제 위에 코드 대신 아래처럼 한번에 출력해주는게 좋겠지?
def show_classroom():
    show_teacher
    show_students


show_classroom()

print("===================== 코드 중복과 함수화 ==========================")

# [상식] 사이드이팩트
#       : 특정 부분의 코드가 문제 없지만, 다른 부분과 예상치 못한 영향을 주고 받는다면?
# 그래서 한 코드에 하나씩 만들어서 파일을 새로 만드는 것이 좋음
# 파일 여러 개로 올리면 좋아

# 코드 중복과 함수화
print("압축기 A 온도 확인 중")
print("결과를 기록합니다")
print("펌프1 온도 확인 중")
print("결과를 기록합니다")

# 위와 같은 식의 코드를 여기저기 복-붙하면
# 언젠가 사람의 실수로 사고가 생길 수 있다.


# 실습 2번
def start_check():
    print("점검을 시작합니다")
    print("안전 정비를 확인하세요")
    print("기록을 준비하세요")


start_check()  # 압축기 A에 대한
start_check()  # 펌프 1에 대해 출력

print("----------------------------------")


# 함수의 호출 결과 예측하기
# 실습 3. 함수 실행 흐름 추적하기
def say_hi():
    print("안녕하세요")


say_hi()
say_hi()
# 두 번 호출해서 두번 나온다~

print("----------------------------------")

# 실습 4. 함수로 설비 점검 자동화하기
# 1. 구분선과 점검안내 2줄이 설비마다 반복 출력
# 2. 점검 안내 여러 줄을 출력하는 함수를 정의
# 3. 두 함수를 설비마다 순서대로 호출
# 4. 실행해 각 설비마다 같은 안내가 반복되는지 확인
# 예상 결과 : 구분선과 점검 안내 2 줄이 설비마다 반복


# 구분선 출력
def print_line():
    print("=" * 20)


def print_check():
    print("점검을 시작합니다")
    print("기록을 준비하세요")


# 장비 1에 대한 함수 호출
print_line()
print_check()

# 장비 2에 대한 함수 호출
print_line()
print_check()
