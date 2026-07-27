line = "=" * 20  # 구분 쉽게하려공 ㅎㅎ


print(line, '""" 삼중 따옴표 / Tab """', line)
# """ """ (삼중 따옴표) - 여러 줄 문자열 구현. 공지사항이나 줄바꿈 할 때 유용함.

# 작성하는 개발자가 보기 편한 방식으로 출력했을 떄 문제
notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검
"""

print(notice)
#
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
# 위와 같이 직접 작성한 줄 바꿈이 반영되어 여러 줄로 출력됨.
#

# 개발자가 보기 편한 방식으로 작성하면 생각과 다른 결과물이 나옴
# """ """ (삼중 따옴표를 사용할 시 그 내부의 모든 줄 바꿈이 다 반영되어 출력)

# 탭 """    """ Tab 사용은 그대로 적용되어 보임
notice = """설비 점검 안내
    1. 전원 확인
2. 센서 점검"""

print(notice)
# 삼중 따옴표는 탭도 그대로 유지됨.
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검


# ===============================================================
print(
    "========== 이스케이프 문자, 줄바꿈(\,n) , Tab(\,t), 역슬래시(하나/둘 역할 다름),   ============"
)

# notice 이스케이프 사용해서 개선
# 1.\n - 줄바꿈
notice = "설비 점검 안내\n1. 전원 확인\n2. 센서 점검"
print("줄 바꿈 : \n 사용", notice)

# 2. \t - 탭
tap = "이름\t상태"
print("이름 상태")  # 위와 비교하기 위해 생성
print("탭 사용 \ t :", tap)

# 3. \\
backslash = "이름\\상태"
print("역슬래시 사용 \ \ ", backslash)
# 이름\상태 -> 쳣 번째\는 이스케이프 문자라는 것을 알리는 용도

quotes = "It's me"
# 감싸는 따옴표와 str 내부 따옴표의 종류가 같을 때는 \를 사용하면 됨.
print("'를 구분하기 위해 \ 사용 :", quotes)

# 빈 문자열과 공백 문자열의 차이
# "" 따옴표로 감싸졌지만 아무것도 작성되지 않았다면 "민 문자열"
# 빈 문자열은 글자 수 0, 길이 0
# "  " 따옴표 안에 공백(스페이스바)가 있는 경우는 "공백 문자열"
# 공백(스페이스바)의 수 만큼 글자가 있고, 길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨.
print("" == "   ")  # False 출력

# 설비 : PUMP_A
# 상태 : 정상
# 가동 : 1200  -> int로 저장되야함
# 점검 : 2026-07-16

code = "PUMP_A"
state = "정상"
run = 1200
date = "2026-07-16"
card = "설비:" + code + "\n상태:" + state + "\n가동:" + str(run) + "\n점검:" + date
# 위에서는 ,를 쓰면 다른 값으로 인식하기 때문에 위에서는 +를 사용하고
# ,를 사용하고 싶으면 밑에 print에서만!
print(card)


# ==================================================
# 인덱싱 - 위치 번호로 글자를 하나 꺼내는 것
# 문자열[인덱스번호]
# 단, 문자열의 첫 글자 인덱스는 💡0
print("=== 인덱싱 ===")

word = "PYTHON"
print(word[0], word[3], word[5])  # P H N
# print(word[100]) # IndexError: string index out of range
# => 변수에 저장된 문자열의 길이보다 큰 인덱스를 호출했기 때문

abc = "abcdefghijklmnopqrstuvwxyz"
# 자기 이름 출력하기 jinny
print(abc[9], abc[8], abc[13], abc[13], abc[-2])

# 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙음
# 주의사항은, 음수 인덱스는 가장 마지막 글자가 💡-1부터 시작함.


#=============================================================
# ⚠️⚠️ 슬라이싱 뇌 저~릿~ 주의 ⚠️⚠️
print("==== 슬라이싱 ====")
# 슬라이싱 - 구간으로 잘라내기 동작을 함.
# 문자열[시작:끝] 인덱스를 넣어주면 됨.
# 단, 시작⭕ 인덱스 글자는 포함 // 끝❌ 인덱스 글자는 제외하고 출력됨.

# HON 출력하고 싶엉  word = "PYTHON"
print("word[3:5] 결과 :", word[3:5])  # HO
print("word[3:6] 결과 :", word[3:6])  # HON
# 슬라이싱은 end가 포함되지 않고 출력하기 때문에 없는 인덱스인 6도 사용할 수 있는거 ! 헷갈리지 마~🤔

# print(word[6]) # 인덱싱은 정확하게 마지막 인덱스까지만 쓸 수 있고, 넘치면 Error 발생 !

# 슬라이싱 - start 생략
# 처음부터 특정 인덱스까지 구간을 뽑아내고 싶을 때 사용함.
print(word[:4])  # PYTH 출력.
print(word[0:4])  # 동일한 동작

# 슬라이싱 - end 생략
# 특정 인덱스부터 끝까지 구간을 뽑아내고 싶을 때 사용
print(word[2:])  # 2번 인덱스부터 끝까지 출력
print(word[2:6])  # 동일한 동작

# 슬라이싱- 전체 생략
print(word[:])  # print(word[0:6]) 와 동일한 동작
# : 을 사용하고 start와 end를 모두 생략하면 모든 인덱스의 구간을 뽑아냄

# 슬라이싱 - 음수 인덱스 사용 가능!
print(word[-3:])  # HON
# 음수 인덱스 작성 시 그 인덱스부터 정방향으로 출력함. (⚠️역순으로 출력하지 않음!)

print(word[:-1])  # PYTHO
# 처음부터 -1(5번 인덱스 N)을 제외한 구간을 뽑아냄 (⚠️⚠️ 역순 아님.)
# 음수 인덱스 사용 시 컴퓨터가 알아서 정수 인덱스 찾아 치환해서 동작함.

# step으로 건너뛰기
# a문자열[시작:끝:간격(step)]
print(word[0:6:2])  # 전체 글자인 경우 = print(word[0::2]) = print(word[::2]) # P T O
# PYTHON에서 첫 번째 글자는 명시했으니 거기서부터 출력.
# step이 2이기 때문에,
# Y 뛰고, T ( 두 번째 점프 ) => # H 뛰고, O ( 두 번째 점프 ) => # N 뛰고 끝.
# ⭐⭐⭐두 글자를 뛰는게 아니라 두 "번" 뛰는 것 ( 뛴 그 자리 글자를 출력한다.)⭐⭐⭐
print(word[::1])  # PYTHON

# start와 end를 생략하고
print(word[0::2])  # P T O
# word 변수의 모든 글자를 두 칸씩 뛰면서 출력

# 순서 뒤집기
print(word[::-1])  # NOHTYP
# step 은 인덱스가 아니기 때문에, 음수 입력시 문자열의 순서를 뒤집음.

# 슬라이싱은 범위를 벗어나도 오류가 발생하지 않음
print("범위를 벗어난 슬라이싱 :", word[0:999])  # PYTHON 정상 출력


print(line, "len() 활용", line)
# ===================================================================================
# len() - 문자열의 길이 반환
# len(문자열입력)

print(len("Hello World!"))  # 12 출력 : 글자수(공백 포함)
print(len(""))  # 0 출력 : 빈 문자열은 0 출력

var = "1 시간만 더 하면 끝이다 ㅜㅜㅜㅜㅜㅜ 언제 끝나 원영적 사고는 뭐임 한 시간 밖에 안남았자나~ 완전 럭키 비키니시티 스폰지밥이 와서 백덤블링해브러~"
print(len(var))
print(len("이렇게") + len("숫자계산") - len("가능함?"))
# 🤔 len() 은 int를 반환하기 때문에 연산이 가능하다 !

print("abc 변수의 길이: ", len(abc), " / 마지막 인덱스 번호 :", len(abc) - 1)

# 음수 인덱스를 사용하지 않아도 마지막 인덱스 문자를 뽑고 싶을 때
print(abc[len(abc) - 1])


# ============================================
print(line, "in 활용", line)

# in - 특정 문자가 문자열에 포함되었는지 여부 확인
# "여부"를 확인하기 때문에 True 또는 False (bool형)으로 결과를 반환함

# "찾을 문자열" in "문자열"
print("고장" in "설비 고장 발생")  # True ( 글자 있음 )
print("정상" in "설비 고장 발생")  # False
print("설비에서 고장" in "설비 고장 발생")  # False
print("설비에서 고장" in "설비에서 고장이 났습니다.")  # True

# not in - in의 정반대 동작
print("고장" not in "설비 고장 발생")  # False ( 고장이 있으니 반대 !)
print("정상" not in "설비 고장 발생")  # True
print("설비에서 고장" not in "설비 고장 발생")  # True
print("설비에서 고장" not in "설비에서 고장이 났습니다.")  # False

print(" " in "설비 고장 발생")  # 공백 문자열이 있으니 True  출력
# 따옴표로 감싼 공백(스페이스바)는 "한 글자"로 취급되기 때문에 !!

# ============================================
print(line, "count()", line)

# .count() - 문자열에 특정 글자의 수를 int 로 반환
# "문자열".count("찾을 글자")

print("banana".count("a"))  # 3
print("010-1234-1234".count("-"))  # 2
print("layla@spreatics.com(강사님 찐 메일)".count("@"))  # 1
# @를 기준으로 이메일인지 아닌지 알 수 있옹

# =================================
print(line, "find()", line)

# find() - 전달받은 글자가 "첫 번째"로 나오는 위치 인덱스 반환
# 찾는 글자가 없다면 -1 을 반환

email = "hong@company.com"
at = email.find("@")  # 4
print(at)  # 4
# email 내에서 "@" 문자를 찾고 싶어. => @ 위치의 인덱스인 4가 할당됨.
user_id = email[:at]  # hong 이라는 사용자 아이디만 추출 가능하다.
print(user_id)

# SQE-00Q8이라는 설비의 SQE만 뽑아내기 (find와 슬라이싱 사용)
sqe ="SQE-000Q9"

sqe_index = sqe.find("SQE")
print(sqe_index) # 0

sqe_index = sqe.find("-")
print(sqe_index) # 3
sqe_fin = sqe[:sqe_index]  # sqe[0:3] ==> SQE
print(sqe_fin) # SQE



email = 'hong@company.com'
at = email.find('@')
print(at) # 4
print(email[:at]) # hong
print('정상'.find('고장')) # -1

email[0:email.find("@")]
# 1. at 변수 사용 안함. 바로 슬라이싱에 삽입
# 2. 0을 썼다. (start 명시, 하지만 생략 가능)
# at 사용 안하고 상황에 따라 넣고 안넣고 해야해. 변수에 담아줘야해. 여러번 쓸 때 마다 연산하면 비효율적이니 재활용되는 함수는 변수로 할당하는게 좋음.

# ------------------------------------
print("====== index() =======")

# 특정 문자열의 위치(인덱스 번호)를 반환
# 앞에서부터 가장 처음 나오는 인덱스 번호만 반환 ⭐⭐⭐
# 찾는 문자열이 없으면 Error 발생.

email = "layla@spreatics.com"
at = email.index("@") # 5 출력
print(email[0:at]) # layla
print(email[:at]) # 시작 번호가 0이라면 start 생략 가능
print(email[at:]) # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략한 도메인
# 위처럼 시작하면 5번 인덱스부터 출력하기 때문에 @을 포함
print(email[at+1:])  # at + 1을 하면 @ 을 포함하지 않고 출력 



# find 에서 했던 SQE 뽑아내기 실습 index 사용으로 바꾸기

sqe ="SQE-000Q9"

sqe_index = sqe.index("-") # - 있으니 정상 동작
print(sqe_index) # 3
sqe_fin = sqe[:sqe_index]
print(sqe_fin) # SQE

# sqe_index = sqe.index("/") # / 없으니 ERROR 나고 중단됨
# print(sqe_index) # 3
# sqe_fin = sqe[:sqe_index]
# print(sqe_fin) # SQE

# ------------------------------------
print("====== count() =======")

# 문자열에서 특정 문자열의 갯수 세기

str = "a, b, c, d, e,a, a"

#  a 의 갯수 세기
print(str.count("a")) # 3

#  , 의 갯수 세기
print(str.count(",")) # 6

#  , 의 갯수 세기
print(str.count(", ")) # 5  # count 로 찾는 문자열과 완전히 동일해야 갯수를 셈


# ------------------------------------
print("====== startswith() =======")

# 특정 문자열로 시작하는지 검사
# True/False (불리언)

# EQP로 시작하는지 검사하기
print("EQP-001".startswith("EQP"))

# 변수 활용
eqp = "EQP"
print("EQP-001".startswith(eqp))
# ⚠️ 주의사항) 변수명은 절대 따옴표 감싸기 금지 

