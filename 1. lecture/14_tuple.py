# tuple - 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나눠서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 , 를 붙여야 python이 튜블로 인식을 함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형


sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = (
    "모터온도",
    78,
)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'int'>

sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = ()
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# ⭐⭐⭐<튜플인 경우>⭐⭐⭐
# [요소 갯수]
## 요소 0개 : () 빈 괄호
## 요소 1개 : 쉼표 여부
## 요소 2개 이상 : 쉼표가 있다면

# 헷갈리는 튜플
## (1) : int
## (1,): tuple

# (1,2,3,) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시
# (1,2,3) -> 튜플이 맞음


# 튜플의 인덱스
# print(sensor[0])  # 모터온도

# 튜플의 슬라이싱
s = (
    "a",
    "b",
    "c",
    "d",
    "e",
)

# 아 bcd만 출력하고 싶다 ;;

print(
    f"슬라이싱한 결과는 소괄호에 감싸져 있음 : {s[1:4]} 따라서, 튜플은 슬라이싱해도 튜플이다~."
)  # ('b', 'c', 'd')

print(f"type(s[1:4]) = {type(s[1:4]) }")

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언하기
a, b, c = "a", "b", "c"

unpacking = (
    1,  # 변수 one
    2,  # 변수 two
    3,  # 변수 three)
)

unpacking = one, two, three
# one,two,three 라는 알 수 없는 변수를
# unpacking 변수에 할당하겠다는 의미
# 동작하지 않음

one, two, three = unpacking
# unpacking이라는 변수에 담긴 튜플 내부의 값들을
# 할당 연산자 왼쪽 one, two, three 변수에 풀어서 담는다는 뜻 !
print(f"one : {one}")
print(f"two : {two}")
print(f"threee : {three}")


one, two, three = unpacking
print(f"one : {one}")
print(f"two : {two}")
print(f"threee : {three}")
# print(f"four : {four}")
# 튜플의 언패킹은 변수의 개수와 튜플에 담긴 값의 개수가 동일해야 함

# 리스트 언패킹이 가능할까?
one, two, three = [11, 22, 33]
print(f"one : {one}")
print(f"two : {two}")
print(f"threee : {three}")
# one : 11
# two : 22
# threee : 33


# =======================================

tup = ("normal", "normal", "worning", "normal", "worning")

# 튜플의 길이
print(len(tup))  # 5

# 특정 값의 갯수 세기
print(tup.count("warning"))  # 2
print(tup.count("warning"))  # 2

# 특정 값이 처음 나온 인덱스 찾기
print(tup.index("warning"))  # 2
# 찾고자 하는 값이 없으면 Error 발생
print(tup.index("warning"))  # ValueError: tuple.index(x): x not in tuple


