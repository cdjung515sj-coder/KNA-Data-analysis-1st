# 실습 4. 반환값으로 간단 계산기 만들기
# print가 아니라 return으로 결과를 돌려주고 변수에 담기
# ①값을 받아 계산하는 함수를 정의
# ②계산 결과를 print가 아니라 return으로 돌려주기
# ③호출 결과를 변수에 담기
# ④담은 값을 다음 계산·출력에 이어 쓰기


def add(a, b):
    return float(a + b)


result = add(10, 75)

print(result)

result - add(result, 5)
print(f"{result}(담은 값을 이어씀)")
