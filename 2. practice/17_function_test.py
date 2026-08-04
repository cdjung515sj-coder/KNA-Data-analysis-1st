# 실습 1. 첫 함수 만들고 호출하기
def start_checking():
    print("점검을 시작합니다")


start_checking()
start_checking()

print("-----------")

# 실습 2. 다중 매개변수로 센서값 계산하기

def function_data(name,temp):
    print(f"{name} {temp}도")


report("모터", 78)
report("펌프", 92)

print("----------")
# 실습 3. 키워드 인자로 함수 호출하기
# ①매개변수 두 개를 가진 함수를 정의
# ②호출할 때 매개변수 이름을 지정해 값을 전달
# ③키워드로 전달하면 순서를 바꿔도 같은 결과인지 확인
# ④위치 인자와 키워드 인자를 섞을 때는 위치가 먼저임을 확인

def report(name, temp):
    print(f"{name}{temp}")

print(name = "모터", temp = 78)
print(name = "펌프", temp = 78)