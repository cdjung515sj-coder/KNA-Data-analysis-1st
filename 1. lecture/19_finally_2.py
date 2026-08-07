# except들의 연속과  finally 사용

text = "24.5"  # 정상

print(text * 2)  # 24.524.5 >>??? 반드시 형변환을 해줘야함

#

text = "24.5"

temp = float(text)
print(temp * 2)  # 24.524.5 >>??? 반드시 형변환을 해줘야함


# text = "24.5" # 정상
text = "영크크"  # 비정상

temp = 0

try:
    temp = float(text)
    print(text * 2)
except ValueError:
    print("ValueError 문제 발생!!")
except NameError:
    print("NameError 문제 발생 !!")   
finally:
    # 오류가 있건 없건 finally 코드를 실행하여 마무리함
    print(temp * 2)
