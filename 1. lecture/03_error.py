# 오류가 발생하면 당황하지 않고 과정이라고 생각하기
# 종류, 위치 읽기
# 해당 줄 확인하고 짝,이름 점검
# 고치고 재확인하기

print("==========NameError  만들기===========")

# print(NameError 만들기)  # SyntacError 발생 (띄어쓰기가 있어서 변수 2개를 쉼표 없이 작성했다고 추정)
# print(NameError만들기)  # NameError 발생 (만들기라는 변수가 없다고 추정)

#  코드는 위에서 아래로 실행되기 떄문에 위에서 에러 발생하면 그 이후 코드는 실행되지 않음.
print("NameError")  # NameError => "" 에러 발생 x



print("==========SyntaxError 만들기===========")

# print("온도) # SyntaxError 발생 (따옴표가 닫히지 않아서 오류 발생)
# print("진동" # SyntaxError 발생 (괄호가 닫히지 않아서 오류 발생)
print("온도")
print("진동")

print("+++++++++실습. 디버깅+++++++++")
# 목표 : 여러 오류가 섞인 코드를 하나씩 고쳐서 정상적으로 실행되도록 만들기
# 오류를 고치는 과정을 디버깅이라고 함.

# print(온도, 75)  # ""없음
# print("진동", 2.3 # 괄호 없음
# print("압력": 4.0)  # "", : 없음


print("온도", 75)
print("진동", 2.3)
print("압력", ":", 4.0)

print("=====","1번","설비","점검","=====") # ,는 띄어쓰기
print("온도(℃ ):"+" 82")
print("온도"+" 상승량:",22-11) # + 이어쓰기, 계산


# if
# for
# def(함수)

# if_true
# temp
# ValueError

#=========================================================

# 파이썬의 Traceback은 특이하게 가장 아래쪽이 진짜 에러가 발생한 위치이다.
# 위에서 아래로 갈수록 시간 순서대로 실행된 것을 의미한다.

# print(온도)
# NameError: name '온도' is not defined


# SyntaxError: 문법 오류
# NameError: 정의되지 않은 이름을 호출했을 때

# ========================================================
# SyntaxError 예시
# print("Hello World" '(' was never closed
# print("진동) unterminated string literal (detected at line ~~)

# 오류 대처 4단계
# 당황하지 않기
# 오류 메시지 읽기
# 오류 메시지 이해하기
# 오류 메시지 검색하기

# ========================================================

# 실습 - 오류 하나씩 고치기

# print(온도, 75)
# print("진동", 2.3
# print("압력": 4.0)

print("온도", 75)  # 따옴표 추가
print("진동", 2.3)  # 괄호 닫기
print("압력", 4.0)  # 콜론을 쉼표로 변경

# ========================================================

# 실습 - 점검 리포트 안내
Temperature_1st = 82  # 정상 온도
Temperature_Anomaly = 95  # 이상 온도
Temperature_Change = abs(Temperature_1st - Temperature_Anomaly)  # 온도 상승량

print("=====", "1번", "설비", "점검", "=====")
print("온도(℃):" + str(Temperature_1st))
print("온도 상승량((❁´◡`❁)):" + str(Temperature_Change))

# Temperature_1st, Temperature_Change은 숫자형이므로,
# + 연산자를 사용하려면 따옴표를 붙이거나,
# str() 클래스 호출 후 형변환이 필요함.