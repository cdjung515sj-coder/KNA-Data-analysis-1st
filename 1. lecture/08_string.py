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


# =============================================================
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
sqe = "SQE-000Q9"

sqe_index = sqe.find("SQE")
print(sqe_index)  # 0

sqe_index = sqe.find("-")
print(sqe_index)  # 3
sqe_fin = sqe[:sqe_index]  # sqe[0:3] ==> SQE
print(sqe_fin)  # SQE


email = "hong@company.com"
at = email.find("@")
print(at)  # 4
print(email[:at])  # hong
print("정상".find("고장"))  # -1

email[0 : email.find("@")]
# 1. at 변수 사용 안함. 바로 슬라이싱에 삽입
# 2. 0을 썼다. (start 명시, 하지만 생략 가능)
# at 사용 안하고 상황에 따라 넣고 안넣고 해야해. 변수에 담아줘야해. 여러번 쓸 때 마다 연산하면 비효율적이니 재활용되는 함수는 변수로 할당하는게 좋음.

# ------------------------------------
print("====== index() =======")

# 특정 문자열의 위치(인덱스 번호)를 반환
# 앞에서부터 가장 처음 나오는 인덱스 번호만 반환 ⭐⭐⭐
# 찾는 문자열이 없으면 Error 발생.

email = "layla@spreatics.com"
at = email.index("@")  # 5 출력
print(email[0:at])  # layla
print(email[:at])  # 시작 번호가 0이라면 start 생략 가능
print(email[at:])  # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략한 도메인
# 위처럼 시작하면 5번 인덱스부터 출력하기 때문에 @을 포함
print(email[at + 1 :])  # at + 1을 하면 @ 을 포함하지 않고 출력


# find 에서 했던 SQE 뽑아내기 실습 index 사용으로 바꾸기

sqe = "SQE-000Q9"

sqe_index = sqe.index("-")  # - 있으니 정상 동작
print(sqe_index)  # 3
sqe_fin = sqe[:sqe_index]
print(sqe_fin)  # SQE

# sqe_index = sqe.index("/") # / 없으니 ERROR 나고 중단됨
# print(sqe_index) # 3
# sqe_fin = sqe[:sqe_index]
# print(sqe_fin) # SQE

# ------------------------------------
print("====== count() =======")

# 문자열에서 특정 문자열의 갯수 세기

str = "a, b, c, d, e,a, a"

#  a 의 갯수 세기
print(str.count("a"))  # 3

#  , 의 갯수 세기
print(str.count(","))  # 6

#  , 의 갯수 세기
print(str.count(", "))  # 5  # count 로 찾는 문자열과 완전히 동일해야 갯수를 셈


# ------------------------------------
print("====== startswith() =======")

# 특정 문자열로 시작하는지 검사
# True/False (불리언)

# EQP로 시작하는지 검사하기
print("EQP-001".startswith("EQP"))

# 변수 활용
eqp = "EQP"
print("EQP-001".startswith(eqp))
# ⚠️ 주의사항) 변수명은 절대 따옴표 감싸기 금지 !!!! ⭐⭐⭐⭐⭐⭐⭐


# ------------------------------------
print("====== endswith() =======")

# 특정 문자열로 끝나는지 확인
# True / False로 반환

str2 = "월요일입니다! 여러분은 할 수 있어요!"

print(str2.endswith("!"))  # True
print(str2.endswith("요!"))  # True
print(str2.endswith("음!"))  # False
print(str2.endswith("월요일입니다! 여러분은 할 수 있어요!"))  # True
# 완전히 똑같아야 True. 공백 있으면 거짓이죵
print(
    str2.endswith("월요일입니다!                     여러분은 할 수 있어요!")
)  # False
print(str2.endswith("월요일입니다! 여러분은 할 수 있어요! "))  # False
print(str2.endswith(" 월요일입니다! 여러분은 할 수 있어요!"))  # False

print(str2)  # 원래 할당된 문자

# 실습 startswith / endswith
csv_file = "sensor_log.csv"
print(csv_file.startswith("sensor"))
print(csv_file.endswith(".csv"))


# ------------------------------------
print("====== 값은 객체다 class =======")

print(type("잊어먹으면 안돼!!!"))  # <class 'str'>
print(len("이렇게 썼죠??"))
# endswith 와 len의 차이는?
# endswith 는 .으로 연결
# . 으로 연결하는 이런 도구들은 "매서드"
# 문자열이나 int, float 처럼 특정 자료형(객체) 내부에 포함된 기능을 의미함.
# len은 . 을 사용 안함
# () -> 함수 로, len과 같이 같이 개발자가 직접 선언하지 않은 기본 제공함수는 "내장함수" 라고 함

"str".startswith("s")
# 🚨 123.startswith(1) 쓸 수 없어요. 정의되지 않았기 때문. 왜? int 자료형엔 메서드가 저장되어 있지 않은거에요.
# . 으로 사용하는 메서드들은 특정 자료형(객체 타입)마다 다름
# int 자료형의 객체에는 startswith라는 메서드가 없음

# 🚨 print(len(123)) # TypeError: object of type 'int' has no len()
# len 내장함수는 길이를 반환하기 때문에 int 자료형 사용 불가 !


# ------------------------------------
print("====== 재할당 복습 =======")

num = 1
num = num + 1  # 2
num += 1  # 3
# += 은 복합할당연산자로 원래 내 자신의 값에 다음 오는 연산자와 값을 적용해서 재할당

# ------------------------------------
print("====== .upper() / .lower =======")

# 대소문자 통일이 필요한 이유는 한 파일에 섞여 같은 상태가 따로 집계되는 문제가 발생함
# 보통 소문자로 맞춤

str3 = "abcdefg"
print(str3)  # abcdefg

str3.upper  # ABCDEFG -> 반환은 대문자이나, 값에 재할당은 되지 않음
print(str3)  # abcdefg -> 기존 str3인 값인 소문자를 그대로 출력

# 앞으로 계속 대문자로 변환한 값을 사용하고 싶ㄷ면
# 변수에 재할당 필요
# 변수 재할당에서 변수 스스로를 부르는 것이 가능
# 재할당에서 변수 스스로 값을 부르려면 무조건 "재할당" 이어야 함.


str3 = str3.upper()

# 최초 변수 할당 시에는 저장된 값이 없어서, 변수 스스로 값을 불러와 할당? 불가능
# str4 = str4.upper() # => 그래서 오류

r = "ready"
rUP = r.upper()
print(rUP)

W = "WARNING"
w = W.lower()
print(w)

# lower
a = "Fault"
b = "FAULT"
print(a == b)  # False (대소문자 달라 다른 값)
print(a.lower() == b.lower())  # True (소문자로 통일 후 비교)

# ------------------------------------
print("====== capitalize() / title() =======")

user_name = "jeong su jin"

# capitalize는 문자열의 첫 글자만 대문자로 변환
print(user_name.capitalize())  # Jeong su jin

# title은 띄어쓰기 기준으로 각 단어의 첫글자들을 모두 대문자로 변환
print(user_name.title())  # Jeong Su Jin

# '를 사용한 경우, 다른 단어로 인식
print("i'm full".title())  # I'M Full
print("i'm full".title())  # I'M Full


# ------------------------------------
print("====== isupper() / islower() =======")

# 모두 대문자/소문자인지 참/거짓으로 확인
# 메서드임

a = "ABC"
b = "abc"
c = "Abc"
print(a.isupper())  # True
print(b.islower())  # True
print(c.isupper())  # False
print(c.islower())  # False

Sfile = "Sensor_LOG.CSV"
low = Sfile.lower()
print(low.startswith("sensor"))
print(low.endswith(".csv"))


# ------------------------------------
print("====== .strip() | 앞,뒤 공백 제거 =======")

# 공백 제거
# .strip() : 앞, 뒤 모든 공백 제거 (중간 띄어쓰기는 그대로 유지됨)
# .lstrip() : left(왼쪽) 공백만 제거
# .rstrip() : right(오른쪽) 공백만 제거


text = "   정상   "
print("[" + text.strip() + "]")  # [정상]
print("[" + text.lstrip() + "]")  # [정상   ]
print("[" + text.rstrip() + "]")  # [   정상]


# 문자열의 가운데 공백은 strip으로 지우지 못함
print("    정   상   ".strip())  # 정   상

print(text)  #
# strip은 재할당이나 새 변수에 할당하지 않은 이상 휘발됨.⭐⭐⭐

# strip 으로 문자 제거
str4 = "===정상==="
print(str4.strip("="))  # 정상
# 인자로 전달한 양 끝의 =이 모두 지워짐

str5 = "=정상========="
print(str5.strip("="))  # 정상
# 갯수 상관 없이 인자로 전달한 무자를 무조건 삭제
print(str5.strip("= "))
# strip 자체가 공백을 지우는 것이기 때문에
# 공백 상관없이 양 끝의 해당 문자열 삭제

str6 = "===정===상==="
print(str6.strip("="))  # 정===상
# 글자 중간에 있는 문자열은 건드리지 않음.

# ------------------------------------
print("====== 체이닝 : 메서드 연결하기 =======")

# 메서드 뒤에 또 메서드를 점으로 이어 붙이기
# text.strip().lower()는 공백 제거 후 소문자
# 읽는 순서는 왼쪽에서 오른쪽으로
# 정리 단계가 여러 개일 때 코드가 깔끔

raw = " NORMAL "

# 체이닝 X
step1 = raw.strip()  # 'NORMAL'
step2 = step1.lower()  # normal

# 체이닝 X, 기존 변수에 재할당
raw = raw.strip()  # 'NORMAL'
raw = raw.lower()  # normal

# 체이닝 O + 재할당
clean = raw.strip().lower()  # 'normal'
print(clean)

# 변수에 할당하지 않고 사용 가능
print(raw.strip().lower())


# 실습
str7 = "   Warning   "
str7 = str7.lower()
print("[" + str7 + "]")

str7 = str7.strip().lower()
print("[" + str7 + "]")


# 대소문자 - upper, lower, capitalize, title, isupper, islower
# 공백 - strip, lstrip, rstrip, strip(문자)
# 점으로 이어 붙이는 체이닝 가능


# strip() 메서드에 인자로 들어가는 문자열은 완전히 동일하지 않아도 삭제됨
str8 = "aaab 오잉 cd"
print(str8.strip("abcd"))  # " 오잉 "
print(str8.strip("abcd "))  # "오잉"
print(str8.strip("ab"))  # "오잉 cd"
print(str8.strip("bc"))  # "aaab 오잉 cd"


# GPT 질문 방법
str8 = "aaab 오잉 cd"
print(str8.strip("abcd"))  # " 오잉 "

# 지금 출력 결과는 " 오잉 " 이렇게 나오고 있어
# 내가 생각했을 때 ==처럼 정확하게 "abcd" 순서가 아니면 strip이 안될 줄 알았는데 실행 결과를 보니 순서랑 상관없이
# 인자로 전달한 문자열에 해당하는 글자가 확인하는 문자열 양 끝에 하나라도 있으면 동작하는 것 같아.
# 내가 이해한게 맞아?
# 그렇다면 왜 이렇게 동작하는거야?

# ------------------------------------
print("====== replace() =======")

# 특정 문자열을 제거하거나 치환할 떄 사용
# .replace("바꾸고싶은문자열", "바꿀문자열")
# 제거할 떄는 인자의 두 번째를 ""(빈문자열)로 작성

print("정 상 작 동".replace(" ", ""))  # 정상가동 (중간 공백 제거)
print("   정          상 작 동".replace(" ", ""))  # 정상가동 (모든 공백 제거)
print("   정   상 작 동".replace("  ", ""))  #  정 상 가 동 (2칸 공백만 제거)

# 글자 치환
print("고장".replace("고장", "fault"))  # fault
print("고장".replace("고", "fault"))  # fault장

# 단어 치환
str9 = "설비 정상 가동"
print(str9.replace("정상", "점검"))  # 설비 점검 가동

# replace() 체이닝
num = "    010-1234-1234   "
print(num.replace(" ", ""))  # 010-1234-1234
print(num.replace(" ", "").replace("-", ""))  # 01012341234


# ------------------------------------
print("====== split() =======")

# 문자열 자르기
# 결과는 대괄호에 감싸진 "리스트" 자료형
# 리스트는 순서가 있기 때문에 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

drinks = "에스크레소 아메리카노 카페라떼"
print(drinks.split())  # 인자를 보내지 않음
# ['에스크레소', '아메리카노', '카페라떼']
# "띄어쓰기"를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서 반환

# 구분자를 특정하고 싶은 경우
fruits = "딸기,망고스틴,수박,자몽,포도,키위,사쿠란보"
print(fruits.split(","))  # 문자열 콤마를 기준으로 분할
#['딸기', '망고스틴', '수박', '자몽', '포도', '키위', '사쿠란보']

fruits2 = "딸기, 망고스틴, 수박, 자몽, 포도, 키위, 사쿠란보"
print(fruits2.split(","))  # 문자열 콤마를 기준으로 분할
#['딸기', ' 망고스틴', ' 수박', ' 자몽', ' 포도', ' 키위', ' 사쿠란보'] -> 공백 그대로 유지

print(fruits2.split(", "))  # 문자열 콤마+공백 1칸을 기준으로 분할
#['딸기', '망고스틴', '수박', '자몽', '포도', '키위', '사쿠란보']

# 리스트의 인덱스
fruits_list = fruits.split(",")
print(fruits_list)

# 포도만 출력하기
print(fruits_list[5]) # 키위
print(fruits_list[3]) # 자몽
print(fruits_list[-1]) # 사쿠란보

# split 횟수 제한
num = "010-1234-1234"
# ["010","1234-1234"] 출력하고 싶음
print(num.split("-",1))

a = "a,b,c,d"
print(a.split(","))


# ------------------------------------
print("====== join() =======")

# 리스트를 하나의 문자열로 합침
# ⭐⭐⭐ "구분자".join(리스트) ⭐⭐⭐
# 모든 요소가 합쳐져서 하나의 문자열로 반환

fruits_list = ['딸기', '망고스틴', '수박', '자몽', '포도', '키위', '사쿠란보']
print("-".join(fruits_list))  # 딸기-망고스틴-수박-자몽-포도-키위-사쿠란보
print(",".join(fruits_list))  # 딸기,망고스틴,수박,자몽,포도,키위,사쿠란보


# 리스트 합치기 실습
list = ['2025','01','15']
print("-".join(list))

# 변수에 "python" 문자열  pyThon 출력

word = "python"

# 방법 1] strip + capitalize
print(word[:2] + word.strip("py").capitalize())  # thon

# 방법 2] replace
print(word.replace("t","T"))

# 방법 3] 슬라이싱 + T 만 upper 사용
print(word[:2] + word[2].upper() + word[3:])

# 방법 4] 인덱싱으로 글자 하나씩 연결
print(word[0]+word[1]+word[3].upper()+word[4]+word[5])

# 방법 5] 인덱싱 + strip + title
print(word[:2] + word.strip("py").title())  # thon

# 방법 6] split + join
print(word.split("t"))  # ['py', 'hon']
print("T".join(word.split("t"))) 
print(word[2].upper().join(word.split("t")))
print((word[2].upper()).join(word.split("t")))

