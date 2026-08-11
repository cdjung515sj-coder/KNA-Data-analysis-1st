# 실습 3. 구체적 예외로 입력 검증하기

origin = input("온도를 입력하세요: ")

try:
    temp = int(origin)

    result = 100 / temp
    print(f"100을 입력한 온도로 나눈 값: {result}")

except ValueError:
    print(
        "[오류] 숫자가 아닌 문자나 소수점은 입력할 수 없습니다. 기본값 0으로 진행합니다."
    )
    temp = 0

except ZeroDivisionError:
    print("[오류] 0으로는 숫자를 나눌 수 없습니다! 온도를 0으로 설정합니다.")
    temp = 0

# 에러가 발생해도 프로그램이 멈추지 않고 아래 코드가 정상 실행됨
next_temp = temp + 10
print(f"입력(또는 기본값) 처리된 온도: {temp}도")
print(f"10도만 더 높으면: {next_temp}도")
