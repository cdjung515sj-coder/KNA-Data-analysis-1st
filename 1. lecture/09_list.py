# list 는 python의 자료형 중 하나임
# 여러 개의 값을 [대괄호] 에 감싸서 순서대로 저장됨
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가짐

int_temps = [10, 20, 30, 40, 50, 60, 100] # int 리스트 ( 숫자 리스트 )
float_temps = [10.0, 20.2, 30.3, 40.4] # float 리스트
str_machines = ["펌프", "압축기", "모터"] # string 리스트

# 리스트는 자료형이 달라도 한 리스트에 담을 수 있음
mixed = ["펌프", 78, True]

# 리스트에 자동으로 순서 인덱스가 붙는다면?
print(int_temps[2]) # 30 출력 - 인덱스로 해당 순서에 위치한 요소 뽑아내기

# 리스트 안에 몇 개의 값이 담겼는지 모르지만 마지막 요소를 뽑고 싶다면?
print(int_temps[-1]) # 100 출력 - 가장 마지막 값의 요소 출력

# 빈 리스트
empty = []

# 리스트에 담긴 값의 갯수 세기
# len() 내장함수 사용
print(len(int_temps)) # 7 개
print(len(empty)) # 0 개

# 리스트의 담긴 값의 갯수 변수에 저장
int_temps_length = len(int_temps) # 변수에 7이라는 값이 할당
print(int_temps_length) # 7

