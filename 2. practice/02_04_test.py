# print("실습 - 이름 입력받아 인사 출력")

# name = input("이름을 입력하세요: ")
# print(f"안녕하세요 {name}님!")
# print("안녕하세요 " + name + "님!")


# print("실습 - 숫자 입력받아 계산하기")
# year = input("태어난 해를 입력하세요: ")
# age = 2026 - int(year)
# print(f"니 나이는 한국 기준으로 {age + 1}살이야.")

# print("=== 실습 - 여러 개의 값 입력 받기 ===")
# country = input("나라 입력: ")
# city = input("도시 입력: ")
# age = int(input("나이 입력: "))
# print(country + "의" + "city에 사는", age, "살 이구나.")


# print("=== 실습 - 두 수 입력받아 사칙연산 ===")


# def calculator(a, b):
#     print(f"덧셈: {a + b}")
#     print(f"뺄셈: {a - b}")
#     print(f"곱셈: {a * b}")
#     print(f"나눗셈: {a / b}")
#     print(f"몫: {a // b}")
#     print(f"나머지: {a % b}")


# x, y = map(int, input("두 수 입력: ").split())
# print("\n산술 연산:")
# calculator(x, y)


print("\n=== 실습 - 입력값 비교해 출력하기 ===")
temper = int(input("온도 입력: "))
print("80 초과?", temper > 80)
print("0도 이상?", temper > 0)


print("\n=== 실습 - 입력/변환/계산/비교/출력(종합) ===")
s1, s2, s3 = map(int, input("세 점수 입력: ").split())
avg = (s1 + s2 + s3) / 3
print(avg)
print("60 이상?", avg >= 60)