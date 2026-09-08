# input - 사용자 입력

name = input("이름(실습 ver) : ")
print("안녕하세요", name + "님!")


print("======= 숫자 입력받아 계산하기 =======")
# 태어난 해 받아 나이 구하기

print("제가 당신의 나이를 맞춰볼게요 :)")
birth = int(input("몇 년도에 태어나셨나요? : "))
age = 2026 - birth
print("나이 : (만) ", age, "세")
print("나이 : ", age + 1, "세")

city = input("거주 국가를 입력해주세요 :")
name = input("거주 도시를 입력해주세요 :")
print(city + "의", name + "에서 거주하시는군요!")

a = int(input("첫 번째 숫자를 입력해주세요 :"))
b = int(input("두 번째 숫자를 입력해주세요 :"))
print("덧셈 결과 :", a + b)
print("뺄셈 결과 :", a - b)
print("곱셈 결과 :", a * b)
print("나눗셈 결과(소숫점 첫 째 자리까지) :", round(a / b, 2))
print("제곱 결과 :", a**b)


temp = int(input("온도 :"))
print("80 초과 되었나요?", 80 < temp)
print("0 ℃ 이상인가요?", 0 <= temp)

print("입력하신 점수 3개의 평균을 구하겠습니다.")
score1 = int(input("점수 1 :"))
score2 = int(input("점수 2 :"))
score3 = int(input("점수 3 :"))
avg = (score1 + score2 + score3) / 3
print("60점 이상인가요?", avg >= 60)
