# 실습 1. finally로 파일 안전하게 닫기

text = input("온도를 입력해주세요:")
temp = 0

try:
    temp = float(text)
    print(f"입력 온도: {temp} ℃, {(temp -32)*1.8:.2f} F")
except ValueError:
    print("ValueError")
except NameError:
    print("NameError")
finally:
    print(f"오류 발생 시 (-57.6 F) :{(temp -32)*1.8:.2f} F")
