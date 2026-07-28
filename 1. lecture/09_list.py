# list 는 python의 자료형 중 하나임
# 여러 개의 값을 [대괄호] 에 감싸서 순서대로 저장됨
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가짐

int_temps = [10, 20, 30, 40, 50, 60, 100]  # int 리스트 ( 숫자 리스트 )
float_temps = [10.0, 20.2, 30.3, 40.4]  # float 리스트
str_machines = ["펌프", "압축기", "모터"]  # string 리스트

# 리스트는 자료형이 달라도 한 리스트에 담을 수 있음
mixed = ["펌프", 78, True]

# 리스트에 자동으로 순서 인덱스가 붙는다면?
print(int_temps[2])  # 30 출력 - 인덱스로 해당 순서에 위치한 요소 뽑아내기

# 리스트 안에 몇 개의 값이 담겼는지 모르지만 마지막 요소를 뽑고 싶다면?
print(int_temps[-1])  # 100 출력 - 가장 마지막 값의 요소 출력

# 빈 리스트
empty = []

# 리스트에 담긴 값의 갯수 세기
# len() 내장함수 사용
print(len(int_temps))  # 7 개
print(len(empty))  # 0 개

# 리스트의 담긴 값의 갯수 변수에 저장
int_temps_length = len(int_temps)  # 변수에 7이라는 값이 할당
print(int_temps_length)  # 7

# 리스트의 인덱스
print(int_temps[0], int_temps[-1])  # 가장 첫 번째 요소, 가장 마지막 요소 값 출력
# -1을 사용하는 이유는 최신 값은 대체로 뒤에 추가가 됨
# 가장 최신 값은 결국 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이 -1 로 계산이 가능 하지만 이 작업은 번거로워 -1을 가장 많이 사용함

# 없는 인덱스 호출
# temps 리스트 길이는 7
# print(int_temps[10]) # IndexError: list index out of range
# 인덱스 범위를 벗어나지 않도록 유의

# 리스트의 자료형
print("========== 리스트의 자료형 ==========")

# temps 리스트 자체
print(f"temps : {int_temps}")  # temps : [10, 20, 30, 40, 50, 60, 100]
print(f"type(temps) : {type(int_temps)}")  # type(temps) : <class 'list'>

# temps 리스트 0번째 인덱스 요소
print(f"temps[0] : {int_temps[0]}")  # temps[0] : 10
print(f"type(temps[0]) : {type(int_temps[0])}")  # type(temps[0]) : <class 'int'>


# 다른 자료형의 값이 들어있는 리스트의 요소 타입
# float 값이 들어있는 float_temps 리스트의 0번쨰 요소
print(type(float_temps[0]))  # <class 'float'>
print(type(str_machines[0]))  #  <class 'str'>

# 퀴즈
# mixed = ["펌프", 78, True]
print(type(mixed[1]))  # <class 'int'>
print(type(mixed[-1]))  # <class 'bool'>
print(type(mixed))  # <class 'list'>

# 리스트 슬라이싱
# 리스트명 [시작:끝:간격]
# 시작, 끝, 간격 인덱스는 모두 생략 가능 (문자열과 동일)

# int_temps = [10, 20, 30, 40, 50, 60, 100]
print(int_temps[1:3])  # [20, 30]
print(int_temps[1:2])  # [20]
print(int_temps[:2])  # [10, 20]
print(int_temps[:2], int_temps[3:])  # [10, 20] [40, 50, 60, 100]
print(int_temps[::1])  # [10, 20, 30, 40, 50, 60, 100]
print(int_temps[::3])  # [10, 40, 100]
print(
    int_temps[100:999]
)  # [] - 빈리스트가 출력됨. 슬라이싱은 없는 인덱스를 넣으면 빈 값을 반환해줌.


# <<< 인덱싱 vs 슬라이싱 >>>

# 인덱싱 temps[0]은 값 하나 ( 10 )
# temps[999]와 같은 없는 인덱스를 사용 시 에러

# 슬라이싱 temps[0:2]은 리스트( [10,20] )
# 슬라이싱은 영역을 잘라내는 역할이기 떄문에 리스트를 반환하는 것
# temps[999] 에러가 발생하지 않음
# 슬라이싱은 '있는 만큼'만 잘라주기 때문에 에러가 발생하지 않음


# 인덱스로 특정 값 바꾸기 // 문자열과 다름
# int_temps = [10, 20, 30, 40, 50, 60, 100]

print("원본 :", int_temps)  # 원본 : [10, 20, 30, 40, 50, 60, 100]
int_temps[2] = 999
print(
    "2번 인덱스 값 변경 결과 :", int_temps
)  # 2번 인덱스 값 변경 결과 : [10, 20, 999, 40, 50, 60, 100]

# in (존재 확인)
# str_machines = ["펌프", "압축기", "모터"]
print("펌프" in str_machines)  # True
print("펌프" not in str_machines)  # False

print("프레스" in str_machines)  # False
print("프레스" not in str_machines)  # True

# 특정 값의 인덱스 찾기
# 리스트.index(찾고자하는 요소)
# str_machines = ["펌프", "압축기", "모터"]

i = str_machines.index("압축기")
print(i)  # 1 출력 => 1번 값에 압축기 있다 ~ 알려줌

# .index() 메서드는 리스트에서 가장 처음 등장하는 인덱스만 반환함
str_machines2 = ["펌프", "압축기", "모터", "압축기"]
i2 = str_machines2.index("압축기")
print(i2)  # 1, 3 인덱스 값이 모두 동일하지만, 1로 출력. 첫 번쨰로 찾은 값만 알려줌

# =======================================================================================================
print("========== 리스트 값 추가 ==========")
### .append(추가할 값)
# - 리스트의 가장 마지막에 값을 추가 해줌 ###
# 리스트 원본이 수정되기 때문에 (재할당 필요 X) ⭐⭐⭐⚠️

nums = [1, 2, 3, 4, 5]

nums.append(999)
print(nums)  # [1, 2, 3, 4, 5, 999]

# 만약 원본 리스트와 특정 값을 추가한 리스트 둘 다 필요하다면
# 원본 리스트를 복사해서 리스트 수정 진행
# nums = [1,2,3,4,5,999] > 기본 리스트는 원본으로 둚
new_nums = nums  # 스스로의 메모리를 할당받지 않고, 메모리 주소만 복사
print(new_nums)  # [1,2,3,4,5,999]

new_nums.append(111)
print("원본 nums 리스트 : ", nums)
# 기대 결과 : [1, 2, 3, 4, 5, 999]
# 실제 결과 :  [1, 2, 3, 4, 5, 999, 111]
# 복사한 메모리 주소에 append를 했기 때문에 원본까지 영향을 받음

# 이를 해결하기 위해 .copy()라는 메스드 사용
# new_nums2 는 새로운 메모리에 nums 배열을 새로 저장
new_nums2 = nums.copy()
new_nums2.append(222)  # nums 배열에 영향을 미치지 않고 사용
print(
    "원본 new_nums2 리스트 :", nums
)  # 원본 new_nums2 리스트 : [1, 2, 3, 4, 5, 999, 111
print(
    "원본 new_nums2 리스트 :", new_nums2
)  # 원본 new_nums2 리스트 : [1, 2, 3, 4, 5, 999, 111, 222]


# 얕은 복사? 깊은 복사? -> 어려워서 패스할게영
# print("복사본 new_nums에 111 append 결과 :", new_nums) #[1, 2, 3, 4, 5, 999, 111]


### .insert(위치, 값)
# - 리스트에서 원하는 위치에 값을 삽입함 ###
# 원본 배열에 바로 삽입 됨
# 기존 배열에서 삭제는 되지 않고, 해당하는 인덱스 값이 삽입됨 (뒤에 요소들은 인덱스 + 1)
nums.insert(3, 333)
print(nums)  # [1, 2, 3, 333, 4, 5, 999, 111]


### .extend()
# - 리스트 연결
# 다른 리스트의 값들을 "풀어서" 이어붙임
data = [1, 2, 3]
new_data = [7, 8, 9]
sum_data = data.extend(new_data)
print(sum_data)

# 함수의 반환 개념을 안 뒤에 확인할 내용 !⤵️
print(data.extend(new_data)) 
# 기대 결과 : [1, 2, 3, 7, 8, 9]
# 실제 결과 : None
# extend() 메서드는 data라는 리스트를 "수정" 이를 반환하지 않음
# 반환값이 없어서 print할 값이 없는 것
print(data) # [1, 2, 3, 7, 8, 9]

