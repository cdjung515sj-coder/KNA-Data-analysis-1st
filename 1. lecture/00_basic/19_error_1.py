# 트레이스백으로 에러 읽기

# ValueError : 글자를 숫자로 변환 요구 - 당연히 실패
# [[ 실패사례 ]]
#  temp = int("스믈")       # IndentationError: unexpected indent
# print(temp)

# [[ 정상 ]]
temp = int("20")
print(temp)

# ===================
print("--=--" * 20)
# ZeroDivisionError : 숫자는 0으로 나뉠 수 없음
# result = 10 / 0           # ZeroDivisionError: division by zero
# print(result)

# 정상화
result = 10 / 3
print(result)


# ==================
# NameError : 그런 이름도 있었어요? 라는
# hello()                   # NameError: name 'hello' is not defined. Did you mean: 'help'?
# print(hello)

# 정상화
print("Hello")

# ==================
# ⭐⭐⭐ try-except 동작 코드 ⭐⭐⭐

try:
    temp = int("스물")
except:
    print("해봤는데 안됨 !")
    temp = 0  # ⭐⭐⭐ 문제가 있어도 앞으로 잘 진행되도록 대안/추가 처리 필요

print(temp)


# ====================

origin = input("온도 :")

print(f"입력한 온도는 {origin}")

temp = 0

try:
    temp = int(origin)
except:
    print(
        "숫자가 아니면 왜 저를 부르셨어요? '0'으로 생각할게요."
    )  # ValueError: invalid literal for int() with base 10: '헤헤ㅔ' 위에 temp 0을 해줘


next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")


# ========================

# 09_01 실습 2

origin = input("온도 :")

print(f"입력한 온도는 {origin}")

try:
    temp = int(origin)
except ValueError:
    # ValueError인 상황이었다면 여기로 예외처리
    print("숫자가 아니면 왜 저를 부르셨어요? '0'으로 생각할게요.")
    temp = 0
except TypeError:
    # TypeError인 상황이었다면 여기로 예외처리
    print("타입 문제는 전지구적 문제입니다.")

next_temp = temp + 10
print(f"현재 온도 + 10 : {next_temp}")
