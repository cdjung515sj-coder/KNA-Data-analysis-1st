# 함수의 기본 예제
def say_hello():
    pass  # 아무일도 안하는 코드


def say_hi():
    print("안녕하세요")


# 함수는 선언된(def) 후에 호출왜야 한다
say_hi()


# 매개변수를 사용하면 더 다양한 일을 할 수 있습니다
def show_hello(name):
    # name = "sujin"
    print("안녕하세요", name)


# show_hello(name) # 이렇게 적는 경우가 많아 아닙니다
# show_hello() # name 이 없어서 안됨

# 그러나 밑의 경우라면?
name = "sujin"
show_hello(name)

# 이렇게 해야함
show_hello("Ned")
show_hello("sujin")


# 매개변수는 여러 값을 받을 수 있고
def show_hi(name):
    message = "안녕하세요"
    print(f"{message}, {name}")


show_hi("sujin", "안녕하세요")
show_hi("sujin", "반갑습니다")

# 매개변수에는 따로 안알려주면 기본값을 적용할 수도 있습니다.
def show_greeting(name, message="안녕하세요"):
    print(f"{message}, {name}")


show_greeting("sujin")
show_greeting("jack")
